#!/usr/bin/python3
"""
this module lists all states from the database hbtn_0e_0_usa

Author: Aymeric Mbepa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    data = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=data)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()