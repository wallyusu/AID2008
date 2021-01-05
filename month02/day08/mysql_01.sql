create function st3(nid int) returns varchar(30)
begin
return (select name from cls where id=nid);
end

create procedure st4()
begin
select name,age from cls;
select * from cls where score > 60;
end