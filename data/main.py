"""Contains the main program function, sets up the Control class
containing the program and event loop. Also builds the state
dictionary, defining the different states."""

from data import main_menu
#from . import setup, tools
from . import constants as c


def main():
    """Main function"""

    runtime = tools.Control("yo", c.MAINMENU)
    runtime.setup_state(build_dict())
    runtime.set_state(c.MAINMENU)
    runtime.main()


def build_dict():
    """Builds a dictionary with state names"""
    return {"MAINMENU": main_menu.MainMenu, "MENU": "Menu", "TOWN": "Town",
        "SHOP": "Shop"}
