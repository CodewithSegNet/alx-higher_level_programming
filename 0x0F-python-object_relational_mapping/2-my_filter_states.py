#!/usr/bin/python3
"""Script displays all values in states table that match given argument
Takes four arguments:
    mysql username
    mysql password
    database name
    name to match
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name = '{}'\
            ORDER BY states.id ASC""".format(argv[4]))
    rows = c.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    c.close()
    db.close()
