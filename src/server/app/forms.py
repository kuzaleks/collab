from flask.ext.wtf import Form
from wtforms import TextField, FileField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Required, Length
from models import User, Lab, Task

class LoginForm(Form):
	cart = TextField('number')
	password = PasswordField('number')
	lastname = TextField('lastname', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class TaskSendForm(Form):
	task = FileField('task', validators = [Required()])

class ConditionForm(Form):
	lab = TextField('lab', validators = [Required()])
	task = TextField('task', validators = [Required()])
	name = TextField('name')

class UserUpdateForm(Form):
	fname = TextField('fname', validators = [Required()])
	lname = TextField('lname', validators = [Required()])
	pname = TextField('pname', validators = [Required()])

	course = TextField('course')
	group = TextField('group')
	
	variant = TextField('variant')