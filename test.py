# import pymssql
# #
# # con = pymssql.connect(server='localhost', user='SA', password='qwert123.', charset='utf8')
# # con.autocommit(True)
# # cur = con.cursor()
# # cur.execute('create database test')
# # print(cur.description)

from models import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

print((7 & 0b0110) == 0b0110)
s = bin(7)
print(type(s), s)
