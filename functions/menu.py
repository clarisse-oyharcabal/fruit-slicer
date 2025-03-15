from pygame import *
from module.constant import * 

# Game functions
def draw_main_menu(window, background_main_menu, button_play, button_lang):
    window.blit(background_main_menu, (0, 0))
    button_lang
    button_lang 
    window.blit(button_play, (90, 430))
    window.blit(button_lang, (90, 510))

def draw_level_menu(window, background_main_menu, BUTTON_EASY, BUTTON_HARD):
    window.blit(background_main_menu, (0, 0))
    window.blit(BUTTON_EASY, (10, 440))
    window.blit(BUTTON_HARD, (10, 520))

def draw_language_menu(window, background_main_menu):
    window.blit(background_main_menu, (0, 0))
    font_button = font.SysFont('comicsansms', 26)
    window.blit(ENGLISH, (10, 490))
    window.blit(FRENCH, (84, 492))
    window.blit(SPAIN, (140, 492))