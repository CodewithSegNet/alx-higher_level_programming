#!/usr/bin/python3
"""Script takes state name as an argument and lists all cities of given state
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
    param = (argv[4], )
    c.execute("SELECT * FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", param)
    rows = c.fetchall()
    cities = []
    for row in rows:
        if row[4] == param[0]:
            cities.append(row[2])
    print(', '.join(cities))
    c.close()
    db.close()
