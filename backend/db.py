# Employee Platform Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:password@localhost/employee_db'
db = SQLAlchemy(app)

def create_db_with_tables():
    db.create_all()

def delete_all_tables_in_db():
    #DELETES ALL TABLES
    with db.engine.connect() as conn:
        conn.execute("SET FOREIGN_KEY_CHECKS=0")
        conn.execute("DROP DATABASE employee_db;")
        conn.execute("CREATE DATABASE employee_db;")
        conn.execute("SET FOREIGN_KEY_CHECKS=1")