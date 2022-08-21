import PySimpleGUI as sg


def person_tab():
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
                    sg.Input(size=(20, 1), font=default_font),
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
                    sg.Input(size=(20, 1), font=default_font),
                ]
            ],
        ),
    ]

    return [
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
        ),
    ]
