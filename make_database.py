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

    create_assets_table = """
        CREATE TABLE IF NOT EXISTS assets
        (
            id integer PRIMARY KEY,
            person text NOT NULL,
            asset text NOT NULL,
            amount float,
            date text
        );
    """

    create_liabilities_table = """
        CREATE TABLE IF NOT EXISTS liabilities
        (
            id integer PRIMARY KEY,
            person text NOT NULL,
            liability text NOT NULL,
            amount float,
            date text
        );
    """

    conn = s.connect(db_file)
    c = conn.cursor()

    if conn:
        c.execute(create_expense_database)
        c.execute(create_assets_table)
        c.execute(create_liabilities_table)
        conn.commit()
    else:
        print("Error")
