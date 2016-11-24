from flask.ext.login import UserMixin
from app import db
from hashlib import md5
from config import ROLE_USER, ROLE_PREPOD, ROLE_ADMIN, PART_A, PART_B, STATUS

association_table = db.Table('association', db.metadata,
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)

class User(db.Model, UserMixin):

	# For both teacher and student
	id = db.Column(db.Integer, primary_key = True)
	
	fname = db.Column(db.String(50))
	lname = db.Column(db.String(50))
	pname = db.Column(db.String(50))

	role = db.Column(db.Integer, default=ROLE_USER)

	# For student
	cart = db.Column(db.Integer)
	
	variant = db.Column(db.Integer)
	attempts = db.relationship('Attempt', backref = 'author', lazy = 'dynamic')

	# For teacher
	password = db.Column(db.String(150), default="")
	salt = db.Column(db.String(150), default="")
	groups = db.relationship("Group", secondary=association_table, back_populates="users")

	def __repr__(self):
		return '<User %r>' % (self.lname)

	def is_authenticated(self):
		return True

	def get_course(self):
		if len(self.groups) == 1 and not self.is_prepod():
			return self.groups[0].course

	def get_group(self):
		if len(self.groups) == 1 and not self.is_prepod():
			return self.groups[0].group_num

	def get_group_obj(self):
		if len(self.groups) == 1 and not self.is_prepod():
			return self.groups[0]

	def groups_to_string(self):
		return ", ".join("%s/%s" % (group.course, group.group_num) for group in self.groups)

	def clear_groups_list(self):
		self.groups = []

	def update_groups_list(self, groups_string):
		self.clear_groups_list()
		groups = [(s.strip().split('/')) for s in groups_string.split(",")]
		for _course, _group in groups:
			group = Group.query.filter_by(course=_course, group_num=_group).first()
			if group:
				self.groups.append(group)

	def set_group(self, course, group_num):
		self.clear_groups_list()
		group = Group.query.filter_by(course=course, group_num=group_num).first()
		if group:
			self.groups.append(group)

	def is_prepod(self):
		if self.role == ROLE_PREPOD or self.role == ROLE_ADMIN:
			return True
		return False

class Group(db.Model):
	id = db.Column(db.Integer, primary_key = True)

	course = db.Column(db.Integer)
	group_num = db.Column(db.Integer)


	users = db.relationship(
		"User",
		secondary=association_table,
		back_populates="groups")

	def __repr__(self):
		return '<Group %r/%r>' % (self.course, self.group_num)


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

	def add_task(self):
		new_task = Task(num = len(self.tasks.all()) + 1, lab_num = self.num)
		db.session.add(new_task)
		db.session.commit()
	
	def __repr__(self):
		return '<Lab %r>' % (self.id)

	def __gt__(self, lab2):
		return self.num > lab2.num

class Task(db.Model):
	# text at app/templates/tasks/{{task.id}}.html
	id = db.Column(db.Integer, primary_key = True)
	
	lab_num = db.Column(db.Integer, db.ForeignKey('lab.num'))
	num = db.Column(db.Integer)
	attempts = db.relationship('Attempt', backref = 'task', lazy = 'dynamic')
	
	def __repr__(self):
		return '<Task %r>' % (self.id)

class Attempt(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	status = db.Column(db.Integer)
	timestamp = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	task_id = db.Column(db.Integer, db.ForeignKey('task.id'))

	def __repr__(self):
		return '<Attempt %r>' % (self.id)