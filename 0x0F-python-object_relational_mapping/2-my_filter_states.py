#!/usr/bin/python3
"""Lists States"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.Connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
