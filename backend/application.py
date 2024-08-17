from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from models import db, StudentApplication  # Replace with your actual file names
from flask import Blueprint

application_bp = Blueprint('application_bp', __name__, url_prefix='/application')
application_api = Api(application_bp)

class StudentApplicationResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('first_name', type=str, required=True, help="First name is required")
        parser.add_argument('middle_name', type=str, required=True, help="Middle name is required")
        parser.add_argument('surname', type=str, required=True, help="Surname is required")
        parser.add_argument('dob', type=str, required=True, help="Date of birth is required")
        parser.add_argument('gender', type=str, required=True, help="Gender is required")
        parser.add_argument('current_class', type=str, required=True, help="Current class is required")
        parser.add_argument('admission_class', type=str, required=True, help="Admission class is required")
        parser.add_argument('residence_name', type=str, required=True, help="Residence name is required")
        parser.add_argument('current_school', type=str, required=True, help="Current school is required")
        parser.add_argument('nationality', type=str, required=True, help="Nationality is required")
        parser.add_argument('phone_number', type=str, required=True, help="Phone number is required")
        parser.add_argument('alternative_number', type=str, required=True, help="Alternative number is required")
        parser.add_argument('email', type=str, required=True, help="Email is required")
        parser.add_argument('sibling', type=bool, required=True, help="Sibling info is required")
        parser.add_argument('sibling_num', type=int, required=True, help="Number of siblings is required")
        parser.add_argument('parent_names', type=str, required=True, help="Parent names are required")
        parser.add_argument('parent_', type=int, required=True, help="Parent information is required")

        args = parser.parse_args()

        student_application = StudentApplication(
            first_name=args['first_name'],
            middle_name=args['middle_name'],
            surname=args['surname'],
            dob=args['dob'],
            gender=args['gender'],
            current_class=args['current_class'],
            admission_class=args['admission_class'],
            residence_name=args['residence_name'],
            current_school=args['current_school'],
            nationality=args['nationality'],
            phone_number=args['phone_number'],
            alternative_number=args['alternative_number'],
            email=args['email'],
            sibling=args['sibling'],
            sibling_num=args['sibling_num'],
            parent_names=args['parent_names'],
            parent_=args['parent_'],
            status='pending') 

        db.session.add(student_application)
        db.session.commit()

        return {"message": "Student application created successfully"}, 201

# Add the resource to the API
application_api.add_resource(StudentApplicationResource, '/student_applications')

class PendingApplicationsResource(Resource):
    def get(self):
        pending_applications = StudentApplication.query.filter_by(status='pending').all()
        applications_list = [
            {
                'id': app.id,
                'first_name': app.first_name,
                'middle_name': app.middle_name,
                'surname': app.surname,
                'dob': app.dob.isoformat(),
                'gender': app.gender,
                'current_class': app.current_class,
                'admission_class': app.admission_class,
                'residence_name': app.residence_name,
                'current_school': app.current_school,
                'nationality': app.nationality,
                'phone_number': app.phone_number,
                'alternative_number': app.alternative_number,
                'email': app.email,
                'sibling': app.sibling,
                'sibling_num': app.sibling_num,
                'parent_names': app.parent_names,
                'parent_': app.parent_,
                'status': app.status,
                'registered_student_id': app.registered_student_id
            }
            for app in pending_applications
        ]
        return applications_list, 200

application_api.add_resource(PendingApplicationsResource, '/applications/pending')
