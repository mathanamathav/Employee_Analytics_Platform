# Expose the Employee Analaytics API

>Employee Schema Followed for now - [link](https://docs.google.com/document/d/1ZEMlIfdAfIX5MGkqnLqinR9kjYMhCoAZb6q2wURWrI0/edit)

## SET-UP

**Step 1) Install the python dependencies**

```
cd .\backend\
pip install -r requirements.txt
```

**Step 2) Install MySQL**

creating a user with user name and password - admin and password

```
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

CREATE DATABASE employee_db;
```

Note if MySQL isn't added in environment variables add this path:
```
C:\Program Files\MySQL\MySQL Server 8.0\bin
```
[fix](https://sebhastian.com/mysql-not-recognized-fix/)

**Step 3) Create tables**

```
cd .\backend\
flask shell

>>>from db import create_db_with_tables
>>>create_db_with_tables() 
>>>exit()
```

**Step 4) Dump the values into the tables**

Install tableplus and connect to mysql server 
```
set FOREIGN_KEY_CHECKS=0;
```

Download the dump [link](https://drive.google.com/drive/folders/1tvaCl2A723MBiUxC3QHAAlU9oN-udogq?usp=share_link)

Click the each table and import the sql-dump data

**Step 5) Start the Flask application**
```
cd .\backend\
python app.py
```


## TO-DO - API Endpoints
- [x] Gender classification
- [x] Department count
- [x] Department maximum and minimum salary 
- [x] Demographic city
- [x] Demographic state
- [x] Count gender given gender
- [x] Employees who worked less than a year
- [x] Employees whose age is above 45
- [x] Vacation Time For Each Employee
- [x] Percentage of Freshers and Experienced Employees Company Prefers
- [x] Age Preference Recruitment
- [ ] Add more


>Sample API Response Preview for Gender Classification
![Screenshot_20230126_102319](https://user-images.githubusercontent.com/62739618/214899280-c5a8603b-c451-4b1f-8c4d-e77f055ffc02.png)
![Screenshot_20230206_120807](https://user-images.githubusercontent.com/62739618/216838398-569b383b-1fee-4483-927f-73709b650505.png)
![Screenshot_20230206_120829](https://user-images.githubusercontent.com/62739618/216838406-e7f705b1-493f-4d2f-ace0-2b2fd0e9a41a.png)


## Requirments 
To do download table plus to view tables in your local machine. [link](https://tableplus.com/windows)
