#!/usr/bin/python3
import MySQLdb
from sys import argv
if __name__ == '__main__':
    if(len(argv) == 4):
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        lol = "SELECT cities.id, cities.name, states.name \
FROM cities INNER JOIN states ON cities.state_id = states.id"
        cur.execute(lol)
        rows = cur.fetchall()
        for row in rows:
            print(row)
