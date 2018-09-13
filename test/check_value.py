from db_accessing.VO import Album_VO

x = Album_VO.query.filter_by(Album_ID=266).all()

print(x[0].Description)