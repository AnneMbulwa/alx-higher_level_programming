#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":

    cur = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argb[2],
            db=sys.argv[3]
            )

    conn = cur.cursor()
    db = conn.execute(
            "SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id")
    city = db.fetchall()
    for row in city:
        print(row)

    conn.close()
    cur.close()
