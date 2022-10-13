#import sqlite3
import mysql.connector as mysql


def main():
    #db = sqlite3.connect(":memory:")
    db = mysql.connect(user="root", password="", host="localhost", database="test")
    cur = db.cursor() #cur = cursor method

    #cur.execute("SELECT sqlite_version()")
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()[0]
    #print(f"SQLite version {version}")
    print(f"Mysql version {version}")

    cur.close()
    db.close()

main()
