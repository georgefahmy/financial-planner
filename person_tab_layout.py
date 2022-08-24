import PySimpleGUI as sg


def add_expense_row():
    pass


def add_person_tab():
    name = sg.popup_get_text("Enter Name:")

    default_font = ("Arial", 14)
    inputs_tab = [
        sg.Tab(
            "Assets",
            layout=[
                [
                    sg.Text(
                        "Enter Asset Name",
                        size=(15, 1),
                    ),
                    sg.Input(size=(20, 1), font=default_font, key=f"asset_{0}"),
                ]
            ],
        ),
        sg.Tab(
            "Liabilities",
            layout=[
                [
                    sg.Text(
                        "Enter Asset Name",
                        size=(15, 1),
                    ),
                    sg.Input(size=(20, 1), font=default_font, key=f"liability_{0}"),
                ]
            ],
        ),
        sg.Tab(
            "Expenses",
            layout=[
                [
                    sg.Column(
                        [
                            [
                                sg.Text(
                                    "Expenses",
                                    size=(15, 1),
                                    expand_x=True,
                                ),
                                sg.Button(
                                    "New Expense",
                                    size=(12, 1),
                                    key="new_expense",
                                    font=("Arial", 12),
                                ),
                            ],
                            [
                                sg.Text(
                                    "Enter Expense:",
                                    size=(15, 1),
                                ),
                                sg.Input(size=(20, 1), font=default_font, key=f"expense_{0}"),
                            ],
                            [
                                sg.Text(
                                    "Enter Expense:",
                                    size=(15, 1),
                                ),
                                sg.Input(size=(20, 1), font=default_font, key=f"expense_{1}"),
                            ],
                        ],
                    )
                ]
            ],
        ),
    ]
    person_tab = sg.Tab(
        name,
        layout=[
            [
                sg.TabGroup(
                    layout=[
                        inputs_tab,
                    ],
                    tab_location="topleft",
                    tab_background_color="darkblue",
                    title_color="white",
                    selected_background_color="teal",
                    selected_title_color="white",
                    expand_y=True,
                    key=name,
                ),
            ],
        ],
    )

    return person_tab
