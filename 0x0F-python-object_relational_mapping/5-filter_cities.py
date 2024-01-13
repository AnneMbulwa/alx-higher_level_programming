#!/usr/bin/python3

"""takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    coon = db.cursor()
    coon.execute(
            "SELECT cities.name, state.name
            FROM cities JOIN states
            ON state.id = citiea.state_id
            WHERE state.name = %s ORDER BY cities.id", (sys.argv[4],))
    rows = coon.fetchall()
    print(", ".join([row[0] for row in rows]))

    coon.close()
    db.close()
