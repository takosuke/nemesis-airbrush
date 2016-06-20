import os
from flask import render_template
from nemesis import app
from models import Image
import random

@app.route('/')
def home():
    return render_template('gallery/index.html')

@app.route('/works/')
def works():
#    images = random.shuffle(Image.query.all())[0:10]
    images = Image.query.filter(Image.category == 'works').all()
    return render_template('gallery/gallery.html', images=images)

@app.route('/workinprogress/')
def workinprogress():
#    images = random.shuffle(Image.query.all())[0:10]
    images = Image.query.filter(Image.category == 'workinprogress').all()
    return render_template('gallery/workinprogress.html', images=images)

@app.route('/about/')
def about():
    return render_template('gallery/about.html')

@app.route('/shop/')
def shop():
    return render_template('gallery/shop.html')

@app.route('/contact/')
def contact():
    return render_template('gallery/contact.html')

