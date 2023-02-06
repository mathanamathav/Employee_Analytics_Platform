# Employee Platform Imports
from flask import Flask, render_template, jsonify
from sqlalchemy import func
from models import Employee, TimeOff, Department
from db import app,db


def Convert(tup, di):
    for a, b, c in tup:
        di.setdefault(a, []).extend([b, c])
    return di


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/gender_status', methods=['GET'])
def symbol():
    gender_count = db.session.query(Employee.gender, func.count(
        Employee.gender)).group_by(Employee.gender).all()
    result = {}
    for data in gender_count:
        gender, count = data
        result[gender] = count
    return jsonify(result)


@app.route('/department/count', methods=['GET'])
def get_department_counts():
    department_counts = db.session.query(Department.dept_name, func.count(Employee.id).label('employee_count')) \
        .join(Employee, Employee.dept_id == Department.id) \
        .group_by(Department.id) \
        .all()
    result = {}
    for data in department_counts:
        department, count = data
        result[department] = count
    return jsonify(result)


@app.route('/department/minmaxsalary', methods=['GET'])
def get_minmax_salary():
    department_salary = db.session.query(Department.dept_name, func.min(Employee.salary).label('min_salary'),
                                         func.max(Employee.salary).label('max_salary')) \
        .join(Employee, Employee.dept_id == Department.id) \
        .group_by(Department.id) \
        .all()
    result = {}
    return jsonify(Convert(department_salary, result))


@app.route('/demographic/city', methods=['GET'])
def city_count():

    city_count = db.session.query(Employee.city, func.count(
        Employee.city)).group_by(Employee.city).all()
    result = {}
    for data in city_count:
        city, count = data
        result[city] = count
    return jsonify(result)


@app.route('/demographic/state', methods=['GET'])
def state_count():
    state_count = db.session.query(Employee.state, func.count(
        Employee.state)).group_by(Employee.state).all()
    result = {}
    for data in state_count:
        state, count = data
        result[state] = count
    return jsonify(result)

@app.route('/age_preference_recruitment', methods = ['GET'])
def age_pref_recruitment():
    age_pref = db.session.query(Employee.experience, func.count(Employee.id)).group_by(Employee.experience).filter(Employee.experience > 10).filter(Employee.age < 40).all()
    result = {}
    for data in age_pref:
        age, count = data
        result[age] = count
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
