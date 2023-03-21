#!/usr/bin/python3

"""
this module  lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

Author: Aymeric Mbepa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                'N%' ORDER BY states.id ASC")

    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()
