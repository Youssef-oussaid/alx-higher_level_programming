#!/usr/bin/python3
"""A module to list rows from a database"""


import MySQLdb
import sys


db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3],
                     port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM hbtn_0e_0_usa ORDER BY states.id ASC")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print("%s," % col, end=" ")
    print("\n")
cur.close()
db.close()

if __name__ == "__main__":
    main()