from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI='sqlite:///db/nemesis.db',
    FLASK_DEBUG=1
))


app.config.from_envvar('NEMESIS_SETTINGS', silent=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

import views
from models import Image

if __name__ == '__main__':
    manager.run()

