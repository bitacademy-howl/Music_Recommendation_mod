from builtins import list
from locale import str

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Table
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm import relationship, backref

from db_accessing import Base

class Artist_VO(Base):
    __tablename__ = 'Artist_table'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Artist_ID = Column(Integer, primary_key=True, unique=True)
    Artist_Name = Column(String(100))
    Gender = Column(String(10))
    Group = Column(Boolean)

    # 아래에서 계속 사용할 링크문자열은 그냥 단순히 해당 객체를 통해 /VO.__tablename__/VO.ID 로 얻어낼 수 있지만,
    # DB 테이블 명을 그대로 외부에 노출시켜야 할 이유는 없기때문에, 이렇게 사용하도록 하였다.
    # 물론 비교를 통해 if __tablename__ == 'Artist':
    #                                    '/aasdfasdf/VO.ID' 등으로 해도 무방하다.
    # 해당 노드를 사용할 때마다 프로세서가 돌지,
    # DB 용량을 점유하여 프로세서 사용을 줄일지의 문제인듯.
    # 해당 아티스트의 링크 문자열 (node) - urlMaker의 direct_node_connect() 의 인자로 활용가능
    Artist_Node = Column(String(50))

    # Relations
    # Albums = relationship("Album_VO", back_populates='Singer')
    # Participation = relationship("Music_VO", back_populates='Staff')
    # Write = relationship("Music_VO", back_populates='Lyricists')

    def __repr__(self):
        return "< {0} " \
               "(Artist_ID : {1}, " \
               "Artist_Name : {2}, " \
               "Gender : {3}, " \
               "Group : {4}, " \
               "Artist_Node : {5})>".format(self.__tablename__, self.Artist_ID, self.Artist_Name, self.Gender, self.Group, self.Artist_Node)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Album_VO(Base):
    __tablename__ = 'Album_table'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Album_ID = Column(Integer, primary_key=True, unique=True)
    Album_Title = Column(String(500))

    Agency = Column(String(500))
    Distributor = Column(String(500))
    Description = Column(String(20000))
    Release_Date = Column(DateTime)

    # 해당 앨범의 링크 문자열 (node) - urlMaker의 direct_node_connect() 의 인자로 활용가능
    Album_Node = Column(String(50))

    # FK
    # Singer_ID = Column(Integer, ForeignKey('Artist_table.Artist_ID', ondelete='CASCADE', name='Singer_FK'))
    # Singer_ID = Column(Integer, ForeignKey('Artist_table.Artist_ID', name='Singer_FK'))
    Singer_ID = Column(Integer)

    # Relations
    # Singer = relationship("Artist_VO", back_populates='Albums')
    # Musics = relationship("Music_VO", back_populates='Album')
    # Musics = relationship("Music_VO", back_populates='Album')

    def __init__(self):
        pass

    def __repr__(self):
        return "< {0} >\n" \
               "(Album_ID : {1}\n" \
               "Album_Title : {2}\n" \
               "Agency : {3}\n" \
               "Distributor : {4}\n" \
               "Release_Date: {5}\n" \
               "Singer_ID : {6}\n" \
               "Album_Node : {7})>".format(self.__tablename__, self.Album_ID, self.Album_Title, self.Agency, self.Distributor, self.Release_Date, self.Singer_ID, self.Album_Node)
               # "Album_Node : {7}\n""Musics : {8})>".format(self.__tablename__, self.Album_ID, self.Album_Title, self.Agency, self.Distributor, str(self.Release_Date), self.Singer_ID, self.Album_Node, self.Musics)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

class Music_VO(Base):
    __tablename__ = 'Music_table'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Music_ID = Column(Integer, primary_key=True, unique=True)       # PK
    Music_Title = Column(String(500))                                # 제목
    Genre = Column(String(500))                                       # 장르

    # 기타 속성들...
    Hash_Tags = Column(String(500), nullable=True)                  # 앨범 설명으로 추출
    Lyrics = Column(String(20000), nullable=True)                    # 태그 내 가사 쑤셔넣을 것!

    # 해당 음원의 링크 문자열 (node) - urlMaker의 direct_node_connect() 의 인자로 활용가능
    Music_Node = Column(String(50))

    # FK
    # 음원이 속한 앨범 - 앨범 테이블에는 Artist(singer), 소속사, 유통사 정보 포함
    # Album_ID = Column(Integer, ForeignKey('Album_table.Album_ID', ondelete='CASCADE', name='Album_FK'))
    # Composer_ID = Column(Integer, ForeignKey("Artist_table.Artist_ID", name='Composer_ID_FK')) # 작곡가
    # Lyricist_ID = Column(Integer, ForeignKey("Artist_table.Artist_ID", name='Lyricist_ID_FK')) # 작사가
    Album_ID = Column(Integer)
    Composer_ID = Column(String(100)) # 작곡가
    Lyricist_ID = Column(String(100)) # 작사가

    # Relations
    # Album = relationship("Album_VO", back_populates='Musics')
    # Staff = relationship("Artist_VO", back_populates="Participation", foreign_keys=[Composer_ID, Lyricist_ID])
    # Lyricists = relationship("Artist_VO", back_populates="Write", foreign_keys=[Lyricist_ID])

    def __init__(self):
        pass

    def __repr__(self):
        return "< {0} (Music_ID : {1}, \n" \
               "Music_Title : {2}, \n" \
               "Genre : {3}, \n" \
               "Music_Node : {4}, \n" \
               "Album : {5}, \n" \
               "Composers : {6}, \n" \
               "Lyricist : {7})>".format(self.__tablename__, self.Music_ID, self.Music_Title, self.Genre,
                                         self.Music_Node, self.Album_ID, self.Composer_ID, self.Lyricist_ID)
               # ")>".format(self.__tablename__, self.Music_ID, self.Music_Title, self.Genre, self.Music_Node, self.Album, self.Composers)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


