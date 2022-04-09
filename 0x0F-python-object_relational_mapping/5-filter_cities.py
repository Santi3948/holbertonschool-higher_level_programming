#!/usr/bin/python3
"""5. All cities by state
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    if(len(argv) == 5):
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        lol = "SELECT cities.name FROM cities INNER JOIN states ON\
 cities.state_id = states.id WHERE states.name LIKE %s"
        cur.execute(lol, (argv[4],))
        rows = cur.fetchall()
        for row in range(len(rows)):
            if(row < len(rows) - 1):
                print("{}, " .format(rows[row][0]), end="")
            elif(row >= 0):
                print("{}" .format(rows[row][0]))
        if not rows:
            print()
