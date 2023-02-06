# Employee Platform Imports
from flask import Flask, render_template, jsonify
from sqlalchemy import func
from models import Employee, TimeOff, Department
from db import app,db
import datetime 

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

@app.route('/employee_count_by_gender/<gender>')
def employee_count_by_gender(gender):
    count = Employee.query.filter_by(gender=gender).count()
    return str(count)

@app.route('/employees_less_than_a_year')
def employees_less_than_a_year():
    current_time = datetime.datetime.now()
    one_year_ago = current_time - datetime.timedelta(days=365)
    employees = Employee.query.filter(TimeOff.start_date >= one_year_ago,
                                      TimeOff.end_date.is_(None) | (TimeOff.end_date >= one_year_ago)).all()
    employee_list = [employee.name for employee in employees]
    return str(employee_list)

@app.route('/employees_above_45')
def employees_above_45():
    employees = Employee.query.filter(Employee.age > 45).all()
    employee_list = [employee.name for employee in employees]
    return str(employee_list)


if __name__ == '__main__':
    app.run(debug=True)
