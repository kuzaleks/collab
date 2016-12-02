# -*- coding: utf-8 -*-
from werkzeug.utils import secure_filename
from config import STATUS, SALT
from models import Lab, User, Task, Attempt
from module import merge
import os, subprocess
import hashlib
import random
import json

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

def clear_dir(folderpath):
	subprocess.call("rm *.*", cwd=folderpath, shell=True)

def path_generate(elems):
	return 'uploads/' + "/".join([str(elem if elem else 1) for elem in elems]) + "/"

def run_command(command, input_args=[], cwd=os.path.dirname(os.path.abspath(__file__))):
	# cwd=cwd.replace('//', '/')
	task = subprocess.Popen(command, 
		stdout=subprocess.PIPE, 
		stdin=subprocess.PIPE, 
		stderr=subprocess.PIPE,
		cwd=cwd,
		shell=True)

	out, err = task.communicate(
		input="\n".join(str(arg) for arg in input_args)
	)

	return out, err

def task_compile(folderpath):
	try:
		comp = subprocess.check_output(
			"g++ *.cpp",
			cwd=folderpath,
			stderr=subprocess.STDOUT,
			shell=True
		)
	except subprocess.CalledProcessError, e:
		print "Compilation stdout output:\n", e.output
		return e.output
	return 0

def task_run(path_to_bin, input_args, expected_output):		
	out, err = run_command([path_to_bin], input_args)
	print "out:", out, "; err:", err
	return out.strip() == expected_output

def parse(path):
	parts = [str(a) for a in path.split('/')]

	options = {
		"lab" : parts[1],
		"task" : parts[2],
		"variant" : parts[3],
		"cart" : parts[4]
	}
	
	return options

def check_task(folderpath):

	options = parse(folderpath)
	
	compile_result = task_compile(folderpath)
	
	
	if compile_result:
		return {
			"status": STATUS['CompileError'],
			"message": "\n".join(compile_result.split('g++:'))
		}

	i = 0
	for test in get_tests(options["lab"], options["task"], options["variant"]):
		i += 1
		if not task_run(os.path.join("../", folderpath, "a.out"), test[0], test[1]):
			return {
				"status": STATUS['IncorrectAnswer'],
				"message": "Тест %s Не пройден." % i
			}

	return {
		"status": STATUS['SUCCESS'],
		"message": "Все тесты пройдены успешно."
	}

def get_tests(lab, task, variant=None):
	
	tests_string = ""
	path = os.path.join(os.getcwd(), "uploads/" + str(lab) + "/" + str(task) + "/tests.json")
	
	with open(path, "r") as f:
		for line in f:
			tests_string += line
	tests = json.loads(tests_string)

	return tests[int(variant)-1] if int(variant) else tests

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
	return hashlib.sha512(password.encode('utf-8') + SALT).hexdigest()