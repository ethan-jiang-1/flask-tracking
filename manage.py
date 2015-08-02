# manage.py

from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)

@manager.command
def hello():
    print "hello"

@manager.command
def hello_Emma():
    print "hello Emma jiang, this line is typed by Emma & Dady,hello everybody I am Emma I am very happy to see you .Do you have queitions ?"

if __name__ == "__main__":
    manager.run()