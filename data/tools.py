"""Contains the Control and State class. Control maintains
the event and program loops, and contains the current state,
while the State class to be inherited by all states"""

import pygame as py
from . import constants as c


class Control(object):

    """Maintains the event and program loops. Handles the current
    state."""

    def __init__(self, title):
        """Initializes the pbject"""

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
        self.state_dict = None

    def event_loop(self):
        """Event loop, handles quit and key presses"""
        for event in py.event.get():
            if event.type == py.QUIT:
                self.done = True
            elif event.type == py.KEYDOWN:
                self.keys = py.key.get_pressed()
                self.key_down = py.key.name(event.key)
            elif event.type == py.KEYUP:
                self.key_down = 0

    def update(self):
        """Updates time and pushes event to state"""

        self.current_time = py.time.get_ticks()
        self.state.get_event(self.key_down)

    def setup_state(self, state_dict):
        """Sets up state_dict"""
        self.state_dict = state_dict

    def set_state(self, state):
        """Sets a state based on the state parameter"""
        if state in c.STATES:
            self.state = self.state_dict[state]()
        else:
            print("Invalid state")

    def main(self):
        """Contains main program loop"""

        while not self.done:
            self.event_loop()

            self.update()
            py.display.update()

            self.clock.tick(self.fps)

class State(object):

    """Class to inherited of all states, maintains time and state dict"""

    def __init__(self, state, state_dict):
        self.state_dict = state_dict
        self.set_state(state)

    def get_state(self):
        """Returns state"""
        # return self.state
        pass

    def set_state(self):
        """Dummy function"""
        pass
