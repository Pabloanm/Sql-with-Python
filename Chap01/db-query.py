import sqlite3


def main():
    db = sqlite3.connect("../db/scratch.db")
    cur = db.cursor()

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.execute("CREATE TABLE IF NOT EXISTS temp ( a TEXT, b TEXT, c TEXT )")
    cur.execute("INSERT INTO temp VALUES ('one', 'two', 'three')")
    cur.execute("INSERT INTO temp VALUES ('four', 'five', 'six')")
    cur.execute("INSERT INTO temp VALUES ('seven', 'eight', 'nine')")
    db.commit()

    cur.execute("SELECT * FROM temp")
    '''
    #Alt 1 Iteration
    # iterate rows one by one
    row = cur.fetchone()
    while row:
        print(row)
        row = cur.fetchone()
    '''
    '''
    # Alt 2 Iteration
    # clean code - iterate rows one by one
    for row in cur:
        print(row)
    '''
    # Alt 3 Iteration
    # fetch all the raws in the table, i need memory to hold all data.
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
