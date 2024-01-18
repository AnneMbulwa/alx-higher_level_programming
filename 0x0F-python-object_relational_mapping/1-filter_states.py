#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    conn = db.cursor()

    conn.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY state.id ASC")

    rows = conn.fetchall()
    for row in rows:
        print(row)
