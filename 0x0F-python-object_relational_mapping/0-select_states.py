#!/usr/bin/python3
""" this excute the database to return all columns
of states table"""
if __name__ == '__main__':
    import MySQLdb
    h = 'localhost'
    r = 'root'
    mdb = 'hbtn_0e_0_usa'
    db = MySQLdb.connect(host=h, port=3306, user=r, passwd=r, db=mdb)
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
