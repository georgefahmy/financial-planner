import PySimpleGUI as sg
import sqlite3 as s
import datetime
import json
import os
import sys
import base64

from string import capwords
from make_database import make_database
from sql_functions import *

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()

db_file = os.path.join(wd, "database.db")
make_database(db_file)

default_font = ("Arial", 14)

expenses = sorted(read_expenses(), key=lambda x: x[2], reverse=True)
available_people = read_available_people()

expense_name_list = "\n".join([f"{expense[1]}:" for expense in expenses])
expense_amount_list = "\n".join(["${:,.2f}".format(expense[2]) for expense in expenses])
total_expenses = "${:,.2f}".format(sum([expense[2] for expense in expenses]))

expense_frame_layout = [
    [
        sg.Frame(
            "",
            layout=[
                [
                    sg.Text("Expense: ", font=default_font),
                    sg.Input("", size=(15, 1), font=default_font, key="new_expense_name"),
                    sg.Text("Amount: ", font=default_font),
                    sg.Input("", size=(8, 1), font=default_font, key="new_expense_amount"),
                    sg.Button(
                        "Submit", font=default_font, key="submit_new_expense", bind_return_key=True
                    ),
                ]
            ],
            size=(440, 40),
        ),
    ],
    [
        sg.Frame(
            "",
            layout=[
                [sg.Text("Recurring Expenses", font=default_font)],
                [sg.HorizontalSeparator()],
                [
                    sg.Column(
                        [
                            [
                                sg.Text(
                                    expense_name_list,
                                    font=default_font,
                                    key="expense_name_list",
                                    expand_x=True,
                                ),
                                sg.Text("", size=(22, 1), expand_x=True),
                                sg.Text(
                                    expense_amount_list,
                                    font=default_font,
                                    justification="r",
                                    expand_x=True,
                                    key="expense_amount_list",
                                ),
                            ],
                        ],
                        scrollable=True,
                        vertical_scroll_only=True,
                        expand_y=True,
                        size=(440, 580),
                    ),
                ],
                [sg.HorizontalSeparator()],
                [
                    sg.Column(
                        [
                            [
                                sg.Text(
                                    "Total:",
                                    font=default_font,
                                    expand_x=True,
                                ),
                                sg.Text("", expand_x=True),
                                sg.Text(
                                    total_expenses,
                                    font=default_font,
                                    key="total_expenses",
                                    expand_x=True,
                                ),
                            ],
                        ],
                        size=(440, 45),
                        expand_x=True,
                    ),
                ],
            ],
            size=(440, 730),
        )
    ],
]

menu_bar_layout = [
    [
        "&File",
        [
            "Load Database",
            "Export Database",
            "New Person",
            "Read Person",
            ("Expenses", ["View All Expenses", "!Delete Expense"]),
        ],
    ],
    ["Reports", ["Budget Report", "Performance Chart"]],
    ["Help", ["!About", "!How To", "!Feedback"]],
]

layout = [
    [sg.Menu(menu_bar_layout, font=("Arial", "12"), key="-MENU-")],
    [expense_frame_layout],
]

window = sg.Window(
    "Financial Planner PRO",
    layout=layout,
    element_justification="top",
    resizable=True,
    finalize=True,
    size=(1250, 730),
)

while True:
    event, values = window.Read()

    if event:
        print(event, values)

    if event == "New Person":
        person = capwords(sg.popup_get_text("Enter new person's name"))
        create_person_table(person)
        person_info = read_person(person)

    if event == "Read Person":
        available_people = read_available_people()
        if len(available_people) == 1:
            person = available_people[0]

        person_info = read_person(person)

    if event == "submit_new_expense":
        expense = values["new_expense_name"]
        amount = values["new_expense_amount"]
        if not expense or not amount:
            continue
        expense_info = (expense, float(amount))
        success = add_expense(db_file, expense_info)
        expenses = sorted(read_expenses(), key=lambda x: x[2], reverse=True)
        expense_name_list = "\n".join([f"{expense[1]}:" for expense in expenses])
        expense_amount_list = "\n".join(["${:,.2f}".format(expense[2]) for expense in expenses])
        total_expenses = "${:,.2f}".format(sum([expense[2] for expense in expenses]))

        window["expense_name_list"].update(value=expense_name_list)
        window["expense_amount_list"].update(value=expense_amount_list)
        window["total_expenses"].update(value=total_expenses)
        window["new_expense_name"].update(value="")
        window["new_expense_amount"].update(value="")

    if event in (None, "Quit", sg.WIN_CLOSED):
        window.close()
        break
