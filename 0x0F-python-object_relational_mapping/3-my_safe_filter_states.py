#!/usr/bin/python3
import MySQLdb
from sys import argv
if __name__ == '__main__':
    if(len(argv) == 5):
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        lol = "SELECT * FROM states WHERE name LIKE %s"
        cur.execute(lol, (argv[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)
