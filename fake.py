from datetime import datetime, timedelta
from random import randint, choice
from faker import Faker
from app import db, app
from app.models import Students, Applications, Courses

fake = Faker()

# Add your departments and courses
with app.app_context():
    departments_and_courses = [
        {"department": "Computer Science", "course": "B.Tech"},
        {"department": "Electrical Engineering", "course": "M.Tech"},
        # Add more as needed
    ]

    for dept_course in departments_and_courses:
        course = Courses(department=dept_course["department"], course=dept_course["course"])
        db.session.add(course)

    db.session.commit()

    # Create 50 applications
    for _ in range(50):
        # Create a fake student
        student = Students(
            name=fake.name(),
            username=fake.user_name(),
            year_of_graduation=randint(2023, 2025),
            register_number=randint(10000, 99999),
            password=fake.password(),
            mail=fake.email(),
            phone=fake.phone_number(),
            gender=choice(["Male", "Female"]),
            role="student",
            is_logged_in=False,
            department_course_id=randint(1, len(departments_and_courses)),
        )

        db.session.add(student)
        db.session.commit()

        # Create a fake application
        application = Applications(
            application_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=randint(30, 90)),
            cgpa=randint(1, 10),
            backlog=0,
            applied_university=fake.company(),
            applied_country=fake.country(),
            applied_course=fake.job(),
            doc_1=fake.file_name(),
            doc_2=fake.file_name(),
            doc_3=fake.file_name(),
            prof_1=randint(1, 5),
            prof_2=randint(1, 5),
            prof_3=randint(1, 5),
            student_id=student.id,
            status_id=1,
        )

        db.session.add(application)
        db.session.commit()

print("50 applications created successfully!")
