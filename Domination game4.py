# Programming Project - Domination
# By Oliver Middleton

import pygame
import time

class Colour():
    red = pygame.Color(255,0,0)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0, 153, 255)
    medBlue = pygame.Color(0, 92, 150)
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
        # Display  size
        self.display_width = 491
        self.display_height = 941
        # Icon Colour
        self.iconColour = Colour.medBlue
        # Icon sizing
        self.iconWidth = 30
        self.iconHeight = 30
        # X and Y coordinates of each icon
        self.AXPos = 275
        self.AYPos = 25
        self.BXPos = 225
        self.BYPos = 225
        self.CXPos = 71
        self.CYPos = 473
        self.DXPos = 205
        self.DYPos = 518
        self.EXPos = 328
        self.EYPos = 459
        self.FXPos = 114
        self.FYPos = 593
        self.GXPos = 313
        self.GYPos = 593
        self.HXPos = 168
        self.HYPos = 704
        self.IXPos = 320
        self.IYPos = 735
        self.JXPos = 192
        self.JYPos = 853

        self.DisplayMap()

    def DisplayMap(self):

        # setting up the display
        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')
        clock = pygame.time.Clock()
        # loading the map
        mapImg = pygame.image.load('GOT map.JPG')

        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)

        gameDisplay.fill(Colour.white)
        gameDisplay.blit(mapImg, (0, 0))

        # Drawing the icons onto the map
        pygame.draw.rect(gameDisplay, self.iconColour, (self.AXPos, self.AYPos, self.iconHeight, self.iconWidth)) # Node A on network graph
        pygame.draw.rect(gameDisplay, self.iconColour, (self.BXPos, self.BYPos, self.iconHeight, self.iconWidth)) # Node B
        pygame.draw.rect(gameDisplay, self.iconColour, (self.CXPos, self.CYPos, self.iconHeight, self.iconWidth)) # Node C
        pygame.draw.rect(gameDisplay, self.iconColour, (self.DXPos, self.DYPos, self.iconHeight, self.iconWidth)) # Node D
        pygame.draw.rect(gameDisplay, self.iconColour, (self.EXPos, self.EYPos, self.iconHeight, self.iconWidth)) # Node E
        pygame.draw.rect(gameDisplay, self.iconColour, (self.FXPos, self.FYPos, self.iconHeight, self.iconWidth)) # Node F
        pygame.draw.rect(gameDisplay, self.iconColour, (self.GXPos, self.GYPos, self.iconHeight, self.iconWidth)) # Node G
        pygame.draw.rect(gameDisplay, self.iconColour, (self.HXPos, self.HYPos, self.iconHeight, self.iconWidth)) # Node H
        pygame.draw.rect(gameDisplay, self.iconColour, (self.IXPos, self.IYPos, self.iconHeight, self.iconWidth)) # Node I
        pygame.draw.rect(gameDisplay, self.iconColour, (self.JXPos, self.JYPos, self.iconHeight, self.iconWidth)) # Node J


class Icons():
    def __init__(self):
        self.A = (22,120)


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
