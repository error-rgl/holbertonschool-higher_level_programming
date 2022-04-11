#!/usr/bin/python3
""" List all cities from a database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Open database connection
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    # execute SQL query using execute() method.
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id;
    """)
    query = cur.fetchall()

    for states in query:
        print(states)

    cur.close()
    db.close()
