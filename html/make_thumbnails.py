import os, sys
from PIL import Image

size = (128, 128)

def make_thumbnails(inpath='static/img/uploads'):
    for file in os.listdir(inpath):
        outfile = os.path.splitext(file)[0] + '.thmb.jpg'
        if file != outfile:
            try:
                im = Image.open(os.path.join(inpath, file))
                im.thumbnail(size)
                im.save((os.path.join('static/img/thmb', outfile)), 'JPEG')
            except IOError:
                print("Cannot create thumbnail for ", file)

if __name__ == '__main__':                        
    make_thumbnails()
