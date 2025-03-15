import pygame 
from pygame import *

"""Constantes du jeu"""""

# Window setup
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('Corn Ninja')

MAX_CORN_ON_SCREEN = 3  # Define the maximum number of corn on screen
BOMB_SPAWN_THRESHOLD = 10  # Corn count before a bomb spawns

# Load images
BACKGROUND_MAIN_MENU = image.load('assets/img/background_main_menu.jpg').convert()
BACKGROUND_PLAY = image.load('assets/img/background_play.png').convert()
BOX = image.load('assets/img/bucket.png').convert_alpha()
CORN_YELLOW = image.load('assets/img/corn_yellow.png').convert_alpha()
CORN_RED = image.load('assets/img/corn_red.png').convert_alpha()
CORN_BLUE = image.load('assets/img/corn_blue.png').convert_alpha()
CORN_GREEN = image.load('assets/img/corn_green.png').convert_alpha()
POPCORN_YELLOW1 = image.load('assets/img/popcorn_yellow1.png').convert_alpha()
POPCORN_YELLOW2 = image.load('assets/img/popcorn_yellow2.png').convert_alpha()
POPCORN_YELLOW3 = image.load('assets/img/popcorn_yellow3.png').convert_alpha()
POPCORN_RED1 = image.load('assets/img/popcorn_red1.png').convert_alpha()
POPCORN_RED2 = image.load('assets/img/popcorn_red2.png').convert_alpha()
POPCORN_RED3 = image.load('assets/img/popcorn_red3.png').convert_alpha()
POPCORN_BLUE1 = image.load('assets/img/popcorn_blue1.png').convert_alpha()
POPCORN_BLUE2 = image.load('assets/img/popcorn_blue2.png').convert_alpha()
POPCORN_BLUE3 = image.load('assets/img/popcorn_blue3.png').convert_alpha()
POPCORN_GREEN1 = image.load('assets/img/popcorn_green1.png').convert_alpha()
POPCORN_GREEN2 = image.load('assets/img/popcorn_green2.png').convert_alpha()
POPCORN_GREEN3 = image.load('assets/img/popcorn_green3.png').convert_alpha()
BOMB = image.load('assets/img/bomb.png').convert_alpha()
BOMB_BIG = image.load('assets/img/bomb_big.png').convert_alpha()
ICE = image.load('assets/img/icy.png').convert_alpha()
LIFE = image.load('assets/img/life.png').convert_alpha()
BUTTON_PLAY = image.load('assets/img/button_play.png').convert_alpha()
BUTTON_LANG = image.load('assets/img/button_lang.png').convert_alpha()
BUTTON_EASY = image.load('assets/img/button_easy.png').convert_alpha()
BUTTON_HARD = image.load('assets/img/button_hard.png').convert_alpha()
BOMBED = image.load('assets/img/bombed.png').convert_alpha()
ICED = image.load('assets/img/iced.png').convert_alpha()
SPAIN = image.load('assets/img/spain.png').convert_alpha()
FRENCH = image.load('assets/img/french.png').convert_alpha()
ENGLISH = image.load('assets/img/english.png').convert_alpha()
NOTIF_ICE = image.load('assets/img/notif_ice.png').convert_alpha()
GAME_OVER = image.load('assets/img/gameover.png').convert_alpha()

# Resize images if necessary
BACKGROUND_MAIN_MENU = transform.scale(BACKGROUND_MAIN_MENU, (WINDOW_WIDTH, WINDOW_HEIGHT))
BACKGROUND_PLAY = transform.scale(BACKGROUND_PLAY, (WINDOW_WIDTH, WINDOW_HEIGHT))
BOX = transform.scale(BOX, (110, 110))
CORN_YELLOW = transform.scale(CORN_YELLOW, (50, 51))
CORN_RED = transform.scale(CORN_RED, (50, 51))
CORN_BLUE = transform.scale(CORN_BLUE, (50, 51))
CORN_GREEN = transform.scale(CORN_GREEN, (50, 51))
POPCORN_YELLOW1 = transform.scale(POPCORN_YELLOW1, (50, 51))
POPCORN_YELLOW2 = transform.scale(POPCORN_YELLOW2, (50, 51))
POPCORN_YELLOW3 = transform.scale(POPCORN_YELLOW3, (50, 51))
POPCORN_RED1 = transform.scale(POPCORN_RED1, (50, 51))
POPCORN_RED2 = transform.scale(POPCORN_RED2, (50, 51))
POPCORN_RED3 = transform.scale(POPCORN_RED3, (50, 51))
POPCORN_BLUE1 = transform.scale(POPCORN_BLUE1, (50, 51))
POPCORN_BLUE2 = transform.scale(POPCORN_BLUE2, (50, 51))
POPCORN_BLUE3 = transform.scale(POPCORN_BLUE3, (50, 51))
POPCORN_GREEN1 = transform.scale(POPCORN_GREEN1, (50, 51))
POPCORN_GREEN2 = transform.scale(POPCORN_GREEN2, (50, 51))
POPCORN_GREEN3 = transform.scale(POPCORN_GREEN3, (50, 51))
BOMB = transform.scale(BOMB, (75, 60))
BOMB_BIG = transform.scale(BOMB_BIG, (747, 600))
ICE = transform.scale(ICE, (100, 100))
LIFE = transform.scale(LIFE, (59, 50))
BUTTON_PLAY = transform.scale(BUTTON_PLAY, (70, 70))
BUTTON_LANG = transform.scale(BUTTON_LANG, (70, 70))
BUTTON_EASY = transform.scale(BUTTON_EASY, (200,60) )
BUTTON_HARD = transform.scale(BUTTON_HARD, (200,60))
SPAIN = transform.scale(SPAIN, (75, 55))
FRENCH = transform.scale(FRENCH, (52, 52))
ENGLISH = transform.scale(ENGLISH, (65, 65))
NOTIF_ICE = transform.scale(NOTIF_ICE, (100, 100))


# Max corn on screen (easy mode)
MAX_CORN = 3

# Special object speeds
SPECIAL_OBJECT_SPEED = 2

# Parabolic motion parameters
GRAVITY = 0.3  # Strength of gravity (affects the curve)
SLOW_VELOCITY = 0.2