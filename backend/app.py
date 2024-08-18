from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import db 
from application import application_bp

app = Flask(__name__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property.db' # change 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'We are winners'
app.register_blueprint(application_bp)

jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app=app, db=db)
bcrypt = Bcrypt()
bcrypt.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)