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
    s = sys.argv[4]
    query = "select * from states where name = %s order by states.id ASC;"
    db = MySQLdb.connect(host=h, port=3306, user=r, passwd=m, db=mdb)
    cur = db.cursor()
    cur.execute(query, (s,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
