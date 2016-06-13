from flask import render_template
from nemesis import app

@app.route('/')
def home():
    return render_template('gallery/index.html')
