import pygame


Width = 800
Height = 800

running = True

CLOCK = pygame.time.Clock()

BLUE = (100,100,100)

speed = 5

red  = (255,0,0)
green = (0,255,0)


screen = pygame.display.set_mode((Width, Height))

spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()


cooldown = 500  #in milliseconds

alien_cooldown = 1000 #This is bullet cooldown in milliseconds
last_alien_shot = pygame.time.get_ticks()


CLOCK = pygame.time.Clock()
running = True

rows = 3
cols = 5

fps = 60

explosion_speed = 3


BLACK = 0,0,0