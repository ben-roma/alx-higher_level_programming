#!/usr/bin/python3
"""
This script lists all states from the
<<<<<<< HEAD
database `hbtn_0e_0_usa`.
=======
database
>>>>>>> e7b340de4c071690d3296e63e3d997730af036f3
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
<<<<<<< HEAD
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
=======
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
>>>>>>> e7b340de4c071690d3296e63e3d997730af036f3
