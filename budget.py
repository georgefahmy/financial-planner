import PySimpleGUI as sg
import sqlite3 as s
import datetime
import json
import os
import sys
import base64
from make_database import make_database
from sql_functions import *

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()

db_file = os.path.join(wd, "database.db")
make_database(db_file)

default_font = ("Arial", 14)

expenses = read_expenses()
assets = read_assets()
liabilities = read_liabilities()

layout = [[sg.Button("Add Expense", key="add_expense", font=default_font)]]

window = sg.Window(
    "Financial Planner PRO",
    layout=layout,
    element_justification="top",
    resizable=True,
    finalize=True,
    size=(600, 400),
)

while True:
    event, values = window.Read()

    if event:
        print(event, values)

    if event == "add_expense":
        expense = sg.popup_get_text("Expense Name")
        amount = sg.popup_get_text("Amount")
        expense_info = (expense, float(amount))
        success = add_expense(db_file, expense_info)
        expenses = read_expenses()
        for expense in expenses:
            print(expense[1], expense[2])

    if event in (None, "Quit", sg.WIN_CLOSED):
        window.close()
        break
