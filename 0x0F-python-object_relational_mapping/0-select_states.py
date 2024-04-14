#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
It includes exception handling and ensures that database
resources are freed properly.
"""

import MySQLdb
from sys import argv


def main():
    """
    Connects to the database, fetches and prints all states sorted by ID.
    Uses command line arguments for database connection parameters.
    """
    try:
        # Connection to the MySQL database
        db = MySQLdb.connect(host="localhost",
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3],
                             port=3306)
        # Cursor to execute query
        cur = db.cursor()
        # Execute the SQL query
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        # Fetch all the rows returned by the database
        rows = cur.fetchall()
        # Print each row
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
    finally:
        # Ensure that cursor and connection are closed properly
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(argv) == 4:
        main()
    else:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
