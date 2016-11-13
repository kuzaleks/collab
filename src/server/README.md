# Task Check System(TCS)


### Installation

TCS requires [Python 2](https://www.python.org/downloads/).

TCS work with [SQLite](https://sqlite.org/).

#### TCS installation

You need clone the repository.

Create database
```sh
# chmod +x ./db_create.py
$ ./db_create.py
```

Then navigate into the folder, and run:
```sh
# chmod +x ./run.py
$ ./run.py
```

### Todos
	For Teacher and Admin:
	 - Edit task
	 - Add student

### Hierarchy

	.
	├── app - folder with our server's heart
	│   ├── forms.py - all forms definition
	│   ├── __init__.py - server initializing
	│   ├── models.py - object models. (database objects)
	│   ├── module.py - some functions
	│   ├── static - static files(scripts/styles/images)
	│   │   ├── css
	│   │   │   └── *.css
	│   │   ├── img
	│   │   │   └── *.png
	│   │   └── js
	│   │       └── *.js
	│   ├── templates - pages templates(for jinja2)
	│   │   ├── *.html
	│   │   ├── tasks - folder with tasks conditions
	│   │   │   ├── 1.html
	│   │   │   ├── 2.html
	│   │   │   ├── 3.html
	│   │   │   ├── 4.html
	│   │   │   └── 5.html
	│   ├── utils.py - different needed functions
	│   ├── views.py - all routes and server logic
	├── app.db - database
	├── config.py - config file
	├── db_create.py - script to create database
	├── db_migrate.py - script to add migration for database(update tables)
	├── db_repository - dir with database stuff
	├── db_upgrade.py - downgrade your database. -1 migration
	├── prun.py - production run(no debug)
	├── README.md - Hello. It's me...
	├── run.py - run server
	└── tmp - temporary stuff

### Errors

 - /usr/bin/python^M: bad interpreter: No such file or directory
 	=> cat ./{FILE_NAME}.py | tr -d '\r' > ./{FILE_NAME}.py
