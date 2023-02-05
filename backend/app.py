#Employee Platform Imports
from flask import Flask, render_template ,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime

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

def Convert(tup, di):
    for a, b,c in tup:
        di.setdefault(a, []).extend([b,c])
    return di

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


@app.route('/department/count',methods = ['GET'])
def get_department_counts():
    department_counts = db.session.query(Department.dept_name, func.count(Employee.id).label('employee_count')) \
        .join(Employee, Employee.dept_id == Department.id) \
        .group_by(Department.id) \
        .all()
    result={}
    for data in department_counts:
        department , count = data
        result[department] = count
    return jsonify(result)

@app.route('/department/minmaxsalary',methods = ['GET'])
def get_minmax_salary():
    department_salary = db.session.query(Department.dept_name, func.min(Employee.salary).label('min_salary'),
                                        func.max(Employee.salary).label('max_salary')) \
        .join(Employee, Employee.dept_id == Department.id) \
        .group_by(Department.id) \
        .all()
    result= {}
    return jsonify(Convert(department_salary, result))
    

@app.route('/demographic/city',methods = ['GET'])
def city_count():
    
    city_count = db.session.query(Employee.city,func.count(Employee.city)).group_by(Employee.city).all()
    result = {}
    for data in city_count:
        city , count = data
        result[city] = count
    return jsonify(result)

@app.route('/demographic/state',methods = ['GET'])
def state_count():
    state_count = db.session.query(Employee.state,func.count(Employee.state)).group_by(Employee.state).all()
    result = {}
    for data in state_count:
        state , count = data
        result[state] = count
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
