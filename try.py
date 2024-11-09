from app import db, app
from app.models import Students, Applications


with app.app_context():
    x = Applications.query.join(Students)
    for i in x:
        print(i.students.name)