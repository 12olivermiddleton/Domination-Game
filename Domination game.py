# Programming Project - Domination
# By Oliver Middleton

# things to do
# flow of game display
import pygame
import time


class Colour():
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 153, 255)
    medium_blue = pygame.Color(0, 92, 150)
    dark_blue = pygame.Color(0, 51, 102)
    white = pygame.Color(255, 255, 255)
    aqua = pygame.Color(0, 255, 255)
    black = pygame.Color(0, 0, 0)
    pink = pygame.Color(255, 200, 200)
    darkGrey = pygame.Color(23, 26, 37)


class CustomFont():
    def __init__(self):
        pygame.font.init()
        domination_font = "./MyDominationFont.ttf"
        self.splash_title = pygame.font.Font(domination_font, 50)
        self.splash_button = pygame.font.Font(domination_font, 30)
        self.menu_heading = pygame.font.Font(domination_font, 30)
        self.menu_title = pygame.font.Font(domination_font, 20)
        self.menu_action = pygame.font.Font(domination_font, 15)
        self.menu_button = pygame.font.Font(domination_font, 30)


class Menu():
    def __init__(self):

        self.button_list = []
        self.display_width = 600
        self.display_height = 600
        domination_font = CustomFont()

        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Menu')
        self.game_display.fill(Colour.darkGrey)

        text_surface = domination_font.splash_title.render("Domination", False, Colour.white)
        self.game_display.blit(text_surface, (110, 50))

        x = 120
        y = 220
        text_pos_x = 130
        button_text_no = 0

        for i in range(3):
            button_text_no = button_text_no + 1
            text_pos_y = y + 20
            self.button_list.append(Button(x, y, self.game_display))

            if button_text_no == 1:
                text_surface = domination_font.splash_button.render("Play Game", False, Colour.white)
                self.game_display.blit(text_surface, (text_pos_x, text_pos_y))

            elif button_text_no == 2:
                text_surface = domination_font.splash_button.render("Load Game", False, Colour.white)
                self.game_display.blit(text_surface, (text_pos_x, text_pos_y))

            elif button_text_no == 3:
                text_surface = domination_font.splash_button.render("Instructions", False, Colour.white)
                self.game_display.blit(text_surface, (text_pos_x, text_pos_y))

            y = y + 100
            pygame.display.update()

    def getButtonList(self):
        return self.button_list


class Instructions():
    def __init__(self):
        self.instructionsDisplay_width = 600
        self.instructionsDisplay_height = 700
        self.instructionsPanel()

    def instructionsPanel(self):
        game_display = pygame.display.set_mode((self.instructionsDisplay_width, self.instructionsDisplay_height))
        pygame.display.set_caption('Instructions')
        game_display.fill(Colour.pink)

        # This is a test to see if the game display window works
        # pygame.draw.rect(game_display, colour.red, (100,100,100,100))


class Graphic():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Button(Graphic):
    def __init__(self, x, y, game_display):
        super().__init__(x, y)
        self.initial_colour = Colour.dark_blue
        self.width = 330
        self.height = 75

        pygame.draw.rect(game_display, self.initial_colour, (self.x, self.y, self.width, self.height))
        pygame.display.update()


class Icons():
    def __init__(self):
        self.user_node = 'B'
        self.prior_node = 'G'
        # Defines and sets up the network graph for the map
        self.network_graph = {
            "A": ["B"],
            "B": ["A", "C", "D", "E"],
            "C": ["B", "F"],
            "D": ["B", "E", "F", "G"],
            "E": ["B", "D", "G"],
            "F": ["C", "D", "H"],
            "G": ["D", "E", "H", "I"],
            "H": ["F", "G", "I"],
            "I": ["G", "H", "J"],
            "J": ["H", "I"]}
        print(*self.network_graph["B"])
        if self.user_node in self.network_graph[self.prior_node]:
            print("I am a genius!!!")
        else:
            print("that was a massive fail")


class Icon(Graphic):
    def __init__(self, colour, x, y, node, shield):
        super().__init__(x, y)
        self.colour = colour
        self.x = x
        self.y = y
        # Icon sizing
        self.height = 30
        self.width = 30
        self.node = node
        self.shield = shield


