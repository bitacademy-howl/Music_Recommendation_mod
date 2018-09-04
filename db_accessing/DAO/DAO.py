# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import scoped_session, sessionmaker
#
# import db_accessing
#
# class DAO:
#     engine = create_engine('mysql+pymysql://root:stark1234@localhost/webdb?charset=utf8', convert_unicode=True)
#     metadata = MetaData()
#     db_session = scoped_session(sessionmaker(autocommit=False,
#                                              autoflush=False,
#                                              bind=engine))
#
#     def init_db(self):
#         self.metadata.create_all(bind=self.engine)
#
#     @db_accessing.app.teardown_request
#     def shutdown_session(self, exception=None):
#         self.db_session.remove()


# session 은 커넥션 풀에 있는 connection 을 사용하고,
# 이를 사용한 후에 session.close() 를 통해 connection pool로 반환해 주어야 한다.
# Flask - SQLAlchemy 를 사용하면 이러한 session 의 life-cycle을 관리해준다.