#!/usr/bin/node
""" Lists all states from the databases hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    query = cur.fetchall()

    for states in query:
        print(states)

    cur.close()
    db.clode()
