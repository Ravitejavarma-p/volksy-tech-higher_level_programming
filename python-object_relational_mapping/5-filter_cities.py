#!/usr/bin/python3
"""Asc order using joins"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM cities \
               INNER JOIN states \
               ON cities.state_id = states.id \
               ORDER BY cities.id")
    for i in c:
        if i[4] == sys.argv[4]:
            print(i)
