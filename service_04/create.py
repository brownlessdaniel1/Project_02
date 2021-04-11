from application import db
from flask import jsonify
from application.models import Colour_Statement


db.drop_all()
db.create_all()

row_1 = Colour_Statement(name="Dan", colour="Green", statement="Dan likes Green!")

db.session.add(row_1)

db.session.commit()

for item in Colour_Statement.query.all():
    print(item.id, item.name, item.colour, item.statement)
