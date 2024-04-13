#!/usr/bin/python3
"""A module to list rows from a database"""


import MySQLdb
db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="hbtn_0e_0_usa", port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM hbtn_0e_0_usa ORDER BY stated.id ASC")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print("%s," % col, end=" "
    print("\n")
cur.close()
db.close()
