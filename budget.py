import PySimpleGUI as sg
import sqlite3 as s
import datetime
import json
import os
import sys
import base64
from make_database import make_database

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()

db_file = os.path.join(wd, "database.db")
make_database(db_file)

default_font = ("Arial", 14)

layout = [[]]

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

    if event in (None, "Quit", sg.WIN_CLOSED):
        window.close()
        break
