from application import db

class Colour_Statement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    colour = db.Column(db.String(20), nullable=False)
    statement = db.Column(db.String(50), nullable=False)
