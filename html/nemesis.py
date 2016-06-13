from flask import Flask
app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
 #   DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    FLASK_DEBUG=1
#    USERNAME='admin',
#    PASSWORD='default'
))

app.config.from_envvar('NEMESIS_SETTINGS', silent=True)

import views
