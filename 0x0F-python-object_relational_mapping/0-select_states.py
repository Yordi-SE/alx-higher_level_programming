#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='hbtn_0e_0_usa')
cur = db.cursor()
cur.execute("select * from states")
rows = cur.fetchall()
for row in rows:
    print("(", end="")
    for col in row:
        if not isinstance(col, int):
            print("'" + col + "'", end="")
        else:
            print(col, end=", ")
    print(")")
