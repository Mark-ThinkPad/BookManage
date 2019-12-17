use Library
select * from TB_Reader
select * from TB_ReaderType
select * from TB_Book
insert into TB_Book (bkName) values ('test')
delete from TB_Book
dbcc checkident (TB_Book, reseed, 0)