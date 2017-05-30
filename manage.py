#!/usr/bin/env python
import os
from sqlalchemy import func
from app import create_app, db
from app.models import Hosts
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand


from script_commands import Setup, Test

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Hosts=Hosts, func=func)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=8000))
manager.add_command('setup', Setup())
manager.add_command('test', Test())

if __name__ == '__main__':
    manager.run()
