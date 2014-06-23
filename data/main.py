from data import main_menu
from . import setup, tools
from . import constants as c

def main():
	runtime = tools.Control("yo", c.MAINMENU)
	runtime.setup_state(build_dict())
	runtime.main()


def build_dict():
	return {"MAINMENU": main_menu.MainMenu, "MENU": "Menu", "TOWN": "Town", "SHOP": "Shop"}