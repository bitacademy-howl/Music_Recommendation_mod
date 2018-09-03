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
#
# print(mv[0], type(mv[0]))
#
def innerF(mv):
    attr = mv[0].as_dict()
    return attr
#
attr = innerF(mv=mv)
print(attr)

dict1 = {'Music_ID': 24357, 'Title': '농사꾼', 'Singer': '김건모내기', 'Album': '밭갈기', 'Genre': None, 'Composer': None, 'Lyricist': None, 'Hash_Tags': None, 'Release_Date': None}
#
dict12 = {'Music_ID': '24357', 'Title': '농사꾼', 'Singer': '김건모내기'}
# print(dict1, type(dict1))

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)

d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}

x = obj(d)
print(x.a, x.b, x.b.c, x.d)
x.b.c
x.d[1].foo


# def print_param2(**kwargs):
#     print(kwargs)
#     # print(kwargs.keys())
#     # print(kwargs.values())
#     first = kwargs.items()
#
#     for name, value in kwargs.items():
#         print("%s : %s" % (name, value))
#
#
# aa = print_param2(first='a', second='b', third='c', fourth='d')

