import os
from flask import render_template
from nemesis import app

@app.route('/')
def home():
    return render_template('gallery/index.html')

@app.route('/works/')
def works():
    thumbnails = get_images()
    print(thumbnails)
    return render_template('gallery/gallery.html', thumbnails=thumbnails)


def get_images():
    files = os.listdir('static/img/thmb/')
    images = [os.path.join('/static/img/thmb/', os.path.splitext(x)[:-1]) for x in files if os.path.splitext(x)[-1] in ('.jpg','.jpeg')]
    return images
