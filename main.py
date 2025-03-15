# main.py
import pygame
from pygame import *
from random import randint
from functions.menu import draw_main_menu, draw_level_menu, draw_language_menu
from functions.launcher import *
from functions.button_events import *
from module.constant import *


def main():
    pygame.init()
    pygame.mixer.init()

    cinema_sound = pygame.mixer.Sound('assets/snd/cinema.wav')
    game_music = 'assets/snd/music.wav'
    rooster_snd = pygame.mixer.Sound('assets/snd/rooster.mp3')


    font = pygame.font.Font(None, 60)
    font.set_bold(True)
    life_font = pygame.font.Font(None, 36)

    running = True
    state = 0
    clock = time.Clock()
    cinema_on = False
    music_on = False
    bomb_countdown = None
    bomb_triggered = False
    game_over = False

    objects = []
    special_objects_easy = []
    corn_count = 0
    score = 0

    cinema_sound.play(-1)
    cinema_on = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        state = button_events(state, mouse_pos)

        if state == 0:
            draw_main_menu(WINDOW, BACKGROUND_MAIN_MENU, BUTTON_PLAY, BUTTON_LANG)
            if not cinema_on:
                pygame.mixer.music.stop()
                cinema_sound.play(-1)
                cinema_on = True
                music_on = False

        elif state == 1:
            draw_level_menu(WINDOW, BACKGROUND_MAIN_MENU, BUTTON_EASY, BUTTON_HARD)
            if not cinema_on:
                pygame.mixer.music.stop()
                cinema_sound.play(-1)
                cinema_on = True
                music_on = False

        elif state == 2:
            draw_language_menu(WINDOW, BACKGROUND_MAIN_MENU)
            if not cinema_on:
                pygame.mixer.music.stop()
                cinema_sound.play(-1)
                cinema_on = True
                music_on = False

        elif state == 3:
            if not game_over:
                keys = pygame.key.get_pressed()
                corn_count = transform_corn_to_popcorn(objects, keys, corn_count, score)
                score = corn_count[1]
                corn_count = corn_count[0]
                handle_bomb_spawn(special_objects_easy, corn_count)
                
                draw_game(WINDOW, BACKGROUND_PLAY,
                        BOX,
                        objects, special_objects_easy,
                        font, score,
                        CORN_YELLOW, CORN_RED, CORN_BLUE, CORN_GREEN,
                        POPCORN_YELLOW1, POPCORN_YELLOW2, POPCORN_YELLOW3,
                        POPCORN_RED1, POPCORN_RED2, POPCORN_RED3,
                        POPCORN_BLUE1, POPCORN_BLUE2, POPCORN_BLUE3,
                        POPCORN_GREEN1, POPCORN_GREEN2, POPCORN_GREEN3,
                        BOMB, ICE,
                        life_font,
                        WINDOW_WIDTH, WINDOW_HEIGHT)
                pygame.display.flip()
                
                if not music_on:
                    cinema_sound.stop()
                    pygame.mixer.music.load(game_music)
                    pygame.mixer.music.play(-1)
                    cinema_on = False
                    music_on = True

                if randint(0, 200) < 2:
                    spawn_corn(WINDOW_HEIGHT, objects)
                if randint(0, 200) < 3 and any(obj["type"].startswith("CORN") for obj in objects):
                    spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy)

                for obj in special_objects_easy[:]:
                    if obj["type"] == "BOMB":
                        if keys[pygame.key.key_code(obj["letter"])]:
                            special_objects_easy.remove(obj)
                            rooster_snd.play()
                        elif obj["y"] > WINDOW_HEIGHT:
                            game_over = True
                            break
                    elif obj["type"] == "ICE":
                        if obj["y"] > WINDOW_HEIGHT:
                            special_objects_easy.remove(obj)
                        elif keys[pygame.key.key_code(obj["letter"])]:
                            freeze_objects(WINDOW, ICED, NOTIF_ICE, 5, objects, special_objects_easy, icecube_snd)
                            special_objects_easy.remove(obj)

            else:
                WINDOW.blit(BOMB_BIG, (0, 0))
                WINDOW.blit(BOMBED, (0,0))
                chicken_snd.play()
                score_text = font.render(f"SCORE = {score}", True, (255,0,0))
                WINDOW.blit(GAME_OVER, (300,300))
                WINDOW.blit(score_text, (300,520))
                pygame.display.flip()
                pygame.time.delay(5000)
                state = 0
                game_over = False
                objects.clear()
                special_objects_easy.clear()
                score = 0
                lives = 5
                

        elif state == 4 :
            if not game_over:
                keys = pygame.key.get_pressed()
                corn_count = transform_corn_to_popcorn(objects, keys, corn_count, score)
                score = corn_count[1]
                corn_count = corn_count[0]
                handle_bomb_spawn(special_objects_easy, corn_count)
                
                draw_game(WINDOW, BACKGROUND_PLAY,
                        BOX,
                        objects, special_objects_easy,
                        font, score,
                        CORN_YELLOW, CORN_RED, CORN_BLUE, CORN_GREEN,
                        POPCORN_YELLOW1, POPCORN_YELLOW2, POPCORN_YELLOW3,
                        POPCORN_RED1, POPCORN_RED2, POPCORN_RED3,
                        POPCORN_BLUE1, POPCORN_BLUE2, POPCORN_BLUE3,
                        POPCORN_GREEN1, POPCORN_GREEN2, POPCORN_GREEN3,
                        BOMB, ICE,
                        life_font,
                        WINDOW_WIDTH, WINDOW_HEIGHT)
                pygame.display.flip()
                
                if not music_on:
                    cinema_sound.stop()
                    pygame.mixer.music.load(game_music)
                    pygame.mixer.music.play(-1)
                    cinema_on = False
                    music_on = True

                if randint(0, 100) < 1:
                    spawn_corn(WINDOW_HEIGHT, objects)
                if randint(0, 100) < 2 and any(obj["type"].startswith("CORN") for obj in objects):
                    spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy)

                for obj in special_objects_easy[:]:
                    if obj["type"] == "BOMB":
                        if keys[pygame.key.key_code(obj["letter"])]:
                            special_objects_easy.remove(obj)
                            rooster_snd.play()
                        elif obj["y"] > WINDOW_HEIGHT:
                            game_over = True
                            break
                    elif obj["type"] == "ICE":
                        if obj["y"] > WINDOW_HEIGHT:
                            special_objects_easy.remove(obj)
                        elif keys[pygame.key.key_code(obj["letter"])]:
                            freeze_objects(WINDOW, ICED, NOTIF_ICE, 5, objects, special_objects_easy, icecube_snd)
                            special_objects_easy.remove(obj)

            else:
                WINDOW.blit(BOMB_BIG, (0, 0))
                WINDOW.blit(BOMBED, (0,0))
                chicken_snd.play()
                score_text = font.render(f"SCORE = {score}", True, (255,0,0))
                WINDOW.blit(GAME_OVER, (300,300))
                WINDOW.blit(score_text, (300,520))
                pygame.display.flip()
                pygame.time.delay(5000)
                state = 0
                game_over = False
                objects.clear()
                special_objects_easy.clear()
                score = 0
                lives = 5


        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()