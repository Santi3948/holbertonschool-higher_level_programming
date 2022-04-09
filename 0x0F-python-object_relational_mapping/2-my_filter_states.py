#!/usr/bin/python3
"""2. Filter states by user input
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    if(len(argv) == 5):
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE\
 name LIKE '%{}%'" .format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
