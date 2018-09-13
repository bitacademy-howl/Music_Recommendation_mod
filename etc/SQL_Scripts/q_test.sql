###################################################################################################
# ORM 테스트 중....
select * from child;
select * from child LIMIT 100, 100;
select * from parent;

drop table child, parent;

delete from parent where id = 1515;
delete from child where id = 3;
select count(*) from child;
###################################################################################################

###################################################################################################
# Alter & Del test
alter table music add constraint fk_Album_ID foreign key (Album_ID) references album (Album_ID) ON DELETE CASCADE;
alter table music drop column Album_ID;
delete from album where Album_ID = 280967;
###################################################################################################

###################################################################################################
# Join Test
SELECT *
FROM music
JOIN album
ON music.Album_ID = album.Album_ID;
###################################################################################################