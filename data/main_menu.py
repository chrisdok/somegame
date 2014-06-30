import pygame as py
import time
from . import constants as c
from data import tools

class MainMenu(tools.State):
	
	choices = ["New Game", "Load Game", "Options", "Exit"]
	selected = 0
	current_button = 0	
	
	def __init__(self):
		self.allow = 1
		self.clock = py.time.Clock()
		self.last_time = 0
		self.font = py.font.SysFont('Calibri', 25, True, False)
		self.screen = py.display.get_surface()
		self.draw()

	def update(self):

		if time.time() - self.last_time < 0.25:
			self.allow = 0
		else:
			self.allow = 1
		print(self.allow)
		
	def draw(self):
		self.screen.fill(c.MENU_GRAY_BG)
		for i, choice in enumerate(self.choices):
			# text = self.font.render("My text", True, c.BLACK)
			self.screen.blit(self.make_button(choice, i == self.selected), (c.SCREEN_WIDTH/3, c.SCREEN_HEIGHT/(len(self.choices) + 1) * (i + 1)))

	def get_event(self, event = 0):
		self.update()
		if self.allow == 1:
			
			if (event in c.UP):
				self.set_choice(-1)
				self.current_button = event
			elif (event in c.DOWN):
				self.set_choice(1)

	def select(self):
		pass

	def set_choice(self, direction):
		if self.selected + direction < 0 or self.selected + direction >= len(self.choices):
			pass
			# print("Invalid choice")
		else: 
			self.selected += direction
			self.draw()
		self.last_time = time.time()

	# def set_event(self, event):
	# 	super(tools.State, self).set_event(event)


	def make_button(self, title, selected):
		print(selected)
		# Creates surface
		surface = py.Surface((int(c.SCREEN_WIDTH/3), int(c.SCREEN_WIDTH/len(self.choices)+1)))
		surface.fill(c.MENU_GRAY_BG)
		
		# Adds rect
		if selected:
			color = c.MENU_GRAY_BUTTONS_SELECTED
		else:
			color = c.MENU_GRAY_BUTTONS

		rect = py.draw.rect(surface, color, (0, 0, int(c.SCREEN_WIDTH/3), int((c.SCREEN_HEIGHT/len(self.choices) + 1) * 0.5)))

		# Adds text
		text = self.font.render(title, True, c.WHITE)
		surface.blit(text, (int((rect.width - text.get_width())/2), int((rect.height - text.get_height())/2)))
		return surface
		