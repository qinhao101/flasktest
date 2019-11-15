from app.config import Config
from flask_script import Manager,Command
from flask_wtf import CSRFProtect
from flask_script import Manager
from app import app


# app.config.from_object(Config)

CSRFProtect(app)
manage = Manager(app)

class CommandTest(Command):
    def run(self):
        print('this is a test for Command')


manage.add_command('hello', CommandTest)

if __name__ == '__main__':
    manage.run(default_command='runserver')
    # manage.run()