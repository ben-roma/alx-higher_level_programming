#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


def list_states_n(username, password, dbname):
    """
    Lists all states from the database starting with 'N'.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        list_states_n(argv[1], argv[2], argv[3])
