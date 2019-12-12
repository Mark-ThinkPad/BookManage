# import pymssql
# #
# # con = pymssql.connect(server='localhost', user='SA', password='qwert123.', charset='utf8')
# # con.autocommit(True)
# # cur = con.cursor()
# # cur.execute('create database test')
# # print(cur.description)

from models import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
try:
    q = TBReader.query.filter(TBReader.rdID == '2017001', TBReader.rdPwd == '12').one()
except NoResultFound:
    print('无查找结果')
except MultipleResultsFound:
    print('后台数据出现问题')
