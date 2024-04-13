#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    user_input = argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (user_input, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