class Board():
    def __init__(self):
        # Display  size
        self.display_width = 1048
        self.display_height = 941
        self.board_position_x = 300
        self.board_position_y = 0
        # Icon information
        self.icon_colour = Colour.medium_blue
        self.icon_list = []

        # stage menu
        self.stage_width = 99
        self.stage_height = 75
        self.sidemenu_stage_position_y = 876
        self.sidemenu_stage_allocate_pos_x = 0
        self.sidemenu_stage_attack_pos_x = 101
        self.sidemenu_stage_fortify_pos_x = 202
        self.status_colour = Colour.white
        self.current_colour = Colour.red
        self._stage_colour = Colour.black

        # setting up the display
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')
        self.clock = pygame.time.Clock()
        ######
        self.setUpIcons()
        ##self.setUpSideMenu()
        self.DisplayMap()
        pygame.display.update()

    def setUpIcons(self):
        # X and Y coordinates of each icon
        self.icon_list.append(Icon(self.icon_colour, 575, 25, "A", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 525, 225, "B", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 371, 473, "C", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 505, 518, "D", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 628, 459, "E", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 414, 593, "F", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 613, 593, "G", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 468, 704, "H", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 620, 735, "I", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 492, 853, "J", 'Shield1.fw.PNG'))

    ##    def setUpSideMenu(self):
    ##        self.sideMenuLineList.append(((0,0), (300, 0)))
    ##        self.sideMenuLineList.append(((5,5), (300, 120)))
    ##        print (self.sideMenuLineList)

    def setUpMenuButtons(self):
        pass

    def DisplayMap(self):
        domination_font = CustomFont()
        # loading the map
        map_img = pygame.image.load('GOT map 2.JPG')

        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)

        self.game_display.fill(Colour.darkGrey)
        self.game_display.blit(map_img, (self.board_position_x, self.board_position_y))

        # drawing lines for side menu
        pygame.draw.line(self.game_display, Colour.white, (0, 0), (300, 0), 3)
        pygame.draw.line(self.game_display, Colour.white, (0, 941), (300, 941), 3)
        pygame.draw.line(self.game_display, Colour.white, (0, 0), (0, 941), 3)
        pygame.draw.line(self.game_display, Colour.white, (300, 0), (300, 941), 3)

        pygame.draw.rect(self.game_display, Colour.medium_blue, (20, 150, 260, 75))
        pygame.draw.rect(self.game_display, Colour.medium_blue, (20, 250, 260, 75))
        pygame.draw.rect(self.game_display, Colour.medium_blue, (20, 350, 260, 75))

        pygame.draw.rect(self.game_display, self.status_colour,
                         (self.sidemenu_stage_allocate_pos_x, self.sidemenu_stage_position_y, self.stage_width, self.stage_height))
        pygame.draw.rect(self.game_display, self.status_colour,
                         (self.sidemenu_stage_attack_pos_x, self.sidemenu_stage_position_y, self.stage_width, self.stage_height))
        pygame.draw.rect(self.game_display, self.status_colour,
                         (self.sidemenu_stage_fortify_pos_x, self.sidemenu_stage_position_y, self.stage_width, self.stage_height))

        header_text1 = domination_font.menu_heading.render("Domination", False, Colour.white)
        header_text2 = domination_font.menu_button.render("Menu", False, Colour.white)
        stage_text = domination_font.menu_title.render("Stage", False, Colour.white)
        allocation_text = domination_font.menu_action.render("Allocate", False, self._stage_colour)
        attack_text = domination_font.menu_action.render("Attack", False, self._stage_colour)
        fortify_text = domination_font.menu_action.render("Fortify", False, self._stage_colour)
        help_text = domination_font.menu_button.render("Help", False, self.status_colour)
        savegame_text = domination_font.menu_button.render("Save Game", False, self.status_colour)
        savequit_text = domination_font.menu_button.render("Save & Quit", False, self.status_colour)
        quit_text = domination_font.menu_button.render("Quit", False, self.status_colour)

        # research how to undeline font in pygame
        # pygame.font.Font.set_underline()
        self.game_display.blit(header_text1, (20, 5))
        self.game_display.blit(header_text2, (100, 75))
        self.game_display.blit(stage_text, (110, 825))
        self.game_display.blit(allocation_text, (5, 890))
        self.game_display.blit(attack_text, (120, 890))
        self.game_display.blit(fortify_text, (220, 890))
        self.game_display.blit(savegame_text, (45, 155))
        self.game_display.blit(help_text, (100, 255))
        self.game_display.blit(quit_text, (100, 355))

        pygame.display.update()

        # Drawing the icons onto the map
        for icon in self.icon_list:
            pygame.draw.rect(self.game_display, icon.colour, (icon.x, icon.y, icon.height, icon.width))
            pygame.display.update()
        ##
        ##        # drawing side menu
        ##        for element in self.sideMenuLineList:
        ##            pygame.draw.line(self.gameDisplay, self.sideMenuLineColour, ((startXCoord, startYCoord), (endXCoord, endYCoord)),  self.menuLineWidth)
        ##            pygame.display.update()

        return self


