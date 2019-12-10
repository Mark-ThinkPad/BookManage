# coding: utf-8
from sqlalchemy import create_engine, Column, DateTime, Float, ForeignKey, Integer, LargeBinary, Numeric, SmallInteger, \
    Text, Unicode
from sqlalchemy.dialects.mssql.base import BIT, MONEY
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mssql+pymssql://LibAdmin:qwert123.@127.0.0.1:1433/Library', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
metadata = Base.metadata


class TBBook(Base):
    __tablename__ = 'TB_Book'

    bkID = Column(Integer, primary_key=True)
    bkCode = Column(Unicode(20))
    bkName = Column(Unicode(50))
    bkAuthor = Column(Unicode(30))
    bkPress = Column(Unicode(50))
    bkDatePress = Column(DateTime)
    bkISBN = Column(Unicode(15))
    bkCatalog = Column(Unicode(30))
    bkLanguage = Column(SmallInteger)
    bkPages = Column(Integer)
    bkPrice = Column(MONEY)
    bkDateIn = Column(DateTime)
    bkBrief = Column(Text(2147483647, 'Chinese_PRC_CI_AS'))
    bkCover = Column(LargeBinary)
    bkStatus = Column(Unicode(2))

    def __str__(self):
        return f'(Book {self.bkID} {self.bkCode} {self.bkName} {self.bkAuthor} {self.bkPress} {self.bkDatePress} {self.bkISBN} {self.bkCatalog} {self.bkLanguage} {self.bkPages} {self.bkPrice} {self.bkDateIn} {self.bkBrief} {self.bkCover} {self.bkStatus})'


class TBBorrow(Base):
    __tablename__ = 'TB_Borrow'

    BorrowID = Column(Numeric(12, 0), primary_key=True)
    rdID = Column(ForeignKey('TB_Reader.rdID'))
    bkID = Column(ForeignKey('TB_Book.bkID'))
    IdContinueTimes = Column(Integer)
    IdDateOut = Column(DateTime)
    IdDateRetPlan = Column(DateTime)
    IdOverDay = Column(Integer)
    IdOverMoney = Column(MONEY)
    IdPunishMoney = Column(MONEY)
    IsHasReturn = Column(BIT, server_default=FetchedValue())
    OperatorLend = Column(Unicode(20))
    OperatorRet = Column(Unicode(20))

    TB_Book = relationship('TBBook', primaryjoin='TBBorrow.bkID == TBBook.bkID', backref='tb_borrows')
    TB_Reader = relationship('TBReader', primaryjoin='TBBorrow.rdID == TBReader.rdID', backref='tb_borrows')

    def __str__(self):
        return f'(Borrow {self.BorrowID} {self.rdID} {self.bkID} {self.IdContinueTimes} {self.IdDateOut} {self.IdDateRetPlan} {self.IdOverDay} {self.IdOverMoney} {self.IdPunishMoney} {self.IsHasReturn} {self.OperatorLend} {self.OperatorRet})'


class TBReader(Base):
    __tablename__ = 'TB_Reader'

    rdID = Column(Integer, primary_key=True)
    rdName = Column(Unicode(20))
    rdSex = Column(Unicode(1))
    rdType = Column(ForeignKey('TB_ReaderType.rdType'), nullable=False)
    rdDept = Column(Unicode(20))
    rdPhone = Column(Unicode(25))
    rdEmail = Column(Unicode(25))
    rdDateReg = Column(DateTime)
    rdPhoto = Column(LargeBinary)
    rdStatus = Column(Unicode(2))
    rdBorrowQty = Column(Integer, server_default=FetchedValue())
    rdPwd = Column(Unicode(20), server_default=FetchedValue())
    rdAdminRoles = Column(SmallInteger)

    TB_ReaderType = relationship('TBReaderType', primaryjoin='TBReader.rdType == TBReaderType.rdType',
                                 backref='tb_readers')

    def __str__(self):
        return f'(Reader {self.rdID} {self.rdName} {self.rdSex} {self.rdType} {self.rdDept} {self.rdPhone} {self.rdEmail} {self.rdDateReg} {self.rdStatus} {self.rdBorrowQty} {self.rdPwd} {self.rdAdminRoles})'


class TBReaderType(Base):
    __tablename__ = 'TB_ReaderType'

    rdType = Column(SmallInteger, primary_key=True)
    rdTypeName = Column(Unicode(20), nullable=False, unique=True)
    CanLendQty = Column(Integer)
    CanLendDay = Column(Integer)
    CanContinueTimes = Column(Integer)
    PunishRate = Column(Float(53))
    DateValid = Column(SmallInteger, nullable=False)

    def __str__(self):
        return f'(ReaderType {self.rdType} {self.rdTypeName} {self.CanLendQty} {self.CanLendDay} {self.CanContinueTimes} {self.PunishRate} {self.DateValid})'
