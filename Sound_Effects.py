import pygame
from pygame import mixer


pygame.mixer.pre_init(44100,-16,2, 512)
mixer.init()

#defining each sound effects and setting their volume
explosion_1_fx = pygame.mixer.Sound("Assets/Explosion+3.wav")
explosion_1_fx.set_volume(0.25)

explosion_2_fx = pygame.mixer.Sound("Assets/Explosion+7.wav")
explosion_2_fx.set_volume(0.25)

lasershot_fx = pygame.mixer.Sound("Assets/Laser-shot.mp3")
lasershot_fx.set_volume(0.25)

Background_fx = pygame.mixer.Sound("Assets/Background-retro-music.mp3")
Background_fx.set_volume(0.01)

