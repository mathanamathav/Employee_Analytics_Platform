from flask import Flask, render_template ,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models import Employee

app = Flask(__name__)
app.config['SECRET_KEY'] = 'root'
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/employee_db'
db = SQLAlchemy(app)

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