class PlayGame():
    def __init__(self, board):
        # side menu assistance variables
        self.stage_width = 99
        self.stage_height = 75
        self.sidemenu_stage_position_y = 876
        self.sidemenu_stage_allocate_pos_x = 40
        self.sidemenu_stage_attack_pos_x = 101
        self.sidemenu_stage_fortify_pos_x = 202
        self.status_colour = Colour.white
        self.current_colour = Colour.red
        self.network_graph = {
            "A": ["B"],
            "B": ["A", "C", "D", "E"],
            "C": ["B", "F"],
            "D": ["B", "E", "F", "G"],
            "E": ["B", "D", "G"],
            "F": ["C", "D", "H"],
            "G": ["D", "E", "H", "I"],
            "H": ["F", "G", "I"],
            "I": ["G", "H", "J"],
            "J": ["H", "I"]}
        # Variables used to store player turns
        self.player1_turns = 0
        self.player2_turns = 0

        # Varioables used for the change between players
        self.current_player = "p2"
        self.current_shield = ""
        self.current_player_data = {}
        self.current_player_no_of_territories = 0
        # sets up dictionary for main game loop
        # self.currentNode = 'A'
        self.player1_shield = 'Shield 5.fw.PNG'
        self.player2_shield = 'Shield 2.fw.PNG'

        self.player1 = {
            "playerOccupied": [],
            "A": [],  # Part of dict storing No, of troops
            "B": [],
            "C": [],
            "D": [],
            "E": [],
            "F": [],
            "G": [],
            "H": [],
            "I": [],
            "J": []}
        self.player1_no_of_territories = 0
        self.player2 = {
            ###TODO remove this hardcoding
            "playerOccupied": ["A","D", "G", "I"],
            "A": [],  # Part of dict storing No, of troops
            "B": [],
            "C": [],
            "D": [],
            "E": [],
            "F": [],
            "G": [],
            "H": [],
            "I": [],
            "J": []}
        self.player2_no_of_territories = 0
        # print (self.player1["p1Occupied"])

        ##        if self.curretnNode in self.player1["p1Occupied"]:
        ##            print("this is a valid move")
        self.crashed = False
        self.board = board
        # self.sideMenuAssistance()

        self.playGame()
        self.allocationStage()
        self.play()

    def playGame(self):

        if self.current_player == "p1":
            self.current_player_data = self.player1
            self.current_player_no_of_territories = self.player1_no_of_territories
            self.current_shield = self.player1_shield
            print(self.current_player_data)
            print(self.current_player_no_of_territories)
            self.current_player = "p2"

        else:
            self.current_player_data = self.player2
            self.current_player_no_of_territories = self.player2_no_of_territories
            self.current_shield = self.player2_shield
            print(self.current_player_data)
            print(self.current_player_no_of_territories)
            self.current_player = "p1"
        # while not self.crashed:
        #     for event in pygame.event.get():
        #         # print(event)
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
        #             self.crashed = True
        #         mouse = pygame.mouse.get_pos()
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             # for
        #             # for button in
        #             # print ("mouse", mouse)
        #             # pygame.display.update()
        #             for icon in board.icon_list:
        #                 print(icon.x, icon.y)
        #                 if icon.x + icon.width > mouse[0] > icon.x and icon.y + icon.height > mouse[1] > icon.y:
        #                     print(icon.node, "node")
        #                     self.board.game_display.blit(pygame.image.load(self.current_shield), (icon.x, icon.y))
        #                     if icon.node in self.current_player_data["playerOccupied"]:
        #                         pass
        #                     else:
        #                         self.current_player_data["playerOccupied"].extend(icon.node)
        #                         print(self.current_player_data)
        #
        #                     iconFound = False
        #                     pygame.display.update()
        #                     break
        #         else:
        #             pass


    def SaveGame(self):
        pass

    def LoadGame(self):
        pass

        pygame.display.update()


    def allocationStage(self):
        count = 0
        print ("this is the allocation of your troops")
        #implementing breadth first search for nodes around the users current nodes for troop allocation
        # Traversing the network graph to find neighbouring nodes
        for CurrentNode in self.current_player_data["playerOccupied"]:
            #print("this is the node in the allocation stage", node)
            CurrentVertexList = self.network_graph[CurrentNode]
            #print (CurrentVertexList)
            for vertex in CurrentVertexList:
                count = count + 1
        print ("the number of troopps that the player will receive is", count)
        NoOfTroops = count

        pygame.display.update()

    def makeMove(self):
        pass

    def attack(self):
        pass

    def fortify(self):
        pass

    def play(self):
        while not self.crashed:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    self.crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("I'm a genius!!")
        pass


