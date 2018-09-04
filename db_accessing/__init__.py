from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:stark1234@localhost/webdb?charset=utf8'

# transection 에 대한 응답
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'stark'

db = SQLAlchemy(app, session_options={"autoflush": False, "autocommit" : False,})

from db_accessing.VO import *

db.create_all()