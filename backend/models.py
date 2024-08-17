from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import datetime
db = SQLAlchemy()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class SubjectTeacher(db.Model):
    __tablename__ = 'subject_teacher'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.BigInteger, nullable=False)
    teacher_id = db.Column(db.BigInteger, nullable=False)

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.BigInteger, nullable=False)
    column_3 = db.Column(db.BigInteger, nullable=False)
    subject_teacher_id = db.Column(db.BigInteger, db.ForeignKey('subject_teacher.id'))

class RegisteredStudent(db.Model):
    __tablename__ = 'registered_students'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    student_application = db.relationship('StudentApplication', backref='registered_student', uselist=False)

class StudentApplication(db.Model):
    __tablename__ = 'student_applications'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    middle_name = db.Column(db.Text, nullable=False)
    surname = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    current_class = db.Column(db.Text, nullable=False)
    admission_class = db.Column(db.Text, nullable=False)
    residence_name = db.Column(db.Text, nullable=False)
    current_school = db.Column(db.Text, nullable=False)
    nationality = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    alternative_number = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    sibling = db.Column(db.Boolean, nullable=False)
    sibling_num = db.Column(db.BigInteger, nullable=False)
    parent_names = db.Column(db.Text, nullable=False)
    parent_ = db.Column(db.BigInteger, nullable=False)
    status = db.Column(db.Text, nullable=True)
    registered_student_id = db.Column(db.BigInteger, db.ForeignKey('registered_students.id'), nullable=True, unique=True)

class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    student_id = db.Column(db.BigInteger, db.ForeignKey('registered_students.id'), nullable=False)
    subject_id = db.Column(db.BigInteger, db.ForeignKey('subjects.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)

class ApplicantSibling(db.Model):
    __tablename__ = 'applicant_siblings'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    grade = db.Column(db.Text, nullable=False)
    application_id = db.Column(db.BigInteger, nullable=False)

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.BigInteger, nullable=False)
    column_3 = db.Column(db.BigInteger, nullable=False)

class SuspendedStudent(db.Model):
    __tablename__ = 'suspended_students'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    class_ = db.Column(db.Text, nullable=False)
    reason = db.Column(db.Text, nullable=False)
    start = db.Column(db.Date, nullable=False)
    end = db.Column(db.Date, nullable=False)
    sus_no = db.Column(db.BigInteger, nullable=False)
    registered_student_id = db.Column(db.BigInteger, db.ForeignKey('registered_students.id'))

