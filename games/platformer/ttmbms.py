import pygame

pygame.init()

LARGHEZZA, LUNGHEZZA = 500, 480

SCHERMO = pygame.display.set_mode((LARGHEZZA, LUNGHEZZA))
pygame.display.set_caption("ttmbms")
icona = pygame.image.load("standing.png")
pygame.display.set_icon(icona)

PERSONAGGIO = pygame.image.load("standing.png")
SFONDO = pygame.image.load("bg.jpg")

x = 50
y = 400

VELOCITA = 10
FPS = 30


def disegna():
    SCHERMO.blit(SFONDO, (0, 0))
    SCHERMO.blit(PERSONAGGIO, (x, y))


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


run = True
while run:
    pygame.time.delay(0)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_LEFT] and x + 20 > VELOCITA:
            x -= VELOCITA
        elif keys[pygame.K_RIGHT] and x < 450:
            x += VELOCITA
    aggiorna()
    disegna()

pygame.display.quit()