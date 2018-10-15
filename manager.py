from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

app = create_app('xfz')

manager = Manager(app=app)

manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()