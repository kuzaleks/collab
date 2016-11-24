from flask import render_template, flash, redirect, session, url_for, request, g, request
from flask.ext.login import login_user, logout_user, current_user, login_required, UserMixin
from app import app, db, lm
from forms import LoginForm, TaskSendForm, ConditionForm, UserUpdateForm
from models import Lab, User, Task, Attempt, Group
from datetime import datetime
from utils import save, check_task, path_generate, get_status, users_tasks, clear_dir, dirs_create, create_hash
from config import STATUS, ROLE_USER, ROLE_PREPOD, ROLE_ADMIN, SALT
from module import merge, biggest_lab_length, merge_obj
from os.path import isfile
from template import task_generate, task_regenerate
from functools import wraps
import collections

"""
Routes:
	/logout
	/
	/index
	/login
	/user/<int:cart>
	/all_attempts
	/all_users
	/choose_task
	/task/<int:task_id>
	/edit
	/add_task
"""

def prepod_only(f):
	@wraps(f)
	def decorator(*args, **kwargs):
		if g.user.is_prepod():
			return f(*args, **kwargs)
		else:
			return redirect(url_for('index'))
	return decorator

@lm.user_loader
def get_user(ident):
  return User.query.get(int(ident))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@login_required
def index():
	return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user and g.user.is_authenticated:
		return redirect(url_for('index'))
	
	form = LoginForm()
	
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		users_with_lname = User.query.filter_by(lname = form.lastname.data)
		user = 0
		if form.cart.data:
			user = users_with_lname.filter_by(cart = form.cart.data).first()
		if not user and form.password.data:
			user = users_with_lname.filter_by(password = create_hash(form.password.data)).first()

		if not user:
			try:
				user = User.query.filter_by(cart = int(form.cart.data), lname = form.lastname.data).first()
			except Exception as e:
				flash("User not found.")
				return render_template('login.html', 
					title = 'Sign In',
					form = form)
		
		# user was found
		return after_login(user, form.cart.data)

	return render_template('login.html', 
		title = 'Sign In',
		form = form)

def after_login(user, cart):
	if user is None:
		flash("User not found.")
		return redirect(url_for('login'))

	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)

	return redirect(request.args.get('next') or url_for('index'))

@app.route('/user/<int:cart>', methods = ['GET', 'POST'])
@login_required
def user(cart):
	user = User.query.filter_by(cart = cart).first()

	if not user or (g.user.is_prepod() and not user.get_group_obj() in g.user.groups):
		return redirect(url_for('index'))        

	table = merge(Task.query.all(), Lab.query.all())
	table_width = biggest_lab_length(table)

	return render_template('user.html',
		user = user,
		attempts = Attempt.query.filter_by(user_id = user.id).all()[::-1],
		table = table,
		table_width = table_width,
		get_status = get_status,
		users_tasks = users_tasks)

@app.route('/all_attempts')
@login_required
def all_attempts():
	attempts = Attempt.query.filter_by(user_id = g.user.id).all()

	return render_template('all_attempts.html',
		attempts = reversed(attempts),
		get_status = get_status)

@app.route('/all_users')
@login_required
@prepod_only
def all_users():

	users = [user for user in User.query.filter_by(role = ROLE_USER).all() if user.get_group_obj() in g.user.groups]

	table = merge(Task.query.all(), Lab.query.all())
	table_width = biggest_lab_length(table)

	return render_template('users_table.html',
		users = users,
		table = table,
		get_status = get_status,
		table_width = table_width,
		users_tasks = users_tasks)

@app.route('/choose_task')
@login_required
def choose_task():
	table = merge_obj(Task.query.all(), Lab.query.all())
	table = collections.OrderedDict(sorted(table.items()))

	return render_template('choose_task.html', table = table)

