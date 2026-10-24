import pygame
import random

pygame.init()

pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("uccello.png")
pygame.display.set_icon(icon)

sfondo = pygame.image.load("sfondo.png")
ucello = pygame.image.load("uccello.png")
base = pygame.image.load("base.png")
gameover = pygame.image.load("gameover.png")
tubo_giu = pygame.image.load("tubo.png")
tubo_su = pygame.transform.flip(tubo_giu, False, True)

SCHERMO = pygame.display.set_mode((288, 512))
FPS = 50
VEL_AVANZ = 3


def disegna_ogetti():
    SCHERMO.blit(sfondo, (0, 0))
    SCHERMO.blit(ucello, (ucellox, ucelloy))
    SCHERMO.blit(base, (basex, 400))


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


def inizializza():
    global ucellox, ucelloy, ucello_vely
    global basex
    ucellox, ucelloy = 60, 150
    ucello_vely = 0
    basex = 0


def hai_perso():
    SCHERMO.blit(gameover, (50, 180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keys[pygame.K_r]:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()


inizializza()

run = True
while run:
    basex -= VEL_AVANZ
    if basex < -45:
        basex = 0
    ucello_vely += 1
    ucelloy += ucello_vely
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ucello_vely = -10
        if event.type == pygame.QUIT:
            run = False
    if ucelloy > 390:
        hai_perso()
    disegna_ogetti()
    aggiorna()

pygame.quit()