from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = \
    'mysql+pymysql://flask:flask-2024@8.136.89.212/restful_db'
db = SQLAlchemy(app)


from resources import student_resource
from resources import book_resource