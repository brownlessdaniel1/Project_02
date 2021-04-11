from application import db
from flask import jsonify
from application.models import Colour_Statement


db.drop_all()
db.create_all()

row_1 = Colour_Statement(name="Dan", colour="Green", statement="Dan likes Green!")
row_2 = Colour_Statement(name="Dan", colour="Blue", statement="Dan likes Blue!")
row_3 = Colour_Statement(name="Dan", colour="Red", statement="Dan likes Red!")
row_4 = Colour_Statement(name="Dan", colour="Purple", statement="Dan likes Purple!")
db.session.add(row_1)
db.session.add(row_2)
db.session.add(row_3)
db.session.add(row_4)
db.session.commit()

for item in Colour_Statement.query.all():
    print(item.id, item.name, item.colour, item.statement)
