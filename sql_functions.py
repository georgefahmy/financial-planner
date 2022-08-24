import sqlite3
import json
import os
import sys
from collections import OrderedDict

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()

db_file = os.path.join(wd, "database.db")


def create_connection(db_file=db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


def read_expenses():
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM expenses")
    return cur.fetchall()


def read_assets():
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM assets")
    return cur.fetchall()


def read_liabilities():
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM liabilities")
    return cur.fetchall()


def add_expense(db_file, expense_info):
    conn = create_connection(db_file)
    cur = conn.cursor()
    sql = f"""
        INSERT OR IGNORE INTO expenses (expense, amount) VALUES(?,?)
        """
    cur.execute(sql, expense_info)
    conn.commit()
    conn.close()
    return


def add_asset(db_file, asset_info):
    conn = create_connection(db_file)
    cur = conn.cursor()
    sql = f"""
        INSERT OR IGNORE INTO assets (person, asset, amount, date) VALUES(?,?,?,?)
        """
    cur.execute(sql, asset_info)
    conn.commit()
    conn.close()
    return


def add_liability(db_file, liability_info):
    conn = create_connection(db_file)
    cur = conn.cursor()
    sql = f"""
        INSERT OR IGNORE INTO assets (person, liability, amount, date) VALUES(?,?,?,?)
        """
    cur.execute(sql, liability_info)
    conn.commit()
    conn.close()
    return
