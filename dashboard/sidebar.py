"""
Sidebar Navigation
"""

from streamlit_option_menu import option_menu


def sidebar():

    with __import__("streamlit").sidebar:

        selected = option_menu(

            menu_title="Navigation",

            options=[

                "Home",

                "Live Detection",

                "Analytics",

                "Traffic Signals",

                "Reports",

                "Settings"

            ],

            icons=[

                "house",

                "camera-video",

                "bar-chart",

                "stoplights",

                "file-earmark-text",

                "gear"

            ],

            default_index=0

        )

    return selected