@app.route('/task/<int:task_id>', methods=('GET', 'POST'))
@login_required
def task(task_id):
	task = Task.query.filter_by(id = task_id).first()

	if not task:
		return redirect('/choose_task')
	
	filepath = "tasks/" + str(task_id) + ".html"
	full_filepath = "app/templates/" + filepath

	taskSendForm = TaskSendForm()
	conditionForm = ConditionForm()

	# on new attempt
	if taskSendForm.validate_on_submit():
		folderpath = path_generate(task.lab_num, task.num, g.user.variant, g.user.cart)
		files = request.files.getlist("task")
		dirs_create(folderpath)
		clear_dir(folderpath)
		for file in files:
			save(file, folderpath)
		attempt = Attempt(
			timestamp = datetime.utcnow(), 
			author = g.user, 
			status = check_task(folderpath),
			task = task)
		db.session.add(attempt)
		db.session.commit()

	# on task add
	if conditionForm.validate_on_submit():
		# save condition to file
		task_text = task_generate(
			name = conditionForm.name.data,
			text = conditionForm.condition.data)
		with open(full_filepath, 'w') as f:
			f.write(task_text)
	
	return render_template('task.html',
		user = g.user,
		attempts = Attempt.query.filter_by(user_id = g.user.id, task = task).all()[::-1],
		task_id = task_id,
		get_status = get_status,
		condition = filepath,
		task_exist = isfile(full_filepath),
		taskSendForm = taskSendForm,
		conditionForm = conditionForm)

@app.route('/edit', methods=('GET', 'POST'))
@login_required
@prepod_only
def edit():
	userForm = UserUpdateForm()

	cart = request.args.get('cart')
	user = User.query.filter_by(cart = cart).first()
	if not user:
		user = User()
		user.cart = cart

	groups = user.groups_to_string()
	
	course = None
	group = None
	
	if not user.is_prepod():
		users_group = {}
		if len(user.groups):
			users_group = user.groups[0]
			course = users_group.course
			group = users_group.group_num
	else:
		group = groups

	if user:
		if  userForm.validate_on_submit():
			
			user.fname = userForm.fname.data
			user.lname = userForm.lname.data
			user.pname = userForm.pname.data
			
			if userForm.group.data and userForm.course.data:
				user.set_group(userForm.course.data, userForm.group.data)
			else:
				user.update_groups_list(userForm.group.data)
			
			user.variant = userForm.variant.data

			db.session.add(user)
			db.session.commit()

			return redirect(url_for("user", cart=cart))

		return render_template('edit.html', 
			userForm = userForm,
			is_prepod = user.is_prepod(),
			fname = user.fname,
			lname = user.lname,
			pname = user.pname,
			course = course,
			group = group,
			variant = user.variant)
	else:
		return redirect(url_for("index"))

@app.route('/add_task', methods=('GET', 'POST'))
@login_required
@prepod_only
def add_task():
	
	conditionForm = ConditionForm()
	task = 0
	id = request.args.get('id')
	lab_num = request.args.get('lab')
	
	is_exist = bool(id) or bool(lab_num)
	
	if lab_num:
		try:
			lab = Lab.query.filter_by(num = lab_num).first()
			if not conditionForm.validate_on_submit():
				lab.add_task()
			task = Task.query.all()[::-1][0]
			id = task.id
		except Exception as e:
			print "Exception: ", e
	else:
		task = task or Task.query.filter_by(id = id).first() or Task()
	

	filepath = "tasks/" + str(id) + ".html"
	full_filepath = "app/templates/" + filepath

	if conditionForm.validate_on_submit():
		# save condition to file
		task.lab_num = conditionForm.lab.data
		task.num = conditionForm.task.data
		db.session.add(task)
		db.session.commit()

		task_condition = task_generate(
			name = conditionForm.name.data,
			text = request.form['condition'])

		with open(full_filepath, 'w') as f:
			f.write(task_condition)

		return redirect(url_for('task', task_id = task.id))

	if is_exist:
		text = ""
		name = ""
		try:
			with open(full_filepath, 'r') as f:
				text = f.read().decode('utf-8')
			name, text = task_regenerate(text)
		except Exception as e:
			print "Reading file exception:", e

		return render_template('add_task.html', 
			conditionForm = conditionForm,
			lab = task.lab_num,
			num = task.num,
			name = name,
			text = text)
	else:
		return render_template('add_task.html', 
			conditionForm = conditionForm)

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	return render_template('500.html'), 500