########################################################################################################################
# VO_Examples 1:
# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True, unique=True)
#     children = relationship("Child")
#
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True, unique=True)
#     parent_id = Column(Integer, ForeignKey('parent.id', ondelete='CASCADE'))
########################################################################################################################



class Album_recommend_VO(Base):
    __tablename__ = 'Album_recommend_table'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}


    # Album_ID = Column(Integer, ForeignKey("Album_Table.Album_ID"), primary_key=True, unique=True)
    # rl1 = Column(Integer, ForeignKey("Album_Table.Album_ID"))
    # rl1_sim = Column(Integer)
    # rl2 = Column(Integer, ForeignKey("Album_Table.Album_ID"))
    # rl2_sim = Column(Integer)
    # rl3 = Column(Integer, ForeignKey("Album_Table.Album_ID"))
    # rl3_sim = Column(Integer)
    Album_ID = Column(Integer, ForeignKey('Album_table.Album_ID'), primary_key = True, unique = True)
    rl1 = Column(Integer)
    rl1_sim = Column(DOUBLE)
    rl2 = Column(Integer)
    rl2_sim = Column(DOUBLE)
    rl3 = Column(Integer)
    rl3_sim = Column(DOUBLE)


    def __repr__(self):
        return "< {0} (Album_ID : {1}, \n" \
               "rl1 : {2}, \n" \
               "rl1_sim : {3}, \n" \
               "rl2 : {4}, \n" \
               "rl2_sim : {5}, \n" \
               "rl3 : {6}, \n" \
               "rl3_sim : {7})>".format(self.Album_ID, self.rl1, self.rl1_sim, self.rl2, self.rl2_sim, self.rl3, self.rl3_sim)

    def set_values(self, values):
        if isinstance(values, list):
            if len(values) >= 3:
                self.rl3 = values[len(values)+1]
                self.rl2 = values[len(values)]
                self.rl1 = values[len(values)-1]
            elif len(values) == 2:
                self.rl2 = values[len(values) + 1]
                self.rl1 = values[len(values)]
            elif len(values):
                self.rl1 = values[len(values) + 1]


    def set_keys(self, keys):
        if isinstance(keys, list):
            if len(keys) >= 3:
                self.rl3_sim = keys[len(keys)+1]
                self.rl2_sim = keys[len(keys)]
                self.rl1_sim = keys[len(keys)-1]
            elif len(keys) == 2:
                self.rl2_sim = keys[len(keys) + 1]
                self.rl1_sim = keys[len(keys)]
            elif len(keys):
                self.rl1_sim = keys[len(keys) + 1]

    def set_dict(self, map):
        if isinstance(map, dict):
            self.set_keys(map.keys())
            self.set_values(map.values())

########################################################################################################################
    # 이 부분이랑 위 set keys, values 는 개선 가능할 듯...ㅠ
    def as_dict(self):
        keys = self.as_keys()
        values = self.as_values()

        res_dict = dict()
        res_list = list()

        for i in range(len(keys)):
            if keys[i] is not None:
                res_list.append((keys[i], values[i]))

        return res_dict.update(res_list)
########################################################################################################################
        # return {x.name: getattr(self, x.name) for x in self.__table__.columns}
        #

        # result_dict = dict()
        # for key in keys:

        # return dict([(self.rl1, self.rl1_sim), (self.rl2, self.rl2_sim), (self.rl3, self.rl3_sim)])

    def as_keys(self):
        return [self.rl1, self.rl2, self.rl3]

    def as_values(self):
        return [self.rl1_sim, self.rl2_sim, self.rl3_sim]

#######################################################################################################################
# VO_Examples 2:
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True, unique=True)
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True, unique=True)
    # parent_id = Column(Integer)
    parent_id = Column(Integer, ForeignKey('parent.id', ondelete='CASCADE'))
    parent = relationship("Parent", back_populates="children")
#######################################################################################################################