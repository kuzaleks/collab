from flask import render_template, flash, redirect, session, url_for, request, g, request
from flask.ext.login import login_user, logout_user, current_user, login_required, UserMixin
from app import app, db, lm
from forms import LoginForm, TaskSendForm
from models import Lab, User, Task, Attempt
from datetime import datetime
from utils import save, check_task, path_generate, get_status, users_tasks, clear_dir, dirs_create
from config import STATUS, ROLE_USER, ROLE_PREPOD, ROLE_ADMIN
from module import merge, biggest_lab_length
from os.path import isfile

# TODO: sort by column at all_users page

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
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user = User.query.filter_by(keyword = form.number.data).first()
        if not user:
            try:
                user = User.query.filter_by(cart = int(form.number.data)).first()
            except Exception as e:
                # print "NOUP"
                return render_template('login.html', 
                    title = 'Sign In',
                    form = form)
        # print "IT'S OK"
        return after_login(user, form.number.data)
    return render_template('login.html', 
        title = 'Sign In',
        form = form)


@app.route('/user/<int:cart>', methods = ['GET', 'POST'])
@login_required
def user(cart):
    users_tasks(cart)
    user = User.query.filter_by(cart = cart).first()

    table = merge(Task.query.all(), Lab.query.all())
    table_width = biggest_lab_length(table)

    return render_template('user.html',
        attempts = Attempt.query.filter_by(user_id = user.id).all()[::-1],
        get_status = get_status,
        user = user,
        table = table,
        table_width = table_width,
        users_tasks = users_tasks)

def after_login(user, number):
    if user is None:
        user = User(cart = number) # TODO: Remove
        db.session.add(user)
        db.session.commit()

    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/all_attempts')
@login_required
def all_attempts():
    attempts = Attempt.query.filter_by(user_id = g.user.id).all()
    if attempts == None:
        flash('Tries not found.')
        return redirect(url_for('index'))

    return render_template('all_attempts.html',
        attempts = attempts[::-1],
        get_status = get_status)

@app.route('/all_users')
@login_required
def all_users():
    if not g.user.is_prepod():
        flash('U are just user.')
        return redirect(url_for('index'))
    users = User.query.filter_by(role = ROLE_USER).all()
    if users == None:
        flash('Users not found.')
        return redirect(url_for('index'))

    table = merge(Task.query.all(), Lab.query.all())
    table_width = biggest_lab_length(table)

    return render_template('users_table.html',
        users = users,
        table = table,
        get_status = get_status,
        table_width = table_width,
        users_tasks = users_tasks)

@app.route('/upload')
@login_required
def choose_lab():
    labs = Lab.query.all()
    return render_template('choose_lab.html', labs = labs)

@app.route('/upload/<int:lab_num>')
@login_required
def choose_task(lab_num):
    tasks = Task.query.filter_by(lab_num = lab_num)
    return render_template('choose_task.html', lab_num = lab_num, tasks = tasks)

@app.route('/upload/<int:lab_num>/<int:task>', methods=('GET', 'POST'))
@login_required
def upload(lab_num, task):
    form = TaskSendForm()
    if form.validate_on_submit():
        folderpath = path_generate(lab_num, task, g.user.variant, g.user.cart)
        files = request.files.getlist("task")
        dirs_create(folderpath)
        clear_dir(folderpath)
        for file in files:
            save(file, folderpath)
        attempt = Attempt(
            timestamp = datetime.utcnow(), 
            author = g.user, 
            status = check_task(folderpath),
            lab_num = lab_num,
            task_num = task)
        db.session.add(attempt)
        db.session.commit()

    id = Task.query.filter_by(lab_num=lab_num, num=task).first().id
    filepath = "tasks/" + str(id) + ".html"
    task_exist = True

    if not isfile("app/templates/" + filepath):
        filepath = "add_task.html"
        task_exist = False
    
    return render_template('upload.html',
        attempts = Attempt.query.filter_by(user_id = g.user.id, lab_num = lab_num, task_num = task).all()[::-1],
        user = g.user,
        form = form,
        get_status = get_status,
        condition = filepath,
        task_exist = task_exist)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

'''

Admin:
    Add task
    Edit task
    Watch students table
        ...
        cart    name    sname   ...
        /\(on click)
            ...
            try[i]: task_num    status  ...
            ...
        ...
    Watch table for each student
    Add student

'''