import PySimpleGUI as sg
import datetime
import json
import os
import sys
import base64
from person_tab_layout import person_tab

default_font = ("Arial", 14)


tab_group = sg.TabGroup(
    layout=[
        [
            sg.Tab(
                "George",
                [
                    person_tab(),
                ],
                key="George",
            ),
            sg.Tab(
                "Britney",
                [
                    person_tab(),
                ],
                key="Britney",
            ),
        ]
    ],
    tab_location="topleft",
    tab_background_color="darkblue",
    title_color="white",
    selected_background_color="teal",
    selected_title_color="white",
    expand_y=True,
)
layout = [
    [
        [tab_group],
    ],
    [sg.Quit()],
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

    if event in (None, "Quit", sg.WIN_CLOSED):
        window.close()
        break
