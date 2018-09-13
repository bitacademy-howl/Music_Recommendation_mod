desc parent;
desc child;

select * from parent;
select * from child;



ALTER TABLE child DROP FOREIGN KEY child_ibfk_1;
ALTER TABLE child ADD CONSTRAINT child_ibfk_1 FOREIGN KEY(parent_id) REFERENCES parent(id);

insert INTO parent (id) values (3030);
delete from parent where id = 3030;


select * from information_schema.table_constraints where table_name = 'parent';
select * from information_schema.table_constraints where table_name = 'child';

drop table parent, child;
drop table parent;
