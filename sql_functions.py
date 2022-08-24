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


def read_assets():
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM assets")
    return cur.fetchall()


def read_expenses():
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM assets")
    return cur.fetchall()


def read_liabilities():
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM assets")
    return cur.fetchall()
