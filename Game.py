import pygame
import random
from pygame import *
from SpaceShip import *
from Settings import *
from Bullets import *
from Aliens import *
from Common import *
from Alien_Bullet import *
from Sound_Effects import *
from Game_State_Manager import GameStateManager



pygame.init()





class game():
    def __init__(self,game_state_manager):
        self.screen = screen


        self.bg = pygame.image.load("Assets/Galaxy Background.png")
        self.bg = pygame.transform.scale(self.bg, (Width, Height))

        self.spaceship_group = spaceship_group
        self.spaceship = spacez
        self.spaceship_group.add(self.spaceship)

        self.bullet_group = bullet_group

        self.alien_group = alien_group 
        se.create_alien()


        self.last_alien_shot = pygame.time.get_ticks()

        self.explosion_group = explosion_group

        self.game_state_manager = game_state_manager
        self.paused = False

    def handle_event(self,events):
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Pause game on Esc
                        self.paused = not self.paused
                        if self.paused:
                            self.game_state_manager.change_state("paused")

            #This will create random alien bullets
            #Recording the current time
            now_time = pygame.time.get_ticks()
            #SHOOT
            if now_time - self.last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0 :
                attacking_alien = random.choice(alien_group.sprites())
                alien_bullet = alien_bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
                alien_bullet_group.add(alien_bullet)
                self.last_alien_shot = now_time

            

    def render(self,screen):
            self.screen.blit(self.bg, (0,0))
            Background_fx.play()
            self.spaceship.update()
            self.bullet_group.update()
            alien_group.update()
            alien_bullet_group.update()
            explosion_group.update()
            
            spaceship_group.draw(screen)
            self.bullet_group.draw(screen)
            alien_group.draw(screen)
            alien_bullet_group.draw(screen)
            explosion_group.draw(screen)
            
            pygame.display.update()
            CLOCK.tick(fps)

  
    

class PauseMenu:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Resume game
                    self.game_state_manager.change_state("playing")
                elif event.key == pygame.K_q:  # Quit to menu
                    self.game_state_manager.change_state("menu")

    def render(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 55)
        text = font.render('Paused - R to Resume, Q to Quit', True, (255, 255, 255))
        screen.blit(text, (50, 100))

def run():
    Game = game()
    Game.run()






