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
    db = MySQLdb.connect(host=h, port=3306, user=r, passwd=m, db=mdb)
    query = "select cities.name from cities inner join states\
            on cities.state_id = states.id where states.name = %s\
            order by cities.id ASC;"
    cur = db.cursor()
    cur.execute(query, (s,))
    rows = cur.fetchall()
    ls = []
    for row in rows:
        ls.append(row[0])
    print(", ".join(ls))
