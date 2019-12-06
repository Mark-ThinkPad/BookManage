import pymssql

con = pymssql.connect(server='localhost', user='SA', password='qwert123.', charset='utf8')
con.autocommit(True)
cur = con.cursor()
cur.execute('create database test')
print(cur.description)