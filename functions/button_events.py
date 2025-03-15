import pygame
from pygame.locals import *

def button_events(state, mouse_pos):
    """Gère les événements clavier et souris, retourne le nouvel état."""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                state = 0  # Retour au menu principal
            if event.key == K_p:  # Touche 'P' pour jouer
                if state == 0:  # Menu principal
                    state = 1  # Aller au menu des niveaux
            if event.key == K_l:  # Touche 'L' pour changer la langue
                if state == 0:  # Menu principal
                    state = 2  # Aller au menu des langues
            if event.key == K_e:  # Touche 'E' pour jouer en mode Easy
                if state == 1:  # Menu de difficulté
                    state = 3  # Démarrer en mode Easy
            if event.key == K_h:  # Touche 'E' pour jouer en mode Easy
                if state == 1:  # Menu de difficulté
                    state = 4  # Démarrer en mode Easy

                    
        if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            if state == 0:  # Menu principal
                play_button_rect = pygame.Rect(90, 430, 70, 70)
                lang_button_rect = pygame.Rect(90, 510, 70, 70)

                if play_button_rect.collidepoint(mouse_pos):
                    state = 1  # Aller au menu des niveaux

                if lang_button_rect.collidepoint(mouse_pos):
                    state = 2  # Aller au menu des langues

            elif state == 1:  # Menu de difficulté
                BUTTON_EASY_rect = pygame.Rect(90, 430, 100, 50)
                BUTTON_HARD_rect = pygame.Rect(90, 510, 100, 50)

                if BUTTON_EASY_rect.collidepoint(mouse_pos):
                    state = 3  # Démarrer en mode Easy

                if BUTTON_HARD_rect.collidepoint(mouse_pos):
                    state = 4  # Mode Hard 

            elif state == 2:  # Menu des langues
                english_button_rect = pygame.Rect(90, 430, 100, 50)
                french_button_rect = pygame.Rect(90, 480, 100, 50)
                spanish_button_rect = pygame.Rect(90, 530, 100, 50)

                if english_button_rect.collidepoint(mouse_pos):
                    pass  # Implémentation future
                if french_button_rect.collidepoint(mouse_pos):
                    pass  # Implémentation future
                if spanish_button_rect.collidepoint(mouse_pos):
                    pass  # Implémentation future

    return state  # Si aucun changement d’état