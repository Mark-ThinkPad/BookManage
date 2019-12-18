use Library
select * from TB_Reader
select * from TB_ReaderType
select * from TB_Book
select * from TB_Borrow
insert into TB_Book (bkName) values ('test')
delete from TB_Borrow
dbcc checkident (TB_Book, reseed, 0)
drop table TB_Borrow