##    def play(self):
##        while not self.crashed:
##            for event in pygame.event.get():
##                #print(event)
##                if event.type == pygame.QUIT:
##                    pygame.quit()
##                    quit()
##                    self.crashed = True
##                mouse = pygame.mouse.get_pos()
##
##                if event.type == pygame.MOUSEBUTTONDOWN:
##                    print ("mouse", mouse)
##                    #pygame.display.update()
##                    for icon in board.iconList:
##                        print(icon.x, icon.y)
##                        if icon.x + icon.width > mouse[0] > icon.x and icon.y + icon.height > mouse[1] > icon.y:
##                            print(icon.node, "node")
##                            self.board.gameDisplay.blit(pygame.image.load(icon.shield), (icon.x, icon.y))
##                            iconFound = False
##                            pygame.display.update()
##                            break
##
##                else:
##                    pass

if __name__ == "__main__":

    pygame.init()
    colour = Colour()
    menu = Menu()
    icons = Icons()
    # changes in order to test objectifying the rectangle A

    # board = Board()
    clock = pygame.time.Clock()
    mouse = pygame.mouse.get_pos()
    # print(mouse)
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_min_x = 120
                button_max_x = 450
                button_min_y = 220
                button_max_y = 295
                mouse = pygame.mouse.get_pos()
                print(mouse)
                button_found = False
                button_number = 0
                # sort out the button numbers, use iterative statements to define the button number// which botton was pressed
                while button_found == False:
                    button_number = button_number + 1
                    if button_max_x > mouse[0] > button_min_x and button_max_y > mouse[1] > button_min_y:
                        pygame.draw.rect(menu.game_display, colour.red, (button_min_x, button_min_y, 330, 75))
                        pygame.display.update()
                        button_found = True
                        # Menu option is loaded below
                        if button_number == 1:
                            pygame.quit()
                            board = Board()
                            play = PlayGame(board)
                        elif button_number == 2:
                            ### need to add in a load game function
                            pass
                        elif button_number == 3:
                            pygame.quit()
                            instructions = Instructions()
                            pygame.display.update()
                    else:
                        button_min_y = button_min_y + 100
                        button_max_y = button_max_y + 100
    # pygame.draw.rect(menu.gameDisplay,colour.red, (self.x,self.y,self.width,self.height))

    pygame.display.update()
    clock.tick(60)
