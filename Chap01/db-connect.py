#!/usr/bin/env python3
# Copyright 2021 BHG [bw.org]
# as of 2021-04-07 bw

import mysql.connector as mysql


def main():
    db = mysql.connect(user="root", password="", host="localhost", database="test")
    cur = db.cursor()

    cur.execute("SELECT VERSION()")
    version = cur.fetchone()[0]
    print(f"Mysql version {version}")

    cur.close()
    db.close()



main()
