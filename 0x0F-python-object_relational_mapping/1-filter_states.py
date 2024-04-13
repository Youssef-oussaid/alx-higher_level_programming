#!/usr/bin/python3
"""lists state names"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.Connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name "
                "LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
