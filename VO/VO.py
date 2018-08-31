from sqlalchemy import Column
from VO import db
from datetime import datetime

class Music_VO(db.Model):
    __tablename__ = 'Music'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Music_ID = Column(db.Integer, primary_key=True, unique=True)
    Title = Column(db.String(50))

    ########### 나눠야 할 부분 #############################
    Singer = Column(db.String(50))
    Album = Column(db.String(50))
    ########################################################

    # 기타 속성들...
    Genre = Column(db.String(50))
    Composer = Column(db.String(30))
    Lyricist = Column(db.String(30))
    Hash_Tags = Column(db.String(200), nullable=True)
    Release_Date = Column(db.DateTime)

    # # Album Table
    # FK_Album_ID = Column(Integer)
    # Album = Column(String)
    #
    # # Singer Table
    # FK_Singer_ID = Column(Integer)
    # Singer = Column(Integer)
    # IsGroup = Column(Boolean)

    def __init__(self):
        pass

    # def __init__(self, Singer, Title, Album):
    #     self.Singer = Singer
    #     self.Title = Title
    #     self.Album = Album

    def __repr__(self):
        return "<Music('%s', '%s', '%s')>" % (self.Title, self.Album, self.Singer)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class test_VO(db.Model):
    __tablename__ = 'Test'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Music_ID = Column(db.Integer, unique=True)
    Title = Column(db.String(50), primary_key=True)

    ########### 나눠야 할 부분 #############################
    Singer = Column(db.String(50), primary_key=True)
    Album = Column(db.String(50), primary_key=True)
    ########################################################

    def __init__(self):
        pass

    def __repr__(self):
        return "<Music('%s', '%s', '%s')>" % (self.Title, self.Album, self.Singer)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}