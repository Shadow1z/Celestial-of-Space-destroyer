import pygame
from pygame.locals import *
from Settings import *
from Bullets import *
from Animations import *
from Sound_Effects import *


class Spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y,health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/tiny_ship17.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.heatlh_start = health
        self.health_remaining = health
        self.shot_last = pygame.time.get_ticks()

    def update(self):

        self.speed = 10
        self.vertical_speed = 4

        #setting a cooldonw variable
        self.cooldown = cooldown 

        #Getting Key press
        key = pygame.key.get_pressed()

        #Moveming Spaceship
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.right < Width:
            self.rect.x += self.speed
        
        #get the current time
        now_time = pygame.time.get_ticks()


        #shooting bullet
        if key[pygame.K_SPACE] and now_time - self.shot_last > self.cooldown:
             bullet = bullets(self.rect.centerx, self.rect.top)
             lasershot_fx.play()
             bullet_group.add(bullet)
             self.shot_last = now_time


        #creating a mask
        self.mask = pygame.mask.from_surface(self.image)

        #Drawing the health bar, red and green
        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0: 
                pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.heatlh_start)), 15))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)#
            self.kill()



        

  


    