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
import datetime

# session = db_session()
# b = session.query(TBBorrow).all()
# for i in b:
#     print(type(i.IsHasReturn), i.IsHasReturn)
# session.commit()
# session.close()

d1 = datetime.datetime(2018,10,31)   # 第一个日期
d2 = datetime.datetime.now()   # 第二个日期
interval = d2 - d1                   # 两日期差距
print(type(interval.days), interval.days)
print(type(interval.seconds), interval.seconds)
