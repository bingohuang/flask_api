from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = \
    'mysql+pymysql://flask:flask-2024@rm-bp1c94s9654848q1mno.mysql.rds.aliyuncs.com/restful_db'
db = SQLAlchemy(app)


from resources import student_resource
from resources import book_resource