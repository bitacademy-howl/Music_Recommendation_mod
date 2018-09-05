from sqlalchemy import Column, ForeignKey
from db_accessing import db

class Artist_VO(db.Model):
    __tablename__ = 'Artist'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Artist_ID = Column(db.Integer, primary_key=True, unique=True)
    Artist_Name = Column(db.String(100))
    Gender = Column(db.String(10))
    Group = Column(db.Boolean)

    def __repr__(self):
        return "< %s ('%d', '%s', '%s', '%b')>" % (self.__tablename__, self.Artist_ID, self.Gender, self.Group)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Album_VO(db.Model):
    __tablename__ = 'Album'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Album_ID = Column(db.Integer, primary_key=True, unique=True)
    Album_Title = Column(db.String(100))

    Agency = Column(db.String(100))
    Distributor = Column(db.String(100))
    Release_Date = Column(db.DateTime)

    # FK
    Singer_ID = Column(db.Integer, ForeignKey('Artist.Artist_ID'))

    def __init__(self):
        pass

    def __repr__(self):
        return "< %s >\n" \
               "(Album_ID : '%d'\n" \
               "Album_Title : '%s'\n" \
               "Agency : '%s'\n" \
               "Distributor : %s\n" \
               "Release_Date: %s\n" \
               "Singer_ID : %d\n)>" % \
               (self.__tablename__, self.Album_ID, self.Album_Title, self.Agency, self.Distributor, str(self.Release_Date), self.Singer_ID)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Music_VO(db.Model):
    __tablename__ = 'Music'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Music_ID = Column(db.Integer, primary_key=True, unique=True)       # PK
    Music_Title = Column(db.String(100))                                # 제목
    Genre = Column(db.String(50))                                       # 장르

    # 기타 속성들...
    Hash_Tags = Column(db.String(500), nullable=True)                  # 앨범 설명으로 추출
    Lyrics = Column(db.String(2000), nullable=True)                    # 태그 내 가사 쑤셔넣을 것!

    # FK
    # 음원이 속한 앨범 - 앨범 테이블에는 Artist(singer), 소속사, 유통사 정보 포함
    Album_ID = Column(db.Integer, ForeignKey('Album.Album_ID'))
    Composer_ID = Column(db.Integer, ForeignKey("Artist.Artist_ID")) # 작곡가
    Lyricist_ID = Column(db.Integer, ForeignKey("Artist.Artist_ID")) # 작사가

    def __init__(self):
        pass

    def __repr__(self):
        return "< %s ('%s', '%s', '%s')>" % \
               (self.__tablename__, self.Music_Title, self.Genre, self.Album_ID)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}