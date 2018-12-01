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
    darkGrey = pygame.Color(23, 26, 37)

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
        self.display_width = 748
        self.display_height = 941
        self.mapXPos = 300
        self.mapYPos = 0
        # Icon Colour
        self.iconColour = Colour.medBlue
        # Icon sizing
        self.iconWidth = 30
        self.iconHeight = 30
        # X and Y coordinates of each icon
        self.AXPos = 275 +300
        self.AYPos = 25
        self.BXPos = 225 +300
        self.BYPos = 225
        self.CXPos = 71 +300
        self.CYPos = 473
        self.DXPos = 205 +300
        self.DYPos = 518
        self.EXPos = 328 +300
        self.EYPos = 459
        self.FXPos = 114 +300
        self.FYPos = 593
        self.GXPos = 313 +300
        self.GYPos = 593
        self.HXPos = 168 +300
        self.HYPos = 704
        self.IXPos = 320 +300
        self.IYPos = 735
        self.JXPos = 192 +300
        self.JYPos = 853
        # Shields
        self.shield1 = pygame.image.load('Shield1.fw.PNG')
        self.shield2 = pygame.image.load('Shield 2.fw.PNG')
        self.shield3 = pygame.image.load('Shield 3.fw.PNG')
        self.shield4 = pygame.image.load('Shield 4.fw.PNG')
        self.shield5 = pygame.image.load('Shield 5.fw.PNG')

        # setting up the display
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')
        self.clock = pygame.time.Clock()
        ######

        self.DisplayMap()
        pygame.display.update()

    def DisplayMap(self):

        # loading the map
        mapImg = pygame.image.load('GOT map 2.JPG')

        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)

        self.gameDisplay.fill(Colour.darkGrey)
        self.gameDisplay.blit(mapImg, (self.mapXPos, self.mapYPos))

        # drawing lines for side menu
        pygame.draw.line(self.gameDisplay, Colour.white, (0,0), (300, 0), 3)
        pygame.draw.line(self.gameDisplay, Colour.white, (0,941), (300, 941), 3)
        pygame.draw.line(self.gameDisplay, Colour.white, (0,0), (0, 941), 3)
        pygame.draw.line(self.gameDisplay, Colour.white, (300,0), (300, 941), 3)

        pygame.draw.rect(self.gameDisplay, Colour.medBlue, (20,150,260,75))
        pygame.draw.rect(self.gameDisplay, Colour.medBlue, (20,250,260,75))
        pygame.draw.rect(self.gameDisplay, Colour.medBlue, (20,350,260,75))

        pygame.font.init()

        myfont = pygame.font.SysFont("Comic Sans MS", 50)
        textsurface = myfont.render("Menu", False, Colour.white)
        #research how to undeline font in pygame
        #pygame.font.Font.set_underline()
        self.gameDisplay.blit(textsurface, (80,5))

        pygame.display.update()

        # Drawing the icons onto the map
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.AXPos, self.AYPos, self.iconHeight, self.iconWidth)) # Node A on network graph
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.BXPos, self.BYPos, self.iconHeight, self.iconWidth)) # Node B
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.CXPos, self.CYPos, self.iconHeight, self.iconWidth)) # Node C
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.DXPos, self.DYPos, self.iconHeight, self.iconWidth)) # Node D
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.EXPos, self.EYPos, self.iconHeight, self.iconWidth)) # Node E
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.FXPos, self.FYPos, self.iconHeight, self.iconWidth)) # Node F
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.GXPos, self.GYPos, self.iconHeight, self.iconWidth)) # Node G
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.HXPos, self.HYPos, self.iconHeight, self.iconWidth)) # Node H
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.IXPos, self.IYPos, self.iconHeight, self.iconWidth)) # Node I
        pygame.draw.rect(self.gameDisplay, self.iconColour, (self.JXPos, self.JYPos, self.iconHeight, self.iconWidth)) # Node J
        pygame.display.update()
        self.PlayGame()
        pygame.display.update()

    def PlayGame(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    crashed = True
                mouse = pygame.mouse.get_pos()
                print(mouse)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.display.update()
                    iconFound = False

                    while iconFound == False:
                        if self.AXPos + self.iconWidth > mouse[0] > self.AXPos and self.AYPos + self.iconHeight > mouse[1] > self.AYPos:

                            self.gameDisplay.blit(self.shield1, (self.AXPos, self.AYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.AXPos, self.AYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.BXPos + self.iconWidth > mouse[0] > self.BXPos and self.BYPos + self.iconHeight > mouse[1] > self.BYPos:
                            self.gameDisplay.blit(self.shield2, (self.BXPos, self.BYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.BXPos, self.BYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.CXPos + self.iconWidth > mouse[0] > self.CXPos and self.CYPos + self.iconHeight > mouse[1] > self.CYPos:
                            self.gameDisplay.blit(self.shield4, (self.CXPos, self.CYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.CXPos, self.CYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.DXPos + self.iconWidth > mouse[0] > self.DXPos and self.DYPos + self.iconHeight > mouse[1] > self.DYPos:
                            self.gameDisplay.blit(self.shield3, (self.DXPos, self.DYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.DXPos, self.DYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.EXPos + self.iconWidth > mouse[0] > self.EXPos and self.EYPos + self.iconHeight > mouse[1] > self.EYPos:
                            self.gameDisplay.blit(self.shield2, (self.EXPos, self.EYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.EXPos, self.EYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.FXPos + self.iconWidth > mouse[0] > self.FXPos and self.FYPos + self.iconHeight > mouse[1] > self.FYPos:
                            self.gameDisplay.blit(self.shield5, (self.FXPos, self.FYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.FXPos, self.FYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.GXPos + self.iconWidth > mouse[0] > self.GXPos and self.GYPos + self.iconHeight > mouse[1] > self.GYPos:
                            self.gameDisplay.blit(self.shield4, (self.GXPos, self.GYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.GXPos, self.GYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.HXPos + self.iconWidth > mouse[0] > self.HXPos and self.HYPos + self.iconHeight > mouse[1] > self.HYPos:
                            self.gameDisplay.blit(self.shield3, (self.HXPos, self.HYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.HXPos, self.HYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.IXPos + self.iconWidth > mouse[0] > self.IXPos and self.IYPos + self.iconHeight > mouse[1] > self.IYPos:
                            self.gameDisplay.blit(self.shield1, (self.IXPos, self.IYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.IXPos, self.IYPos, self.iconHeight, self.iconWidth))
                            iconFound = True
                        elif self.JXPos + self.iconWidth > mouse[0] > self.JXPos and self.JYPos + self.iconHeight > mouse[1] > self.JYPos:
                            self.gameDisplay.blit(self.shield5, (self.JXPos, self.JYPos))
                            #pygame.draw.rect(self.gameDisplay, Colour.aqua, (self.JXPos, self.JYPos, self.iconHeight, self.iconWidth))
                            iconFound = True

                        pygame.display.update()
                else:
                    pass

class Icons():
    def __init__(self):
        # Defines and dsets up the network graph for the map
         self.networkGraph = {
             "A": ["B"],
             "B": ["A","C","D","E"],
             "C": ["B","F"],
             "D": ["B","E","F","G"],
             "E": ["B","D","G"],
             "F": ["C","D","H"],
             "G": ["D","E","H","I"],
             "H": ["F","G","I"],
             "I": ["G","H","J"],
             "J": ["H","I"]}
         print (self.networkGraph["B"])
##A = [B]
##B = [A, C, D, E]
##C = [B, F]
##D = [B, E, F, G]
##E = [B, D, G]
##F = [C, D, H]
##G = [D, E, H, I]
##H = [F, G, I]
##I = [G, H, J]
##J = [H, I]

if __name__ == "__main__":

    pygame.init()
    colour = Colour()
    menu = Menu()
    icons = Icons()
    # changes in order to test objectifying the rectangle A

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
                buttonFound = False
                buttonNumber = 0
                # sort out the button numbers, use iterative statements to define the button number// which botton was pressed
                while buttonFound == False:

                    buttonNumber = buttonNumber + 1
                    if buttonMaxX > mouse[0] > buttonMinX and buttonMaxY > mouse[1] > buttonMinY:

                        pygame.draw.rect(menu.gameDisplay,colour.red, (buttonMinX, buttonMinY, 330,75))

                        pygame.display.update()

                        buttonFound = True

                    # Menu option is loaded below
                        if buttonNumber == 1:
                            pygame.quit()
                            board = Board()

                        elif buttonNumber == 2:
                            ### need to add in a load game function
                            pass

                        elif buttonNumber == 3:
                            pygame.quit()
                            instructions = Instructions()
                            pygame.display.update()
                    else:
                        buttonMinY = buttonMinY + 100
                        buttonMaxY = buttonMaxY + 100

#pygame.draw.rect(menu.gameDisplay,colour.red, (self.x,self.y,self.width,self.height))

    pygame.display.update()
    clock.tick(60)
