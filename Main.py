import pygame
from MainMenu import main
from Game import game, PauseMenu
from Game_State_Manager import GameStateManager
from Settings import *

def menu():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    clock = pygame.time.Clock()

    game_state_manager = GameStateManager()
    menu = main(game_state_manager)
    Game = game(game_state_manager)
    pause_menu = PauseMenu(game_state_manager)

    while True:
        events = pygame.event.get()

        if game_state_manager.state == "menu":
            menu.handle_event(events)
            menu.render(screen)
        elif game_state_manager.state == "playing":
            Game.handle_event(events)
            Game.render(screen)
        elif game_state_manager.state == "paused":
            pause_menu.handle_events(events)
            pause_menu.render(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    menu()