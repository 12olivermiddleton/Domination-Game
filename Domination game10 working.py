# Programming Project - Domination
# By Oliver Middleton



# things to do
# flow of game display
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
        self.gameDisplay.fill(Colour.darkGrey)

        myfont = pygame.font.SysFont("Comic Sans MS", 60)
        textsurface = myfont.render("Domination", False, Colour.white)
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

class Icons():
    def __init__(self):
        self.usernode = 'B'
        self.priornode = 'G'
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
        print (*self.networkGraph["B"])
        if self.usernode in self.networkGraph[self.priornode]:
            print ("I am a genius!!!")
        else:
            print("that was a massive fail")
         

class Icon():
    def __init__(self, colour, xPos, yPos, node, shield):
        self.colour = colour
        self.xPos = xPos
        self.yPos = yPos
        # Icon sizing
        self.height = 30
        self.width = 30
        self.node = node
        self.shield = shield



class Board():
    def __init__(self):
        # Display  size
        self.display_width = 748
        self.display_height = 941
        self.mapXPos = 300
        self.mapYPos = 0
        # Icon Colour
        self.iconColour = Colour.medBlue
        self.iconList = []
        self.sideMenuLineList =[]
        self.sideMenuLineColour = Colour.white
        self.menuLineWidth = 3

        # setting up the display
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')
        self.clock = pygame.time.Clock()
        ######
        
        self.setUpIcons()
        ##self.setUpSideMenu()
        self.DisplayMap()
        pygame.display.update()
        

    def setUpIcons(self):
        # X and Y coordinates of each icon
        self.iconList.append(Icon(self.iconColour, 575,25,"A",'Shield1.fw.PNG' ))
        self.iconList.append(Icon(self.iconColour, 525,225,"B",'Shield1.fw.PNG' ))
        self.iconList.append(Icon(self.iconColour, 371,473,"C", 'Shield1.fw.PNG'))
        self.iconList.append(Icon(self.iconColour, 505,518,"D", 'Shield1.fw.PNG'))
        self.iconList.append(Icon(self.iconColour, 628,459,"E", 'Shield1.fw.PNG'))
        self.iconList.append(Icon(self.iconColour, 414,593,"F", 'Shield1.fw.PNG'))
        self.iconList.append(Icon(self.iconColour, 613,593,"G", 'Shield1.fw.PNG'))
        self.iconList.append(Icon(self.iconColour, 468,704,"H", 'Shield1.fw.PNG'))
        self.iconList.append(Icon(self.iconColour, 620,735,"I",'Shield1.fw.PNG'))
        self.iconList.append(Icon(self.iconColour, 492,853,"J", 'Shield1.fw.PNG'))

##    def setUpSideMenu(self):
##        self.sideMenuLineList.append(((0,0), (300, 0)))
##        self.sideMenuLineList.append(((5,5), (300, 120)))
##        print (self.sideMenuLineList)


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
        for icon in self.iconList:
            pygame.draw.rect(self.gameDisplay, icon.colour, (icon.xPos, icon.yPos, icon.height, icon.width))
            pygame.display.update()
##
##        # drawing side menu
##        for element in self.sideMenuLineList:
##            pygame.draw.line(self.gameDisplay, self.sideMenuLineColour, ((startXCoord, startYCoord), (endXCoord, endYCoord)),  self.menuLineWidth)
##            pygame.display.update()

        return self

class PlayGame():
    def __init__(self, board):
        self.crashed = False
        self.board = board
        self.play()
        

    def play(self):

        while not self.crashed:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    self.crashed = True
                mouse = pygame.mouse.get_pos()
                    
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    print ("mouse", mouse)
                    #pygame.display.update()
                    for icon in board.iconList:
                        print(icon.xPos, icon.yPos)
                        if icon.xPos + icon.width > mouse[0] > icon.xPos and icon.yPos + icon.height > mouse[1] > icon.yPos:
                            print(icon.node, "node")
                            self.board.gameDisplay.blit(pygame.image.load(icon.shield), (icon.xPos, icon.yPos))
                            iconFound = False
                            pygame.display.update()
                            break

                else:
                    pass


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
    #print(mouse)
    
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
                            play = PlayGame(board)

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
