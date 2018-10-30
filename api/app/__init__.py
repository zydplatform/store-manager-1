
from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'am a secret key'

jwt = JWTManager(app)
