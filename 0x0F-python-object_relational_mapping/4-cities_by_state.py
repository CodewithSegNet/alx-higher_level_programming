#!/usr/bin/python3
"""Script lists all cities from database
Takes three arguments:
    mysql username
    mysql password
    database name
Connects to default host (localhost) and port (3306)
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
