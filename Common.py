import pygame
from Settings import *
from Aliens import *
from SpaceShip import *

class set():
    def __init__(self):
        pass
    
    def create_alien(self):
        for row in range(rows):
            for item in range(cols):
                alien = aliens(100 + item * 150, 100 + row * 70)
                alien_group.add(alien)
se = set()

spacez = Spaceship(int(Width/2), Height - 80, 3)