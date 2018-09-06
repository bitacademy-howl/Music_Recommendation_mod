from sqlalchemy import Column, ForeignKey

from db_accessing import db

# class Artist_VO(db.Model):
#     __tablename__ = 'test_Artist'
#     __table_args__ = {'mysql_collate': 'utf8_general_ci'}
#
#     Artist_ID = Column(db.Integer, primary_key=True, unique=True)
#     Artist_Name = Column(db.String(100))
#
#     def __repr__(self):
#         return "< %s ('%d', '%s', '%s', '%b')>" % (self.__tablename__, self.Artist_ID, self.Gender, self.Group)
#
#     def as_dict(self):
#         return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Album_VO(db.Model):
    __tablename__ = 'test_Album'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Album_ID = Column(db.Integer, primary_key=True, unique=True)
    Album_Title = Column(db.String(100))

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Music_VO(db.Model):
    __tablename__ = 'test_Music'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Music_ID = Column(db.Integer, primary_key=True, unique=True)       # PK
    Music_Title = Column(db.String(100))                                # 제목

    # FK
    # 음원이 속한 앨범 - 앨범 테이블에는 Artist(singer), 소속사, 유통사 정보 포함
    Album_ID = Column(db.Integer, ForeignKey('test_Album.Album_ID'))

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}