from sqlalchemy import Column, String

import db_accessing
from db_accessing.VO import Music_VO


########################################################################################################################
print(Music_VO.Music_Title.type.length)
print(Music_VO.Lyrics.type.length, type(Music_VO.Lyrics.type.length))

print(Music_VO.Lyrics.type.__class__.__name__)

# Lyrics 라는 변수는 Column() 생성자에 의해 생성된 객체이고,
# 이 클래스는 String() 생성자에 의한 객체를 type이라는 변수명으로 멤버로 포함
# 해당 컬럼의 type을 지정한 이름을 얻어올때는 type.__class__.__name__ 사용하면 됨...굳
########################################################################################################################


class cla:
    a = Column(String(1000))
    b = String(100)

print(cla.b.__class__.__name__, type(cla.b))

print(Music_VO.Lyrics.__class__.__name__)
print(cla.a.__class__.__name__)

print(isinstance(cla.a, Column))

mVO = Music_VO()
print(mVO.__class__.__name__)