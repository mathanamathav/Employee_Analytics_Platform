# Employee Platform Imports
from flask import Flask, render_template, jsonify
from db import app
import requests

EMPLOYEE_DATA_PLATFORM_LINK = 'https://emp-data-app.azurewebsites.net/api/fetchall'


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/gender_status', methods=['GET'])
def gender_status():
    
    req_data = requests.get(EMPLOYEE_DATA_PLATFORM_LINK)
    if req_data.status_code != 200:
        return jsonify({'Error message': 'Employee Data platform is not currently online'})
    req_data = req_data.json()

    result_data = {}
    for data in req_data:
        if data['gender'] in result_data:
            result_data[data['gender']] += 1
        else:
            result_data[data['gender']] = 1
    return jsonify(result_data)


@app.route('/department/count', methods=['GET'])
def department_counts():

    req_data = requests.get(EMPLOYEE_DATA_PLATFORM_LINK)
    if req_data.status_code != 200:
        return jsonify({'Error message': 'Employee Data platform is not currently online'})
    req_data = req_data.json()

    result_data = {}
    for data in req_data:
        if data['department_name'] in result_data:
            result_data[data['department_name']] += 1
        else:
            result_data[data['department_name']] = 1
    return jsonify(result_data)


@app.route('/department/minmaxsalary', methods=['GET'])
def get_minmax_salary():

    req_data = requests.get(EMPLOYEE_DATA_PLATFORM_LINK)
    if req_data.status_code != 200:
        return jsonify({'Error message': 'Employee Data platform is not currently online'})
    req_data = req_data.json()

    result_data = {}
    for data in req_data:
        if data['department_name'] in result_data:
            result_data[data['department_name']].append(
                data['employee_salary'])
        else:
            result_data[data['department_name']] = [data['employee_salary']]

    for data in result_data:
        if len(result_data[data]) == 1:
            result_data[data] = {'min': result_data[data]
                                 [0], 'max': result_data[data][0]}
        else:
            max_sal, min_sal = max(result_data[data]), min(result_data[data])
            result_data[data] = {'min': min_sal, 'max': max_sal}

    return jsonify(result_data)


@app.route('/demographic/city', methods=['GET'])
def city_count():
    
    req_data = requests.get(EMPLOYEE_DATA_PLATFORM_LINK)
    if req_data.status_code != 200:
        return jsonify({'Error message': 'Employee Data platform is not currently online'})
    req_data = req_data.json()

    result_data = {}
    for data in req_data:
        if data['city'] in result_data:
            result_data[data['city']] += 1
        else:
            result_data[data['city']] = 1
    return jsonify(result_data)


@app.route('/demographic/state', methods=['GET'])
def state_count():

    req_data = requests.get(EMPLOYEE_DATA_PLATFORM_LINK)
    if req_data.status_code != 200:
        return jsonify({'Error message': 'Employee Data platform is not currently online'})
    req_data = req_data.json()
    
    result_data = {}
    for data in req_data:
        if data['state'] in result_data:
            result_data[data['state']] += 1
        else:
            result_data[data['state']] = 1
    return jsonify(result_data)


@app.route('/demographic/country', methods=['GET'])
def country_count():
    
    req_data = requests.get(EMPLOYEE_DATA_PLATFORM_LINK)
    if req_data.status_code != 200:
        return jsonify({'Error message': 'Employee Data platform is not currently online'})
    req_data = req_data.json()
    
    result_data = {}
    for data in req_data:
        if data['country'] in result_data:
            result_data[data['country']] += 1
        else:
            result_data[data['country']] = 1
    return jsonify(result_data)


if __name__ == '__main__':
    app.run(debug=True)
