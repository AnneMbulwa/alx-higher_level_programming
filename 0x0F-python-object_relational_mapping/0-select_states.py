#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user="username",
            passwd="password",
            port=3306,
            database="database"
            )
    cur = db.cursor()
    cur.execute ("SELECT * FROM states ORDER BY state.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
