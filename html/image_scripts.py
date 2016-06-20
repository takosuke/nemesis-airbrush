import os, sys, random
from PIL import Image
from nemesis import app, db
from models import Image as Nemesis_Image

def random_full_size():
    return random.randint(700, 1100)

def random_thmb_size():
    return random.randint(250, 500)

def import_images(category, inpath=app.config['SOURCE_IMAGES']):
    outpath = os.path.join(app.config['SERVE_IMAGE_PATH'], category)
    filelist = os.listdir(os.path.join(inpath, category))
    filelist = [x for x in filelist if os.path.splitext(x)[-1] == '.jpg' \
            or os.path.splitext(x)[-1] == '.jpeg'\
            or os.path.splitext(x)[-1] == '.gif']
    print(filelist)
    for filename in filelist:
        fullsize = random_full_size(), random_full_size()
        thmbsize = random_thmb_size(), random_thmb_size()
        try:
            im = Image.open(os.path.join(inpath, category, filename))
            im.thumbnail(fullsize)
            im.save((os.path.join(outpath, filename)), 'JPEG')
            im = Image.open(os.path.join(inpath, category, filename))
            im.thumbnail(thmbsize)
            im.save((os.path.join(outpath, 'thmb', filename)), 'JPEG')

            new_image = Nemesis_Image(filename=filename, category=category)
            db.session.add(new_image)

        except IOError:
            print("Cannot create image for ", filename)

        db.session.commit()

if __name__ == '__main__':                        
    import_images('works')
    import_images('workinprogress')
