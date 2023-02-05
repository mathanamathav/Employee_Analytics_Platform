# Employee Platform Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/employee_db'
db = SQLAlchemy(app)
