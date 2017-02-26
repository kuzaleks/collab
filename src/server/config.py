# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'ale4u8lasfhkuke47ghaslg'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

ROLE_USER = 0
ROLE_PREPOD = 1
ROLE_ADMIN = 2

STATUS = {
	"SUCCESS": 0,
	"CompileError": 1,
	"RuntimeError": 2,
	"IncorrectAnswer": 3
}

class Column:
	def __init__(self, name, f):
		self.name = name.decode('utf-8')
		self.f = f

COLUMNS = [
	Column("Студенческий", 	lambda x : x.cart),
	Column("Фамилия", 		lambda x : x.lname),
	Column("Имя", 			lambda x : x.fname),
	Column("Отчество", 		lambda x : x.pname),
	Column("Курс", 			lambda x : x.get_course()),
	Column("Группа", 		lambda x : x.get_group()),
	Column("Вариант", 		lambda x : x.variant)
]

SALT = "nHh3O4j6Hz7EmVAV"