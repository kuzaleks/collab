from werkzeug.utils import secure_filename
from config import STATUS, SALT
from models import Lab, User, Task, Attempt
from module import merge
import os, subprocess
import hashlib
import random

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
		return "None"
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
		for id in lab_task[lab]:
			temp = attempts.filter_by(task_id = id).all()
			cur_attempts = sorted( temp, key = lambda attempt: attempt.timestamp )[::-1]
			attempt = get_first(cur_attempts)
			if attempt:
				result[lab].append(attempt.status)
			else:
				result[lab].append(None)
	return result

def salt_generator(length = 16):
	ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	chars=[]
	for i in range(length):
		chars.append(random.choice(ALPHABET))

	return "".join(chars)


def create_hash(password):
	# if not salt: 
	# 	salt = salt_generator()
	return hashlib.sha512(password.encode('utf-8') + SALT).hexdigest()