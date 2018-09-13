###################################################################################################
# 호스트 추가 중, db 유저 확인
use mysql;
select host, user, password from user;

grant all privileges on *.* to 'root'@'192.168.1.28' identified by 'stark1234';
flush privileges;

use webdb;
###################################################################################################

###################################################################################################
# 테이블 삭제
drop table music_table, album_table;
###################################################################################################

###################################################################################################
# 제약조건 확인
select * from information_schema.table_constraints where table_name = 'Music_table';
select * from information_schema.table_constraints where table_name = 'album_table';
select * from information_schema.table_constraints where table_name = 'artist_table';
###################################################################################################

###################################################################################################
# Count 함수
SELECT COUNT(*) FROM music_table;
SELECT COUNT(*) FROM album_table;
SELECT COUNT(*) FROM artist_table;
###################################################################################################

SELECT COUNT(*) FROM album_table WHERE album_table.Description is not NULL;
SELECT COUNT(*) FROM album_table WHERE album_table.Description is NULL;

###################################################################################################
SELECT * FROM album_table WHERE album_table.Description is not NULL;

# select 구문
select * from music_table;
select * from album_table;
select * from artist_table order by artist_id desc LIMIT 10000;
select * from album_table order by Album_ID desc LIMIT 10000;
select * from music_table order by Music_ID desc LIMIT 10000;
###################################################################################################

###################################################################################################
# insert
insert INTO artist_table VALUES (10000000, 'Various Artists', '혼성', 0, '/artist/10000000');
###################################################################################################

###################################################################################################
# 컬럼 데이터 타입 변경
desc album_table;

# workbench 에서는 오류 뜨는데 구분 정상실행 됨
ALTER TABLE album_table modify Album_Title VARCHAR(500);
###################################################################################################


# 제약조건들
ALTER TABLE album_table DROP FOREIGN KEY Singer_FK;
ALTER TABLE album_table ADD CONSTRAINT Singer_FK FOREIGN KEY(Singer_ID) REFERENCES artist_table(Artist_ID);
ALTER TABLE album_table ADD CONSTRAINT Singer_FK FOREIGN KEY(Singer_ID) REFERENCES artist_table(Artist_ID) ON DELETE CASCADE;
desc album_table;



# 컬럼 추가
# ALTER TABLE 테이블명 ADD 추가할컬럼명 컬럼타입 DEFAULT 디폴트값;
# ALTER TABLE 테이블명 ADD COLUMN 추가할컬럼명 컬럼타입 DEFAULT 디폴트값 컬럼위치;
# ALTER TABLE user ADD level int DEFAULT 1;
# ALTER TABLE `rank` ADD COLUMN `ranking` INT(10) DEFAULT 0 AFTER `user_id`; //user_id 뒤에추가
# ALTER TABLE `rank` ADD COLUMN `test` INT(10) DEFAULT 1 FIRST; //테이블 맨앞에 추가

# 컬럼 삭제
# ALTER TABLE 테이블명 DROP 컬럼명;
# ALTER TABLE user DROP level;

# 제약조건 확인하기
#  select * from information_schema.table_constraints;

# 제약조건 삭제하기
#  ALTER TABLE [테이블명] DROP CONSTRAINT [제약조건이름];

# 만약 위의 구문으로 Error code 1064: You have an error in your SQL syntax; 가 나왔다면, 
# 외래키 제약조건일 확률이 높다
#  ALTER TABLE [테이블명] DROP FOREIGN KEY [제약조건이름];

# 제약조건 추가하기

# 외래키 :
#  ALTER TABLE [테이블명] ADD CONSTRAINT [제약조건이름] FOREIGN KEY(컬럼명) REFERENCES [부모테이블명](PK컬럼명) [ON DELETE CASCADE / ON UPDATE CASCADE];

# 기본키 : 
#  ALTER TABLE [테이블명] ADD CONSTRAINT [제약조건이름] PRIMARY KEY(컬럼명);

# NOT NULL 제약조건 추가
#  ALTER TABLE [테이블명] MODIFY [컬럼명] [데이터타입] CONSTRAINT [제약조건이름] NOT NULL;
