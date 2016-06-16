import os

class BaseConfig(object):
    SECRET_KEY='development key'
    SQLALCHEMY_DATABASE_URI='sqlite:///db/nemesis.db'
    FLASK_DEBUG=1
    BASE_DIR=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(BaseConfig):
    SOURCE_IMAGES=os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'project_files', 'images', 'edited')
    SERVE_IMAGE_PATH=os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'project_files', 'images', 'serve')
