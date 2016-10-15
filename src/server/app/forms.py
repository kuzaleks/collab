from flask.ext.wtf import Form
from wtforms import TextField, FileField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Required, Length
from models import User, Lab, Task

class LoginForm(Form):
    number = TextField('number', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class TaskSendForm(Form):
    task = FileField('task', validators = [Required()])

class ConditionForm(Form):
    name = TextField('name', validators = [Required()])
    condition = TextAreaField('condition', validators = [Required()])