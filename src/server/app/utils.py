from werkzeug.utils import secure_filename
from config import STATUS
import os, subprocess
from models import Lab, User, Task, Attempt
from module import merge

def save(file, folderpath):
	filename = secure_filename(file.filename)
	filepath = folderpath + filename
	file.save(filepath)

def dirs_create(folderpath):
	if not os.path.exists(os.path.dirname(folderpath)):
		try:
			os.makedirs(os.path.dirname(folderpath))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

def task_compile(folderpath):
	p = subprocess.call("g++ *.cpp", cwd=folderpath, shell=True)
	return p

def clear_dir(folderpath):
	subprocess.call("rm *.*", cwd=folderpath, shell=True)

def path_generate(lab, task, variant, cart):
	return 'uploads/' + "/".join([str(lab), str(task), str(variant), str(cart)]) + "/"

def check_task(folderpath):

	if task_compile(folderpath):
		return STATUS['CompileError']

	# if not task_run(folderpath):
	# 	return STATUS.RuntimeError

	# if not check_answer(folderpath):
	# 	return STATUS.AnswerError

	return STATUS['SUCCESS']

def get_status(code):
	if code == None:
		return 0
	for key, value in STATUS.iteritems():
		if value == code:
			return key

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

# Tasks table of user with solving status
def users_tasks(cart):
	user = User.query.filter_by(cart = cart).first()
	
	name = " ".join([user.lname, user.fname, user.pname])
	attempts = user.attempts

	lab_task = merge(Task.query.all(), Lab.query.all())		

	result = {}
	for lab in lab_task:
		result[lab] = []
		for task in lab_task[lab]:
			temp = attempts.filter_by(lab_num = lab, task_num = task).all()
			cur_attempts = sorted( temp, key = lambda attempt: attempt.timestamp )[::-1]
			attempt = get_first(cur_attempts)
			if attempt:
				result[lab].append(attempt.status)
			else:
				result[lab].append(None)
	return result

'''
from config import STATUS, ROLE_USER, ROLE_PREPOD, ROLE_ADMIN
from app.models import Lab, User, Task, Attempt
from app import app, db, lm

user = User(cart=1,
role=1,
keyword="passwordpass",
fname = "Teacher\'s name",
lname = "Teacher\'s last name",
pname = "Teacher\'s patronymic")


user1 = User(cart = 1521080,fname = "Kirill",lname = "Schastny",pname = "Andreevich",course = 2,group = 6,variant = 3, role=0)
user2 = User(cart = 1521107,fname = "Evgeniy",lname = "Saigak",pname = "Alekseevich",course = 2,group = 9,variant = 7, role=0)

lab = Lab(difficulty = 0, num = 1, name = "if")

task0 = Task(num = 1, lab_num = 1)
task01 = Task(num = 2, lab_num = 1)
task02 = Task(num = 3, lab_num = 1)
task03 = Task(num = 4, lab_num = 1)


lab1 = Lab(difficulty = 0, num = 2, name = "for")

task1 = Task(num = 1, lab_num = 2)
task11 = Task(num = 2, lab_num = 2)
task12 = Task(num = 3, lab_num = 2)


lab3 = Lab(difficulty = 0, num = 3, name = "while")

task2 = Task(num = 1, lab_num = 3)
task21 = Task(num = 2, lab_num = 3)
task22 = Task(num = 3, lab_num = 3)


lab4 = Lab(difficulty = 0, num = 4, name = "do while")

task3 = Task(num = 1, lab_num = 4)
task31 = Task(num = 2, lab_num = 4)
task32 = Task(num = 3, lab_num = 4)


db.session.add(user)
db.session.add(user1)
db.session.add(user2)
db.session.add(lab)
db.session.add(task0)
db.session.add(task01)
db.session.add(task02)
db.session.add(task03)
db.session.add(lab1)
db.session.add(task1)
db.session.add(task11)
db.session.add(task12)
db.session.add(lab3)
db.session.add(task2)
db.session.add(task21)
db.session.add(task22)
db.session.add(lab4)
db.session.add(task3)
db.session.add(task31)
db.session.add(task32)

db.session.commit()

'''