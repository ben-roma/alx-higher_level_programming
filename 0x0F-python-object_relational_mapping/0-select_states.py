#!/usr/bin/python3
"""
Module 0-select_states.py
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username, password, dbname):
    """
    Lists all states from the database in ascending order by states.id.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
