
from platform import python_version
import sqlite3
import mysql.connector as mysql


def main():
    print(f'This is python version {python_version()}')
    print(f"SQLite version {sqlite3.sqlite_version}")
    print(f"MySQL connector version {mysql.__version__}")


if __name__ == "__main__":
    main()
