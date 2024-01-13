#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa where
name matches the argument."""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    conn = db.cursor()
    conn.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY state.id"
            .format(sys.argv[4]))
    rows = conn.fetchall()
    for row in rows:
        print(row)

    conn.close()
    db.close()
