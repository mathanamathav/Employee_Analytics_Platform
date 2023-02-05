from datetime import datetime
from db import db


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    company_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    role = db.Column(db.String(100))
    email = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    dept_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    salary = db.Column(db.Float)
    hire_date = db.Column(db.DateTime(), default=datetime.now)
    experience = db.Column(db.Integer)


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)

    dept_name = db.Column(db.String(100))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))


class TimeOff(db.Model):
    __tablename__ = 'time_off'
    id = db.Column(db.Integer, primary_key=True)

    start_date = db.Column(db.DateTime(), default=datetime.now)
    end_date = db.Column(db.DateTime())
    leave_type = db.Column(db.String(100))
    reason = db.Column(db.String(100))
    approval_status = db.Column(db.String(100))
    approver_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
