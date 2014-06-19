import pygame as py
from . import constants as c

class Control(object): 

	def __init__(self, title):
		self.screen = py.display.get_surface()
		self.done = False
		self.clock = py.time.Clock()
		self.title = title
		self.fps = 60
		self.keys = py.key.get_pressed()
		self.current_time = 0

	def event_loop(self):
		for event in py.event.get():
			if event.type == py.QUIT:
				self.done = True
			elif event.type == py.KEYDOWN:
				self.keys = py.key.get_pressed()
			elif event.type == py.KEYUP:
				self.keys = py.key.get_pressed()

	def update(self):
		self.current_time = py.time.get_ticks()


	def main(self):
		while not self.done:
			self.event_loop()
			self.update()
			py.display.update()
			self.clock.tick(self.fps)