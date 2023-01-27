#Employee Platform Imports
from flask import Flask, render_template ,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime
from models import Employee

app = Flask(__name__)
app.config['SECRET_KEY'] = 'root'
#SqlAlchemy Database Configuration With Mysql #update the local user name and password and database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/employee_db'
db = SQLAlchemy(app)

#our model
class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(100))
    age =  db.Column(db.Integer)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    role = db.Column(db.String(100))
    email = db.Column(db.String(100))
    gender= db.Column(db.String(100))
    dept_id = db.Column(db.Integer,db.ForeignKey('department.id'))
    salary = db.Column(db.Float)
    hire_date = db.Column(db.DateTime(), default=datetime.now)
    experience =  db.Column(db.Integer)

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key = True)

    dept_name = db.Column(db.String(100))
    employee_id = db.Column(db.Integer,db.ForeignKey('employee.id'))
    

class TimeOff(db.Model):
    __tablename__ = 'time_off'
    id = db.Column(db.Integer, primary_key = True)

    start_date = db.Column(db.DateTime(), default=datetime.now)
    end_date = db.Column(db.DateTime())
    leave_type = db.Column(db.String(100))
    reason = db.Column(db.String(100))
    approval_status = db.Column(db.String(100))
    approver_id =  db.Column(db.Integer,db.ForeignKey('employee.id'))
    employee_id = db.Column(db.Integer,db.ForeignKey('employee.id'))

# two decorators, same function sample function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

# This endpoint gives classification of gender with their count in our company
@app.route('/gender_status',methods = ['GET'])
def symbol():
    gender_count = db.session.query(Employee.gender,func.count(Employee.gender)).group_by(Employee.gender).all()
    result = {}
    for data in gender_count:
        gender , count = data
        result[gender] = count
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
