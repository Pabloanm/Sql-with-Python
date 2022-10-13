#you need to create database "scratch"

import mysql.connector as mysql

MY_HOST = 'localhost'
MY_USER = 'root'
MY_PASS = ''


def main():
    db = mysql.connect(host=MY_HOST, user=MY_USER, password=MY_PASS, database='scratch')
    cur = db.cursor(prepared=True) # to use prepared statements

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.execute("CREATE TABLE IF NOT EXISTS temp ( a TEXT, b TEXT, c TEXT )")
    cur.execute("INSERT INTO temp VALUES ('one', 'two', 'three')")
    cur.execute("INSERT INTO temp VALUES ('four', 'five', 'six')")
    cur.execute("INSERT INTO temp VALUES ('seven', 'eight', 'nine')")

    cur.execute("SELECT * FROM temp")
    for row in cur:
        print(row)

    query = "SELECT * FROM temp WHERE a = ?"
    cur.execute(query, ('four',)) # if you only have one value in the tuple, you need that comma to make it actually create a tuple

    for row in cur:
        print(f"result is {row}")

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
