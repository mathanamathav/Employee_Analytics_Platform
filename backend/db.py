from flask_sqlalchemy import SQLAlchemy


def initialize_db(app):
    db = SQLAlchemy(app)
    return db