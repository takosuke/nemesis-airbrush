import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DevConfig')
app.config.from_pyfile('local_config.cfg', silent=True)

db = SQLAlchemy(app)

import views
from models import Image





