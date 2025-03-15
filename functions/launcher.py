# launcher.py
import pygame
from pygame.locals import *
from pygame import *
from random import randint, choice
from module.constant import *
import time

pygame.mixer.init()
popcorn_snd = pygame.mixer.Sound('assets/snd/popcorn.mp3')
icecube_snd = pygame.mixer.Sound('assets/snd/icecube.mp3')
chicken_snd = pygame.mixer.Sound('assets/snd/chicken.mp3')
combo_snd = pygame.mixer.Sound('assets/snd/combo.mp3')
score = 0
lives = 5
combo_active = False
combo_start_time = 0
last_pop_time = 0

def draw_letter_above_object(WINDOW, font, obj):
    text = font.render(obj["letter"], True, (255, 255, 255))
    WINDOW.blit(text, (obj["x"] + 15, obj["y"] - 35))

def draw_game(
    WINDOW, BACKGROUND_PLAY,
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
    WINDOW_WIDTH, WINDOW_HEIGHT):
    
    global lives, state, combo_active, combo_start_time

    WINDOW.blit(BACKGROUND_PLAY, (0, 0))
    WINDOW.blit(BOX, (0,490))

    all_objects = objects + special_objects_easy

    to_remove = []
    failed_corns= []
    to_remove_specials= []

    for obj in all_objects:
        obj["x"] += obj["vx"]
        obj["y"] += obj["vy"]
        obj["vy"] += GRAVITY

        if obj["x"] < 0:
            obj["x"] = 0
        elif obj["x"] > WINDOW_WIDTH - 50:
            obj["x"] = WINDOW_WIDTH - 50

        if obj["y"] < 0:
            obj["y"] = 0

        # Si un corn tombe au sol, on l'ajoute à la liste des échecs et on décrémente les vies
        if obj["y"] > WINDOW_HEIGHT:
            if obj["type"].startswith("CORN"): # Vérifie si c'est un corn
                failed_corns.append(obj) # Ajouter à la liste des échecs
                

        if obj["type"] == "CORN_YELLOW":
            WINDOW.blit(CORN_YELLOW, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_RED":
            WINDOW.blit(CORN_RED, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_BLUE":
            WINDOW.blit(CORN_BLUE, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_GREEN":
            WINDOW.blit(CORN_GREEN, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_YELLOW1":
            WINDOW.blit(POPCORN_YELLOW1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_YELLOW2":
            WINDOW.blit(POPCORN_YELLOW2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_YELLOW3":
            WINDOW.blit(POPCORN_YELLOW3, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_RED1":
            WINDOW.blit(POPCORN_RED1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_RED2":
            WINDOW.blit(POPCORN_RED2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_RED3":
            WINDOW.blit(POPCORN_RED3, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_BLUE1":
            WINDOW.blit(POPCORN_BLUE1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_BLUE2":
            WINDOW.blit(POPCORN_BLUE2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_BLUE3":
            WINDOW.blit(POPCORN_BLUE3, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_GREEN1":
            WINDOW.blit(POPCORN_GREEN1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_GREEN2":
            WINDOW.blit(POPCORN_GREEN2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_GREEN3":
            WINDOW.blit(POPCORN_GREEN3, (obj["x"], obj["y"]))
        elif obj["type"] == "BOMB":
            WINDOW.blit(BOMB, (obj["x"], obj["y"]))
        elif obj["type"] == "ICE":
            WINDOW.blit(ICE, (obj["x"], obj["y"]))

        draw_letter_above_object(WINDOW, font, obj)

        if obj["x"] > WINDOW_WIDTH or obj["y"] > WINDOW_HEIGHT:
            to_remove.append(obj)

        if obj["x"] > WINDOW_WIDTH or obj["y"] > WINDOW_HEIGHT:
            to_remove_specials.append(obj)

     # Décrémenter les vies lorsque des corns tombent
    for obj in failed_corns:
        if obj in objects:
            objects.remove(obj)
            if lives > 1:
                lives -= 1
            else:
                # Afficher l'écran de Game Over
                WINDOW.blit(BOMB_BIG, (0, 0))
                WINDOW.blit(BOMBED, (0,0))
                chicken_snd.play()
                score_text = font.render(f"SCORE = {score}", True, (255,0,0))
                WINDOW.blit(GAME_OVER, (300,300))
                WINDOW.blit(score_text, (300,520))
                pygame.display.flip()

                # Attendre un peu avant de retourner au menu (3 secondes dans cet exemple)
                pygame.time.delay(3000)  # 3000 millisecondes = 3 secondes

                # Réinitialiser les variables du jeu pour revenir au menu
                state = 0  # Supposons que state = 0 correspond au menu principal
                score = 0
                lives = 5
                objects.clear()
                special_objects_easy.clear()
                return

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    WINDOW.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10, 10))
    
    life_x = WINDOW_WIDTH - LIFE.get_width() - 10  # Align with score
    life_y = 30 + score_text.get_height() # Below the score
    WINDOW.blit(LIFE, (life_x, life_y)) # Draw Life Image

    lives_text = life_font.render(str(lives), True, (255, 255, 255))
    text_x = life_x + LIFE.get_width() - 80
    WINDOW.blit(lives_text, (text_x, life_y + 10))
                

          # Afficher le message de combo si actif
    if combo_active:
        draw_combo_message(WINDOW, font)
        combo_snd.play()
        if time.time() - combo_start_time > 1.0:  # Le combo dure 1 seconde
            combo_active = False

def spawn_corn(WINDOW_HEIGHT, objects):
    if len([obj for obj in objects if obj["type"].startswith("CORN")]) < MAX_CORN:
        obj_type = choice(["CORN_YELLOW", "CORN_RED", "CORN_BLUE", "CORN_GREEN"])

        x = 0
        y = WINDOW_HEIGHT - 100
        if obj_type in ["CORN_YELLOW", "CORN_RED", "CORN_BLUE", "CORN_GREEN"]:
            vx = randint(5, 10)
            vy = randint(-20, -10)
        else:
            vx = randint(5, 10)
            vy = randint(-20, -10)

        letter = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        objects.append({
            "type": obj_type,
            "x": x, "y": y,
            "vx": vx, "vy": vy,
            "letter": letter
        })

def spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy):
    if len([obj for obj in special_objects_easy if obj["type"] == "BOMB"]) < 1:
        obj_type = choice(["BOMB", "ICE"])

        x = 0
        y = WINDOW_HEIGHT - 100

        if obj_type in ["BOMB", "ICE"]:
            vx = randint(3, 6)
            vy = randint(-20, -10)

        letter = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        special_objects_easy.append({
            "type": obj_type,
            "x": x, "y": y,
            "vx": vx, "vy": vy,
            "letter": letter
        })


def handle_bomb_spawn(special_objects_easy, corn_count):
    if corn_count >= 10:
        if not any(obj["type"] == "BOMB" for obj in special_objects_easy):
            spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy)
        corn_count = 0
        return


import pygame

def freeze_objects(window, ICED, NOTIF_ICE, duration, objects, special_objects_easy, icecube_snd):
    start_time = pygame.time.get_ticks()  # Récupère le temps actuel
    original_velocities = []

    # Mettre les vitesses à zéro et afficher ICED
    for obj in objects + special_objects_easy:
        original_velocities.append((obj["vx"], obj["vy"]))
        obj["vx"], obj["vy"] = 0, 0

    icecube_snd.play()

    # Afficher l'image de freeze
    window.blit(ICED, (100, 100))  # Ajuste la position si nécessaire
    window.blit(NOTIF_ICE, (1,0))
    pygame.display.update()

    # Attendre sans bloquer le programme
    while pygame.time.get_ticks() - start_time < duration * 1000:
        for event in pygame.event.get():  # Permet de ne pas bloquer Pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    # Restaurer les vitesses après le freeze
    for i, obj in enumerate(objects + special_objects_easy):
        obj["vx"], obj["vy"] = original_velocities[i]



def transform_corn_to_popcorn(objects, keys, corn_count, score):
    global last_pop_time, combo_active, combo_start_time

    
    popcorn_variants = {
        "CORN_YELLOW": ["POPCORN_YELLOW1", "POPCORN_YELLOW2", "POPCORN_YELLOW3"],
        "CORN_RED": ["POPCORN_RED1", "POPCORN_RED2", "POPCORN_RED3"],
        "CORN_BLUE": ["POPCORN_BLUE1", "POPCORN_BLUE2", "POPCORN_BLUE3"],
        "CORN_GREEN": ["POPCORN_GREEN1", "POPCORN_GREEN2", "POPCORN_GREEN3"]
    }

    current_time = time.time()

    for obj in objects:
        if obj["type"] in popcorn_variants and keys[pygame.key.key_code(obj["letter"])]:
            obj["type"] = choice(popcorn_variants[obj["type"]])
            corn_count += 1
            score += 1
            popcorn_snd.play()

 # Vérifier si un combo est possible
            if current_time - last_pop_time < 1.0:  # Moins d'une seconde depuis le dernier fruit
                if not combo_active:
                    combo_active = True
                    combo_start_time = current_time
                    score += 3  # Ajouter le bonus de combo
            else:
                combo_active = False

            last_pop_time = current_time

    return corn_count, score


def draw_combo_message(WINDOW, font):
    combo_text = font.render("Combo +3", True, (255, 215, 0))  # Couleur or
    text_rect = combo_text.get_rect(center=(WINDOW.get_width() // 2, WINDOW.get_height() // 2))
    WINDOW.blit(combo_text, text_rect)
