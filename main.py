import pygame

from clases import Grilla

ANCHO = 1280
ALTO = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (62, 70, 72)

TICK = 130
DELAY = 30
BLOCK = 16
if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(size=(ANCHO, ALTO))
    pygame.display.set_caption("Juego de la vida")
    clock = pygame.time.Clock()

    screen.fill(BLACK)

    grilla = Grilla(ANCHO//BLOCK, ALTO//BLOCK)

    preparando = True
    jugando = True

    while preparando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                preparando = False
                jugando = False
        clock.tick(TICK)
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            posicionx = pos[0]//BLOCK
            posiciony = pos[1]//BLOCK
            grilla.matriz[posiciony][posicionx].viva = True

        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            posicionx = pos[0] // BLOCK
            posiciony = pos[1] // BLOCK
            grilla.matriz[posiciony][posicionx].viva = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            preparando = False

        for posx in range(grilla.columnas):
            for posy in range(grilla.filas):
                if grilla.matriz[posy][posx].viva:
                    pygame.draw.rect(screen,
                                     WHITE,
                                     [posx*BLOCK, posy*BLOCK, BLOCK, BLOCK])
                else:
                    pygame.draw.rect(screen,
                                     GREY,
                                     [posx*BLOCK, posy*BLOCK, BLOCK, BLOCK])
                pygame.draw.rect(screen,
                                 BLACK,
                                 [posx * BLOCK, posy * BLOCK, BLOCK, BLOCK], 1)

        pygame.time.delay(DELAY)
        pygame.display.flip()

    while jugando:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            DELAY -= 5
        if keys[pygame.K_n]:
            DELAY += 5
        clock.tick(TICK)

        for posx in range(grilla.columnas):
            for posy in range(grilla.filas):
                if grilla.matriz[posy][posx].intentar_revivir():
                    pygame.draw.rect(screen,
                                     WHITE,
                                     [posx*BLOCK, posy*BLOCK, BLOCK, BLOCK])
                else:
                    pygame.draw.rect(screen,
                                     GREY,
                                     [posx*BLOCK, posy*BLOCK, BLOCK, BLOCK])
                pygame.draw.rect(screen,
                                 BLACK,
                                 [posx * BLOCK, posy * BLOCK, BLOCK, BLOCK], 1)
        grilla.convertir()

        pygame.time.delay(DELAY)
        pygame.display.flip()
