from flask.ext.login import UserMixin
from app import db
from hashlib import md5
from config import ROLE_USER, ROLE_PREPOD, ROLE_ADMIN, PART_A, PART_B, STATUS

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	cart = db.Column(db.Integer)

	fname = db.Column(db.String(50))
	lname = db.Column(db.String(50))
	pname = db.Column(db.String(50))

	course = db.Column(db.Integer)
	group = db.Column(db.Integer)
	
	variant = db.Column(db.Integer)
	attempts = db.relationship('Attempt', backref = 'author', lazy = 'dynamic')
	
	role = db.Column(db.Integer, default=ROLE_USER)
	keyword = db.Column(db.String(50), default="") # for prepod

	def __repr__(self):
		return '<User %r>' % (self.cart)

	def is_authenticated(self):
		return True

	def is_prepod(self):
		if self.role == ROLE_PREPOD or self.role == ROLE_ADMIN:
			return True
		return False

class Lab(db.Model):
	id = db.Column(db.Integer, primary_key = True)

	#: PART_A or PART_B depends on difficulty
	difficulty = db.Column(db.Integer)

	#: Tasks at the lab
	tasks = db.relationship('Task', backref = 'lab', lazy = 'dynamic')
	
	#: Number of the lab
	num = db.Column(db.Integer)

	#: Name of the lab
	name = db.Column(db.String(50))
	
	def __repr__(self):
		return '<Lab %r>' % (self.id)

	def __gt__(self, lab2):
		return self.num > lab2.num

class Task(db.Model):
	# text at app/templates/tasks/{{task.id}}.html
	id = db.Column(db.Integer, primary_key = True)
	
	lab_num = db.Column(db.Integer, db.ForeignKey('lab.num'))
	num = db.Column(db.Integer)
	
	def __repr__(self):
		return '<Task %r>' % (self.id)

class Attempt(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	status = db.Column(db.Integer)
	timestamp = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	lab_num = db.Column(db.Integer)
	task_num = db.Column(db.Integer)
	
	def __repr__(self):
		return '<Attempt %r>' % (self.id)