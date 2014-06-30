import pygame as py
from . import constants as c

class Control(object): 

	def __init__(self, title, state):
		self.screen = py.display.get_surface()
		self.done = False
		self.clock = py.time.Clock()
		self.title = title
		self.fps = 60
		self.keys = py.key.get_pressed()
		self.current_time = 0
		self.event = 0
		self.key_down = 0	
		self.state = 0	

	def event_loop(self):
		for event in py.event.get():
			if event.type == py.QUIT:
				self.done = True
			elif event.type == py.KEYDOWN:
				self.keys = py.key.get_pressed()
				self.key_down = py.key.name(event.key)
			elif event.type == py.KEYUP:
				self.key_down = 0

	def update(self):
		self.current_time = py.time.get_ticks()
		self.state.get_event(self.key_down)

	def setup_state(self, state_dict):
		self.state_dict = state_dict

	def set_state(self, state):
		if state in c.STATES:
			self.state = self.state_dict[state]()
		else:
			print("Invalid state")

	def main(self):

		while not self.done:
			self.event_loop()

			self.update()
			py.display.update()

			self.clock.tick(self.fps)

	def yo(self):
		print("test")

class State(object):

	def __init__(self, state, state_dict):
		self.state_dict = state_dict
		self.set_state(state)
	
	def get_state(self):
		return self.state



