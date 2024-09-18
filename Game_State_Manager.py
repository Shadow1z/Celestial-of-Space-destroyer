import pygame
from Settings import *


class GameStateManager:
    def __init__(self):
        self.state = "menu"  # Start in the menu

    def change_state(self, new_state):
        self.state = new_state