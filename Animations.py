import pygame
from pygame.locals import *
from Settings import *


#creating the Explosion Class
class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f"Assets/EXPO{num}.png")
            if size == 1:
                img = pygame.transform.scale(img,(20,20))
            if size == 2:
                img = pygame.transform.scale(img,(40,40))
            if size == 3:
                img = pygame.transform.scale(img,(160,160))
            #ADD IMAGE TO THE LIST
            self.images.append(img)
        
        self.Index = 0
        self.image = self.images[self.Index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0


    def update(self):
        self.explosion_speed = explosion_speed

        #Updating the explosion animation
        self.counter += 1
        if self.counter >= self.explosion_speed and self.Index < len(self.images) - 1:
            self.counter = 0
            self.Index += 1
            self.image = self.images[self.Index]
        
        #Once the animation is complete, the animation will be deleted
        if self.Index >= len(self.images) -1 and self.counter >= explosion_speed:
            self.kill()


        