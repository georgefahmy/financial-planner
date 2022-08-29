import sqlite3 as s
import json
import os
import sys

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()

db_file = os.path.join(wd, "databse.db")


def make_database(db_file=db_file):
    create_expense_database = """
        CREATE TABLE IF NOT EXISTS expenses
        (
            id integer PRIMARY KEY,
            expense text NOT NULL,
            amount float
        );
    """

    conn = s.connect(db_file)
    c = conn.cursor()

    if conn:
        c.execute(create_expense_database)
        conn.commit()
    else:
        print("Error")
