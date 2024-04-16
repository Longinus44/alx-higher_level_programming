#!/usr/bin/python3

""" This script lists all states from the database"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], dbName=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BT id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
