--1. 查找30多元的图书
select * from book where price>30 and price<40;
--２．查找人民文学出版社出版的图书
select * from book where press='人民文学出版社';
--３．查找鲁迅写的，人民文学出版社出版的图书
select * from book where author='鲁迅' and press='人民文学出版社';
--４．查找备注不为空的图书
select * from book where remark is not null;
--５．查找价格超过６０元的图书，只看书名和价格
select name,price from book where price>60;
--６．查找鲁迅写的或者茅盾写的图书
select * from book where author='鲁迅' or author='三毛';