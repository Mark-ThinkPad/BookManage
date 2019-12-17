create database Library
go
use Library
go
create table TB_ReaderType
(
    rdType smallint primary key,
    rdTypeName nvarchar(20) unique not null,
    CanLendQty int,
    CanLendDay int,
    CanContinueTimes int,
    PunishRate float,
    DateValid smallint not null ,
)
go
insert into TB_ReaderType values
(10, '教师', 12, 60, 2, 0.05, 0),
(20, '本科生', 8, 30, 1, 0.05, 4),
(21, '专科生', 8, 30, 1, 0.05, 3),
(30, '硕士研究生', 8, 30, 1, 0.05, 3),
(31, '博士研究生', 8, 30, 1, 0.05, 4)
go
create table TB_Reader
(
    rdID int primary key,
    rdName nvarchar(20),
    rdSex nchar(1) check (rdSex in ('男', '女')),
    rdType smallint not null,
    rdDept nvarchar(20),
    rdPhone nvarchar(25),
    rdEmail nvarchar(25),
    rdDateReg datetime,
    rdPhoto image,
    rdStatus nchar(2) check (rdStatus in ('有效', '挂失', '注销')),
    rdBorrowQty int default 0,
    rdPwd nvarchar(20) default '123',
    rdAdminRoles smallint,
    foreign key (rdType) references TB_ReaderType(rdType),
)
go
create table TB_Book
(
    bkID int primary key identity(1, 1),
    bkCode nvarchar(20),
    bkName nvarchar(50),
    bkAuthor nvarchar(30),
    bkPress nvarchar(50),
    bkDatePress datetime,
    bkISBN nvarchar(15),
    bkCatalog nvarchar(30),
    bkLanguage smallint check (bkLanguage in (0,1,2,3,4,5)),
    bkPages int,
    bkPrice money,
    bkDateIn datetime,
    bkBrief text,
    bkCover image,
    bkStatus nchar(2) check (bkStatus in ('在馆','借出','遗失','变卖','销毁')),
)
go
create table TB_Borrow
(
    BorrowID numeric(12, 0) primary key,
    rdID int,
    bkID int,
    IdContinueTimes int,
    IdDateOut datetime,
    IdDateRetPlan datetime,
    IdDateRetAct datetime,
    IdOverDay int,
    IdOverMoney money,
    IdPunishMoney money,
    IsHasReturn bit default 0,
    OperatorLend nvarchar(20),
    OperatorRet nvarchar(20),
    foreign key (rdID) references TB_Reader(rdID),
    foreign key (bkID) references TB_Book(bkID),
)
go
create login LibAdmin with password = 'qwert123.', default_database = Library
create user LibAdmin for login LibAdmin with default_schema = dbo
exec sp_addrolemember 'db_owner', 'LibAdmin'
go
-- 系统自动生成bkID, 创建after触发器将bkID自动赋给bkCode, 免去人工编码
create trigger IDtoCode on TB_Book for insert
as
    update TB_Book set bkCode=cast(bkID as nvarchar(20)) where bkCode is null
go

