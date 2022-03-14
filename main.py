
import pygame, sys

import pygame_menu
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((1380, 710))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")
BG = pygame.transform.scale(BG, (1380, 710))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#Level Screen
def level():
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Light Blue")

        LEVEL_TEXT = get_font(45).render("This is the level screen.", True, "Red")
        LEVEL_RECT = LEVEL_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEVEL_TEXT, LEVEL_RECT)

        LEVEL_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        LEVEL_BACK.changeColor(LEVEL_MOUSE_POS)
        LEVEL_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_BACK.checkForInput(LEVEL_MOUSE_POS):
                    play()

        pygame.display.update()

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("Light Green")

    
        PLAY_BACK = Button(image=None, pos=(640, 560), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="BLACK")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        pygame.display.update()
#options
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Supply Mission", True, "#b68f40")
        
        MENU_RECT = MENU_TEXT.get_rect(center=(840, 100))

        PLAY_BUTTON = Button(image= None, pos=(970, 250), 
                            text_input="LEVEL", font=get_font(40), base_color="#BFEFFF", hovering_color="Green")
        OPTIONS_BUTTON = Button(image= None, pos=(970, 400), 
                            text_input="OPTIONS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image= None, pos=(970, 550), 
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()