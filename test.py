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
b = session.query(TBBorrow).all()
for i in b:
    print(type(i.IsHasReturn), i.IsHasReturn)
session.commit()
session.close()
