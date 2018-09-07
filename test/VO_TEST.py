########################################################################################################################
# in VO_Examples 2:
from sqlalchemy.exc import IntegrityError, InvalidRequestError

from db_accessing import db_session
from db_accessing.VO import Parent, Child
# #
p = Parent()  # 여기서는 앨범
p.id = 1515
db_session.merge(p)
db_session.commit()

child = Child()
########################################################################################################################
# !!!!!! 주의 !!!!!
# DB 에 id, 즉 primary key를 0는 넣지 말것!
########################################################################################################################
for i in range(1, 100, 1):
    child.id = i
    child.parent_id = p.id
    child.parent_id = 1515
    db_session.merge(child)

db_session.commit()

parent = Parent.query.filter(Parent.id.like(1515)).first()

for ch in parent.children:
    print(ch.id, ch.parent_id, ch.parent.id)
########################################################################################################################









########################################################################################################################
# # in VO_Examples 1:
# from sqlalchemy.exc import IntegrityError, InvalidRequestError
#
# from db_accessing import db_session
# from db_accessing.VO import Parent, Child
# # #
# p = Parent()  # 여기서는 앨범
# p.id = 1515
# db_session.merge(p)
# db_session.commit()
#
# child = Child()
# # !!!!!! 주의 !!!!!
# # DB 에 id, 즉 primary key를 0는 넣지 말것!
# for i in range(1, 100, 1):
#     child.id = i
#     # child.parent_id = p.id
#     child.parent_id = 1515
#     db_session.merge(child)
#
# db_session.commit()
#
# parent = Parent.query.filter(Parent.id.like(1515)).first()
########################################################################################################################