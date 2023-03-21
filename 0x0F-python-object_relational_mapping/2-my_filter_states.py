#!/usr/bin/python3
"""
this module takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

AUTHOR: Aymeric Mbepa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()

    qr = "SELECT * FROM states WHERE states.name LIKE %s ORDER BY states.id ASC"
    cur.execute(qr, ('{}%'.format(state_name),))

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
