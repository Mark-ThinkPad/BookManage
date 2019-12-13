# import pymssql
# #
# # con = pymssql.connect(server='localhost', user='SA', password='qwert123.', charset='utf8')
# # con.autocommit(True)
# # cur = con.cursor()
# # cur.execute('create database test')
# # print(cur.description)

from models import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

session = db_session()
session.query(TBReader).filter(TBReader.rdID == '2017001', TBReader.rdPwd == 'qwert').delete()
session.commit()
session.close()
