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

expenses = sorted(read_expenses(), key=lambda x: x[2], reverse=True)


expense_name_list = "\n".join([f"{expense[1]}:" for expense in expenses])
expense_amount_list = "\n".join(["${:,.2f}".format(expense[2]) for expense in expenses])
total_expenses = "${:,.2f}".format(sum([expense[2] for expense in expenses]))

expense_tab_layout = [
    [
        sg.Frame(
            "",
            layout=[
                [
                    sg.Text("New Expense: ", font=default_font),
                    sg.Input("", size=(10, 1), font=default_font, key="new_expense_name"),
                    sg.Text("Amount: ", font=default_font),
                    sg.Input("", size=(10, 1), font=default_font, key="new_expense_amount"),
                    sg.Button(
                        "Submit", font=default_font, key="submit_new_expense", bind_return_key=True
                    ),
                ]
            ],
        ),
    ],
    [
        sg.Frame(
            "",
            layout=[
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
                                sg.Text("", expand_x=True),
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
                    ),
                ]
            ],
        )
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Text("Total:", font=default_font),
        sg.Text("", expand_x=True),
        sg.Text(
            total_expenses,
            font=default_font,
            key="total_expenses",
        ),
    ],
]

expense_tab = sg.Tab("Expenses", layout=expense_tab_layout)

assets = read_assets()


asset_name_list = "\n".join([f"{asset[2]}:" for asset in assets])
asset_amount_list = "\n".join(["${:,.2f}".format(asset[3]) for asset in assets])
total_assets = "${:,.2f}".format(sum([asset[3] for asset in assets]))

asset_tab_layout = [
    [
        sg.Frame(
            "",
            layout=[
                [
                    sg.Text("New Asset: ", font=default_font),
                    sg.Input("", size=(10, 1), font=default_font, key="new_asset_name"),
                    sg.Text("Amount: ", font=default_font),
                    sg.Input("", size=(10, 1), font=default_font, key="new_asset_amount"),
                    sg.Button(
                        "Submit", font=default_font, key="submit_new_asset", bind_return_key=True
                    ),
                ]
            ],
        ),
    ],
    [
        sg.Frame(
            "",
            layout=[
                [
                    sg.Column(
                        [
                            [
                                sg.Text(
                                    asset_name_list,
                                    font=default_font,
                                    key="asset_name_list",
                                    expand_x=True,
                                ),
                                sg.Text("", expand_x=True),
                                sg.Text(
                                    asset_amount_list,
                                    font=default_font,
                                    justification="r",
                                    expand_x=True,
                                    key="asset_amount_list",
                                ),
                            ],
                        ],
                        scrollable=True,
                        vertical_scroll_only=True,
                    ),
                ]
            ],
        )
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Text("Total:", font=default_font),
        sg.Text("", expand_x=True),
        sg.Text(
            total_assets,
            font=default_font,
            key="total_assets",
        ),
    ],
]

asset_tab = sg.Tab("Assets", layout=asset_tab_layout)

liabilities = read_liabilities()
tabs = sg.TabGroup(layout=[[expense_tab], [asset_tab]])

menu_bar_layout = [
    [
        "&File",
        [
            "Save",
            "Load Database",
            "Export Database",
            "Expenses",
            ["New Expense", "!Delete Expense", "View All Expenses"],
            "Assets",
            ["New Asset", "!Delete Asset", "View All Assets"],
            "Liabilities",
            ["New Liability", "!Delete Liability", "View All Liabilities"],
        ],
    ],
    ["Reports", ["Budget Report", "Performance Chart"]],
    ["Help", ["!About", "!How To", "!Feedback"]],
]

layout = [
    [sg.Menu(menu_bar_layout, font=("Arial", "12"), key="-MENU-")],
    [tabs],
    # [net_worth_frame],
]

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

    if event == "submit_new_expense":
        expense = values["new_expense_name"]
        amount = values["new_expense_amount"]
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
