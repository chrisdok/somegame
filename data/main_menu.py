import pygame as py


class MainMenu(object):
	
	choices = ["Load Game", "New Game", "Options", "Exit"]
	selected = 0
	font = py.font.SysFont('Calibri', 25, True, False)
	
	def __init__(self):
		draw()

	def draw(self, direction = 0):
		screen.FILL(BLACK)
		for i, choice in enumerate(choices):
			text = font.render("My text", True, BLACK)
		