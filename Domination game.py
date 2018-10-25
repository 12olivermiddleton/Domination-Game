# Programming Project - Domination
# By Oliver Middleton

import pygame
import time

class Colour():
    red = pygame.Color(255,0,0)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0, 153, 255)
    darkBlue = pygame.Color(0, 51, 102)
    white = pygame.Color(255,255,255)
    aqua = pygame.Color(0,255,255)
    black = pygame.Color(0,0,0)
    pink = pygame.Color(255,200,200)

class Menu():
    def __init__(self):

        self.buttonList = []
        self.display_width = 600
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Menu')
        self.gameDisplay.fill(Colour.white)

        

        myfont = pygame.font.SysFont("Comic Sans MS", 60)
        textsurface = myfont.render("Domination", False, Colour.black)
        self.gameDisplay.blit(textsurface, (110,50))

        
        x = 120
        y = 220
        for i in range(3):
            self.buttonList.append(Button(x,y, self.gameDisplay))
            y = y + 100
       


class Button():
    def __init__(self, x, y, gameDisplay):
        self.initialColour = Colour.darkBlue
        self.newColour = Colour.red
        self.x = x
        self.y = y
        self.width = 330
        self.height = 75
        pygame.draw.rect(gameDisplay, self.initialColour, (self.x,self.y,self.width,self.height))

        mouse = pygame.mouse.get_pos()
        if 120+330 > mouse[0] >120 and 220+75 > mouse[1] > 22:
            pygame.draw.rect(gameDisplay, self.newColour, (self.x,self.y,self.width,self.height))
        
        pygame.display.update()

##        if 
##        #print(mouse)
##
##        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
##            pygame.draw.rect(gameDisplay, Colour.blue,(150,450,100,50))
##        else:
##            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
##        pygame.draw.rect(gameDisplay, red,(550,450,100,50))
##        pygame.display.update()
##        clock.tick(15)



class Board():
    def __init__(self):
        self.display_width = 491
        self.display_height = 941
        self.DisplayMap()
        
       
    def DisplayMap(self):

        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')

        clock = pygame.time.Clock()
        crashed = False
        mapImg = pygame.image.load('GOT map.JPG')


        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)

        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            gameDisplay.fill(Colour.white)
            gameDisplay.blit(mapImg, (0, 0))

            pygame.display.update()
            clock.tick(60)

    #pygame.quit()
    #quit()


if __name__ == "__main__":
    
    pygame.init()

    menu = Menu()
    #board = Board()
    clock = pygame.time.Clock()

    pygame.display.update()
    clock.tick(60)
    
