#!/usr/bin/python3
"""Asc order"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY cities.id")
    for i in c:
        print(i)
