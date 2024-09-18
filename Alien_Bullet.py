import pygame
from pygame.locals import *
from Settings import *
from SpaceShip import *
from Common import *
from Animations import *
from Sound_Effects import *


class alien_bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/Enemy-bullet-1.png")
        self.image = pygame.transform.rotate(self.image,90)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > Height:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            #Now we will reduce the spaceships health, each time it collides with alien's bullets
            self.kill()
            explosion_1_fx.play()
            spacez.health_remaining -= 1
            #Explosion Animation whenever alien bullet collides with spaceship
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)

