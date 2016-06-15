from nemesis import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150), unique=True)
    category = db.Column(db.String(40))
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Image %r %r>' % (self.filename, self.category)

