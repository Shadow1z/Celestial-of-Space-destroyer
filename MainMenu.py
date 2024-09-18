import pygame
from Game_State_Manager import *
from Game import *
from Settings import *
from button import *
from Game_State_Manager import GameStateManager

class main():
    def __init__(self,game_state_manager):
        self.screen = screen

        self.Main_bg = pygame.image.load("Assets/MainMenu-BG.png")
        self.Main_bg = pygame.transform.scale(self.Main_bg, (Width, Height))
        start_btn = pygame.image.load("Assets/Start_BTN.png")
        start_btn = pygame.transform.scale(start_btn,(200,100))
        exit_btn = pygame.image.load("Assets/Exit_BTN.png")
        exit_btn = pygame.transform.scale(exit_btn,(200,100))

        self.game_state_manager = game_state_manager


        self.button1 = Button(start_btn, (400, Height/2))
        self.button2 = Button(exit_btn, (400, (Height/2 + 110)))

        self.buttons = [self.button1, self.button2]



    def handle_event(self,events):
        for event in events:
            if event.type == QUIT:
                    pygame.quit()
                    exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
            if self.button1.is_clicked(event):
                self.game_state_manager.change_state("playing")
            if self.button2.is_clicked(event):
                pygame.quit()

    def render(self,screen):
            screen.blit(self.Main_bg, (0,0))
            for button in self.buttons:
                button.draw(screen)
            


   
        
        
