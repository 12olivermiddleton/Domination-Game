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
        textPosX = 130
        buttonTextNo = 0
        myfont = pygame.font.SysFont("Comic Sans MS", 40)
        for i in range(3):
            buttonTextNo = buttonTextNo + 1
            self.buttonList.append(Button(x,y, self.gameDisplay))

            if buttonTextNo == 1:
                textsurface = myfont.render("Play Game", False, Colour.white)
                self.gameDisplay.blit(textsurface, (textPosX,y))

            elif buttonTextNo == 2:
                textsurface = myfont.render("Load Game", False, Colour.white)
                self.gameDisplay.blit(textsurface, (textPosX,y))

            elif buttonTextNo == 3:
                textsurface = myfont.render("Instructions", False, Colour.white)
                self.gameDisplay.blit(textsurface, (textPosX,y))

            y = y + 100
            pygame.display.update()

    def getButtonList(self):
        return self.buttonList

class Instructions():
    def __init__(self):
        self.instructionsDisplay_width = 600
        self.instructionsDisplay_height = 700
        self.instructionsPanel()

    def instructionsPanel(self):
        gameDisplay = pygame.display.set_mode((self.instructionsDisplay_width, self.instructionsDisplay_height))
        pygame.display.set_caption('Instructions')
        gameDisplay.fill(Colour.white)

        #This is a test to see if the game display window works
        #pygame.draw.rect(gameDisplay, colour.red, (100,100,100,100))

class Button():
    def __init__(self, x, y, gameDisplay):
        self.initialColour = Colour.darkBlue
        self.x = x
        self.y = y
        self.width = 330
        self.height = 75


        pygame.draw.rect(gameDisplay, self.initialColour, (self.x,self.y,self.width,self.height))

        pygame.display.update()

class Board():
    def __init__(self):
        self.display_width = 491
        self.display_height = 941
        self.DisplayMap()

    def DisplayMap(self):

        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')

        clock = pygame.time.Clock()
        mapImg = pygame.image.load('GOT map.JPG')

        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)

        gameDisplay.fill(Colour.white)
        gameDisplay.blit(mapImg, (0, 0))





if __name__ == "__main__":

    pygame.init()
    colour = Colour()
    menu = Menu()
    #board = Board()
    clock = pygame.time.Clock()


    mouse = pygame.mouse.get_pos()
    print(mouse)


    crashed = False
    while not crashed:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttonMinX = 120
                buttonMaxX = 450
                buttonMinY = 220
                buttonMaxY = 295

                mouse = pygame.mouse.get_pos()
                print(mouse)
                ButtonFound = False
                ButtonNumber = 0
                ### sort out the button numbers, use iterative statements to define the button number// which botton was pressed
                while ButtonFound == False:

                    ButtonNumber = ButtonNumber + 1
                    if buttonMaxX > mouse[0] > buttonMinX and buttonMaxY > mouse[1] > buttonMinY:

                        pygame.draw.rect(menu.gameDisplay,colour.red, (buttonMinX, buttonMinY, 330,75))

                        pygame.display.update()

                        ButtonFound = True

##                        print(ButtonNumber)
##                        print("hello")

                        if ButtonNumber == 1:
                            pygame.quit()
                            board = Board()
                            pygame.display.update()

                        elif ButtonNumber == 2:
                            ### need to add in a load game function
                            pass

                        elif ButtonNumber == 3:
                            pygame.quit()
                            instructions = Instructions()
                            pygame.display.update()

                    else:
                        buttonMinY = buttonMinY + 100
                        buttonMaxY = buttonMaxY + 100



#pygame.draw.rect(menu.gameDisplay,colour.red, (self.x,self.y,self.width,self.height))





    pygame.display.update()
    clock.tick(60)
print ("hello")
