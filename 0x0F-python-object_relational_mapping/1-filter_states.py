#!/usr/bin/python3
"""Lists all states with a name starting with N
"""
import sys
import MySQLdb

f __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")
    query = cur.fetchall()

    for states in query:
        print(states)

    cur.close()
    db.close()
