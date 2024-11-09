import datetime
import sys

from app import app, bcrypt
from app.models import (Applications, ApplicationStatus, Courses, Deans,
                        Professors, Students, db)

print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])

with app.app_context():
    db.create_all()
    print("Database created")


    p1 = Professors(name="Prof 1", mail="sapnambhardwaj@gmail.com")
    p2 = Professors(name="Prof 2", mail="sapnambhardwaj@gmail.com")
    p3 = Professors(name="Prof 3", mail="sapnambharadwaj@gmail.com")
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.commit()
    print("Professors created")


    c1 = Courses(department="Department of Computer Science and Engineering", course="B. E. Computer Science and Engineering")
    c2 = Courses(department="Department of Mechanincal Engineering", course="B. E. Mechanical Engineering")
    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()
    print("Department and courses created")


    student1 = Students(
        name="David",
        register_number=40739999,
        username="dd",
        password=bcrypt.generate_password_hash("dd"),
        year_of_graduation=2024,
        mail="sanjeevsaisasank9@gmail.com",
        phone=9384700000,
        gender="M",
        department_course_id=1,
        role="student"
    )
    db.session.add(student1)
    db.session.commit()
    print("Student dd:dd created")


    dean1 = Deans(
        name="Dr. Dean",
        username="dd",
        password=bcrypt.generate_password_hash("dd"),
        mail="sapnambharadwaj@gmail.com",
        phone="9384700000",
        gender="M",
        role="dean"
    )
    db.session.add(dean1)
    db.session.commit()
    print("Dean dd:dd created")


    applicationStatus1 = ApplicationStatus(value="Application successful")
    applicationStatus2 = ApplicationStatus(value="Initial approval from dean successful")
    applicationStatus3 = ApplicationStatus(value="Professors have uploaded their LORs")
    applicationStatus4 = ApplicationStatus(value="Final approval successful")
    applicationStatus5 = ApplicationStatus(value="LOR obtained successfully")
    db.session.add(applicationStatus1)
    db.session.add(applicationStatus2)
    db.session.add(applicationStatus3)
    db.session.add(applicationStatus4)
    db.session.add(applicationStatus5)
    db.session.commit()
    print("Application statuses created")


    if len(sys.argv) > 1 and sys.argv[1] == "-a":
        new_application = Applications(
            application_date = datetime.datetime.today(),
            expiry_date = datetime.datetime.today() + datetime.timedelta(days=30),
            cgpa = 9,
            backlog = 0,
            applied_university = "UCLA",
            applied_country = "USA",
            applied_course = "MS Computer Science",
            doc_1 = None,
            doc_2 = None,
            doc_3 = None,
            prof_1 = 1,
            prof_2 = 2,
            prof_3 = 3,
            status_id = 1,
            student_id = student1.id
        )
        db.session.add(new_application)
        db.session.commit()
        print("Application created")


