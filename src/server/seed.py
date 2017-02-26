#!/usr/bin/python
from config import STATUS, ROLE_USER, ROLE_PREPOD, ROLE_ADMIN
from app.models import Lab, User, Task, Attempt, Group
from app import app, db, lm
from app.utils import create_hash

teacher1 = User(cart=1,
role=1,
password=create_hash("passwordpass1"),
lname = "Homich",
fname = "Vasiliy",
pname = "Vasilevich")

teacher2 = User(cart=2,
role=1,
password=create_hash("passwordpass2"),
lname = "Avramec",
fname = "Dmitry",
pname = "Alecsandrovich")

for course in xrange(1,5):
	for group in xrange(1,11):
		cur_group = Group(course=course,group_num=group)
		db.session.add(cur_group)

def find_group(course, group):
	return Group.query.filter_by(course=course, group_num=group).first()

teacher1.groups.append(find_group(2,6))
teacher1.groups.append(find_group(2,7))
teacher2.groups.append(find_group(2,9))

user1 = User(
	cart = 1521080,
	fname = "Kirill",
	lname = "Shasniy",
	pname = "Andreevich", 
	variant = 3)
user1.set_group(2, 6)
user3 = User(
	cart = 1521117,
	fname = "Vlada",
	lname = "Zaharova",
	pname = "Vadimovna", 
	variant = 2)
user3.set_group(2, 6)
user2 = User(
	cart = 1521107,
	fname = "Eugeniy",
	lname = "Saigak",
	pname = "Alekseevich", 
	variant = 7)
user2.set_group(2, 9)

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


db.session.add(teacher1)
db.session.add(teacher2)

db.session.add(user3)
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

