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

if __name__ == "__main__":
    manager.run()