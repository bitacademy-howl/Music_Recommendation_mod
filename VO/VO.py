from sqlalchemy import Column, Integer, String, Boolean, Date
from VO import db
from datetime import datetime

class Music_VO(db.Model):
    __tablename__ = 'Music'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Music_ID = Column(Integer, primary_key=True, unique=True)
    Title = Column(String)

    ########### 나눠야 할 부분 #############################
    Singer = Column(Integer)
    Album = Column(String)
    ########################################################

    # 기타 속성들...
    Genre = Column(String)
    Composer = Column(String)
    Lyricist = Column(String)
    Hash_Tags = Column(String, nullable=True)
    Release_Date = Column(Date)

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

    def __init__(self, Singer, Title, Album):
        self.Singer = Singer
        self.Title = Title
        self.Album = Album

    def __repr__(self):
        return "<Music('%s', '%s', '%s')>" % (self.Title, self.Album, self.Singer)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}