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


def create_person_table(person):
    person = person.replace(" ", "_")

    create_person_assets_table = f"""
        CREATE TABLE IF NOT EXISTS {person}_assets
        (
            id integer PRIMARY KEY,
            date text
        );
    """

    create_person_liabilities_table = f"""
        CREATE TABLE IF NOT EXISTS {person}_liabilities
        (
            id integer PRIMARY KEY,
            date text
        );
    """

    conn = create_connection(db_file)
    cur = conn.cursor()

    if conn:
        cur.execute(create_person_assets_table)
        cur.execute(create_person_liabilities_table)
        conn.commit()
        conn.close()
    else:
        print("Error")


def read_available_people():
    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    conn = create_connection(db_file)
    cur = conn.cursor()
    if conn:
        tables = cur.execute(sql).fetchall()
        people = list(
            set([table[0].split("_")[0] for table in tables if "expenses" not in table[0]])
        )
        return people


def add_asset_to_person(db_file, person, asset):
    add_person_asset = f"""
        ALTER TABLE {person}_assets
        (
            {asset} float
        );
    """
    conn = create_connection(db_file)
    cur = conn.cursor()

    if conn:
        cur.execute(add_person_asset)
        conn.commit()
    else:
        print("Error")


def add_liability_to_person(db_file, person, liability):
    add_person_liability = f"""
        ALTER TABLE {person}_assets
        (
            {liability} float
        );
    """
    conn = create_connection(db_file)
    cur = conn.cursor()

    if conn:
        cur.execute(add_person_liability)
        conn.commit()
    else:
        print("Error")


def read_person(person):
    conn = create_connection(db_file)
    cur = conn.cursor()
    asset_names = cur.execute(f"PRAGMA table_info({person}_assets);").fetchall()
    asset_names = [name[1] for name in asset_names if "id" not in name]

    liability_names = cur.execute(f"PRAGMA table_info({person}_liabilities);").fetchall()
    liability_names = [name[1] for name in liability_names if "id" not in name]

    print(asset_names, liability_names)

    cur.execute(f"SELECT {', '.join(asset_names)} FROM {person}_assets")
    assets = cur.fetchall()
    cur.execute(f"SELECT {', '.join(liability_names)} FROM {person}_liabilities")
    liabilities = cur.fetchall()

    return asset_names, liability_names, assets, liabilities


def read_expenses():
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM expenses")
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
