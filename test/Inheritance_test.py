from flask_sqlalchemy import Model
from sqlalchemy import Column

# from VO import db

# class Music_VO(db.Model):
#     Music_ID = Column(db.Integer, primary_key=True, unique=True)
#     Title = Column(db.String(100))
#     Singer = Column(db.String(100))
#     Album = Column(db.String(100))
#
#     def __init__(self):
#         pass
#
#     def __repr__(self):
#         return "<Music('%s')>" % str(self.as_dict)
#
#     def as_dict(self):
#         return {x.name: getattr(self, x.name) for x in self.__table__.columns}
from VO import Music_VO

mv = Music_VO.query.filter_by(Singer="김건모").all()
print(mv, type(mv))

print(mv[0], type(mv[0]))

def innerF(mv):
    attr = mv[0].get_Attr()