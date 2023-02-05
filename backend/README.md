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
- [ ] Add more


>Sample API Response Preview for Gender Classification
![Screenshot_20230126_102319](https://user-images.githubusercontent.com/62739618/214899280-c5a8603b-c451-4b1f-8c4d-e77f055ffc02.png)


## Requirments 
To do download table plus to view tables in your local machine. [link](https://tableplus.com/windows)
