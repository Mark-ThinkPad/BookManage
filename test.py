# import pymssql
# #
# # con = pymssql.connect(server='localhost', user='SA', password='qwert123.', charset='utf8')
# # con.autocommit(True)
# # cur = con.cursor()
# # cur.execute('create database test')
# # print(cur.description)

from models import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from random import randint

session = db_session()
s = session.query(TBBorrow).filter(TBBorrow.rdID == '10').all()
print(len(s), type(s))
for i in s:
    print('触发')
session.commit()
session.close()
