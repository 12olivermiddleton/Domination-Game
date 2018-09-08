# Programming Project - Domination
# By Oliver Middleton

import pygame

pygame.init()




def DisplayMap():

    display_width = 491
    display_height = 941

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Domination Game!')

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    mapImg = pygame.image.load('GOT map.JPG')


    def map(x, y):
        gameDisplay.blit(mapImg, (0, 0))


    x = (display_width * 0.45)
    y = (display_height * 0.8)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill(white)
        map(x, y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()



def Menu():
    display_width = 600
    display_height = 600

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Menu')

    gameDisplay.fill(white)
    map(x, y)

    pygame.display.update()
    clock.tick(60)

    pygame.quit()
    quit()





#Menu()
DisplayMap()
