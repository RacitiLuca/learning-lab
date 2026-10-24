import pygame

pygame.init()

pygame.display.set_caption("1VS1")
icon = pygame.image.load("spaceship_red.png")
pygame.display.set_icon(icon)

LARGHEZZA, LUNGHEZZA = 900, 500
LARG_NAV, LUNG_NAV = 55, 40
BORDO = pygame.Rect(LARGHEZZA//2 - 5, 0, 10, LUNGHEZZA)

SCHERMO = pygame.display.set_mode((LARGHEZZA, LUNGHEZZA))
FPS = 50

NERO = (0, 0, 0)

SFONDO = pygame.transform.scale(pygame.image.load("space.png"), (LARGHEZZA, LUNGHEZZA))

NAVICELLA_GIALLA_FOTO = pygame.image.load("spaceship_yellow.png")
NAVICELLA_GIALLA = pygame.transform.rotate(pygame.transform.scale(
    NAVICELLA_GIALLA_FOTO, (LARG_NAV, LUNG_NAV)), 270)

NAVICELLA_ROSSA_FOTO = pygame.image.load("spaceship_red.png")
NAVICELLA_ROSSA = pygame.transform.rotate(pygame.transform.scale(
    NAVICELLA_ROSSA_FOTO, (LARG_NAV, LUNG_NAV)), 90)


def disegna():
    SCHERMO.blit(SFONDO, (0, 0))
    SCHERMO.blit(NAVICELLA_ROSSA, (ROSSO_X, ROSSO_Y))
    SCHERMO.blit(NAVICELLA_GIALLA, (GIALLO_X, GIALLO_Y))
    pygame.draw.rect(SCHERMO, NERO, BORDO)


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


def inizializza():
    global GIALLO_X, GIALLO_Y, ROSSO_X, ROSSO_Y
    global VEL_AVANZ
    GIALLO_X, GIALLO_Y = 700, 100
    ROSSO_X, ROSSO_Y = 100, 100
    VEL_AVANZ = 10


inizializza()

run = True
while run:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_l] and GIALLO_Y < 450:
            GIALLO_Y += VEL_AVANZ
        if keys[pygame.K_o] and GIALLO_Y > 0:
            GIALLO_Y -= VEL_AVANZ
        if keys[pygame.K_m] and GIALLO_X < 860:
            GIALLO_X += VEL_AVANZ
        if keys[pygame.K_k] and GIALLO_X > 450:
            GIALLO_X -= VEL_AVANZ

        if keys[pygame.K_s] and ROSSO_Y < 450:
            ROSSO_Y += VEL_AVANZ
        if keys[pygame.K_z] and ROSSO_Y > 0:
            ROSSO_Y -= VEL_AVANZ
        if keys[pygame.K_d] and ROSSO_X < 410:
            ROSSO_X += VEL_AVANZ
        if keys[pygame.K_q] and ROSSO_X > 0:
            ROSSO_X -= VEL_AVANZ
    disegna()
    aggiorna()

pygame.quit()