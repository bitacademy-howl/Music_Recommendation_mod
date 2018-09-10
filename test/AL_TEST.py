# from sqlalchemy import create_engine, Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
#
# engine = create_engine('mysql+pymysql://root:stark1234@localhost/webdb?charset=utf8', echo=True)
# Base = declarative_base()
# Base.metadata.create_all(engine)
#
# class Artist_VO(Base):
#     __tablename__ = 'Artist'
#     __table_args__ = {'mysql_collate': 'utf8_general_ci'}
#
#     Artist_ID = Column(Integer, primary_key=True, unique=True)
#     Artist_Name = Column(String(100))
#     Gender = Column(String(10))
#     Group = Column(Boolean)
#
#     def __repr__(self):
#         return "< %s ('%d', '%s', '%s', '%b')>" % (self.__tablename__, self.Artist_ID, self.Gender, self.Group)
#
#     def as_dict(self):
#         return {x.name: getattr(self, x.name) for x in self.__table__.columns}
#
# print(Artist_VO.__table__)
# print(Artist_VO.__mapper__)
#
# Artist_VO.metadata.create_all(engine)