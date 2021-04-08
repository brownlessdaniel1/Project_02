from app import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    int_one = db.Column(db.Integer, nullable=False)
    int_two = db.Column(db.Integer, nullable=False)
    sum = db.Column(db.Integer, nullable=False)

db.drop_all()
db.create_all()
