from application import db
from flask import jsonify
from application.models import Record


db.drop_all()
db.create_all()

asdf = Record(int_one=2,int_two=4,sum=6)
asdff = Record(int_one=3,int_two=4,sum=7)
db.session.add(asdf)
db.session.commit()
db.session.add(asdff)
db.session.commit()

for item in Record.query.all():
    print(item.id, item.int_one, item.int_two, item.sum)

output = {}
for row in Record.query.all():
    output[row.id] = [str(row.int_one), str(row.int_two), str(row.sum)]


print(output)