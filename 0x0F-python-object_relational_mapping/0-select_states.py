#!/usr/bin/python3
""" this excute the database to return all columns
of states table"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    h = 'localhost'
    r = sys.argv[1]
    m = sys.argv[2]
    mdb = sys.argv[3]
    db = MySQLdb.connect(host=h, port=3306, user=r, passwd=m, db=mdb)
    cur = db.cursor()
    cur.execute("select * from states order by id")
    rows = cur.fetchall()
    for row in rows:
        print("(", end="")
        for col in row:
            if not isinstance(col, int):
                print("'" + col + "'", end="")
            else:
                print(col, end=", ")
        print(")")
