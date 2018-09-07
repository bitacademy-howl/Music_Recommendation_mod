from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:stark1234@localhost/webdb?charset=utf8', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import db_accessing.VO
    Base.metadata.create_all(bind=engine)

init_db()












# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
#
# # app config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:stark1234@localhost/webdb?charset=utf8'
#
# # transection 에 대한 응답
# app.config['SQLALCHEMY_ECHO'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = 'stark'
#
# db = SQLAlchemy(app, session_options={"autoflush": False, "autocommit" : False})
#
# from db_accessing.VO import *
# # from db_accessing.test_VO import *
#
# db.create_all()