import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI='sqlite:///db/nemesis.db',
    FLASK_DEBUG=1,
    BASE_DIR=os.path.abspath(os.path.dirname(__file__)),
    SOURCE_IMAGES=os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'project_files', 'images', 'edited'),
    SERVE_IMAGE_PATH=os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'project_files', 'images', 'serve')
))


app.config.from_envvar('NEMESIS_SETTINGS', silent=True)

db = SQLAlchemy(app)

import views
from models import Image





