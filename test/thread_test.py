import threading
from time import sleep
from sqlalchemy import desc

from db_accessing.VO import Artist_VO, Album_VO, Music_VO
from modules.collection import collecting_track, collecting_album, collecting_artist
t1 = threading.Thread(target=collecting_artist, args=[Artist_VO.query.order_by(desc("Artist_ID")).first().Artist_ID])
t2 = threading.Thread(target=collecting_album, args=[Album_VO.query.order_by(desc("Album_ID")).first().Album_ID])
t3 = threading.Thread(target=collecting_track, args=[Music_VO.query.order_by(desc("Music_ID")).first().Music_ID])

while(True):
    if not t1.is_alive():
        t1.start()
    if not t2.is_alive():
        t2.start()
    if not t3.is_alive():
        t3.start()

    sleep(10)