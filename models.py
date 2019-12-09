from manage import db


class TBBook(db.Model):
    __tablename__ = 'TB_Book'

    bkID = db.Column(db.Integer, primary_key=True)
    bkCode = db.Column(db.Unicode(20))
    bkName = db.Column(db.Unicode(50))
    bkAuthor = db.Column(db.Unicode(30))
    bkPress = db.Column(db.Unicode(50))
    bkDatePress = db.Column(db.DateTime)
    bkISBN = db.Column(db.Unicode(15))
    bkCatalog = db.Column(db.Unicode(30))
    bkLanguage = db.Column(db.SmallInteger)
    bkPages = db.Column(db.Integer)
    bkPrice = db.Column(db.MONEY)
    bkDateIn = db.Column(db.DateTime)
    bkBrief = db.Column(db.Text(2147483647, 'Chinese_PRC_CI_AS'))
    bkCover = db.Column(db.LargeBinary)
    bkStatus = db.Column(db.Unicode(2))


class TBBorrow(db.Model):
    __tablename__ = 'TB_Borrow'

    BorrowID = db.Column(db.Numeric(12, 0), primary_key=True)
    rdID = db.Column(db.ForeignKey('TB_Reader.rdID'))
    bkID = db.Column(db.ForeignKey('TB_Book.bkID'))
    IdContinueTimes = db.Column(db.Integer)
    IdDateOut = db.Column(db.DateTime)
    IdDateRetPlan = db.Column(db.DateTime)
    IdOverDay = db.Column(db.Integer)
    IdOverMoney = db.Column(db.MONEY)
    IdPunishMoney = db.Column(db.MONEY)
    IsHasReturn = db.Column(db.BIT, server_default=db.FetchedValue())
    OperatorLend = db.Column(db.Unicode(20))
    OperatorRet = db.Column(db.Unicode(20))

    TB_Book = db.relationship('TBBook', primaryjoin='TBBorrow.bkID == TBBook.bkID', backref='tb_borrows')
    TB_Reader = db.relationship('TBReader', primaryjoin='TBBorrow.rdID == TBReader.rdID', backref='tb_borrows')


class TBReader(db.Model):
    __tablename__ = 'TB_Reader'

    rdID = db.Column(db.Integer, primary_key=True)
    rdName = db.Column(db.Unicode(20))
    rdSex = db.Column(db.Unicode(1))
    rdType = db.Column(db.ForeignKey('TB_ReaderType.rdType'), nullable=False)
    rdDept = db.Column(db.Unicode(20))
    rdPhone = db.Column(db.Unicode(25))
    rdEmail = db.Column(db.Unicode(25))
    rdDateReg = db.Column(db.DateTime)
    rdPhoto = db.Column(db.LargeBinary)
    rdStatus = db.Column(db.Unicode(2))
    rdBorrowQty = db.Column(db.Integer, server_default=db.FetchedValue())
    rdPwd = db.Column(db.Unicode(20), server_default=db.FetchedValue())
    rdAdminRoles = db.Column(db.SmallInteger)

    TB_ReaderType = db.relationship('TBReaderType', primaryjoin='TBReader.rdType == TBReaderType.rdType', backref='tb_readers')


class TBReaderType(db.Model):
    __tablename__ = 'TB_ReaderType'

    rdType = db.Column(db.SmallInteger, primary_key=True)
    rdTypeName = db.Column(db.Unicode(20), nullable=False, unique=True)
    CanLendQty = db.Column(db.Integer)
    CanLendDay = db.Column(db.Integer)
    CanContinueTimes = db.Column(db.Integer)
    PunishRate = db.Column(db.Float(53))
    DateValid = db.Column(db.SmallInteger, nullable=False)
