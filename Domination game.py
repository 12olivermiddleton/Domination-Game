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
            "A": {"connections": ["B"],
                  "coords": [520, 25]},
            "B": {"connections": ["A", "C", "D", "E"],
                  "coords": [525, 225]},
            "C": {"connections": ["B", "F"],
                  "coords": [371, 473]},
            "D": {"connections": ["B", "E", "F", "G"],
                  "coords": [505, 518]},
            "E": {"connections": ["B", "D", "G"],
                  "coords": [628, 459]},
            "F": {"connections": ["C", "D", "H"],
                  "coords": [414, 593]},
            "G": {"connections": ["D", "E", "H", "I"],
                  "coords": [613, 593]},
            "H": {"connections": ["F", "G", "I"],
                  "coords": [468, 704]},
            "I": {"connections": ["G", "H", "J"],
                  "coords": [620, 735]},
            "J": {"connections": ["H", "I"],
                  "coords": [492, 853]}}
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


class SideMenuLeft():
    # relative sizing for buttons and menus

    def __init__(self):

        # Menu Container
        self.menu_width = 330
        self.x_pos_menu_container = 0
        self.y_pos_menu_container = 0

        # Stage (split into 3 buttons with 1 pixel divider)
        self.y_pos_stage_menu = 876
        self.stage_button_width = round(self.menu_width / 3) - 1
        self.stage_height = 75
        self.x_pos_stage_allocate = 0
        self.x_pos_stage_attack = round(self.menu_width/3)
        self.x_pos_stage_fortify = round(self.menu_width/3)*2

        self.status_colour = Colour.white
        self.current_colour = Colour.red
        self._stage_colour = Colour.black

        self.menu_container_height = self.y_pos_stage_menu + self.stage_height

        # Menu buttons
        self.x_pos_menu_buttons_container_indent = 20
        self.y_pos_menu_buttons_container_top = 150
        self.menu_button_height = 75
        self.menu_button_vertical_gap = 25
        self.menu_button_width = self.menu_width - 2 * self.x_pos_menu_buttons_container_indent # pad either side
        self.menu_button_vertical_spacing = self.menu_button_height + self.menu_button_vertical_gap

        self.btn_save = (self.x_pos_menu_buttons_container_indent, self.y_pos_menu_buttons_container_top, self.menu_button_width, self.menu_button_height)
        self.btn_info = (self.x_pos_menu_buttons_container_indent, self.y_pos_menu_buttons_container_top + self.menu_button_vertical_spacing, self.menu_button_width, self.menu_button_height)
        self.btn_quit = (self.x_pos_menu_buttons_container_indent, self.y_pos_menu_buttons_container_top + 2 * self.menu_button_vertical_spacing, self.menu_button_width, self.menu_button_height)


    def drawItems(self, surface, stage):  # example of method overloading
        # border lines for side menu
        pygame.draw.line(surface, Colour.white, (self.x_pos_menu_container, self.y_pos_menu_container), (self.menu_width, self.y_pos_menu_container), 3)  # across top
        pygame.draw.line(surface, Colour.white, (self.x_pos_menu_container, self.menu_container_height), (self.menu_width, self.menu_container_height), 3) # across bottom
        pygame.draw.line(surface, Colour.white, (self.x_pos_menu_container, self.y_pos_menu_container), (self.x_pos_menu_container, self.menu_container_height), 3) # down left side
        pygame.draw.line(surface, Colour.white, (self.menu_width, self.y_pos_menu_container), (self.menu_width, self.menu_container_height), 3) # down right side

        # side menu left buttons
        pygame.draw.rect(surface, Colour.medium_blue, self.btn_save)
        pygame.draw.rect(surface, Colour.medium_blue, self.btn_info)
        pygame.draw.rect(surface, Colour.medium_blue, self.btn_quit)

        # side menu left stages buttons
        pygame.draw.rect(surface, self.status_colour, (self.x_pos_stage_allocate, self.y_pos_stage_menu, self.stage_button_width, self.stage_height))

        def centreJustifyIndent(indent, button_width, text_object):
            return indent + round((button_width - text_object.get_width()) /2)

        domination_font = CustomFont()
        header_text1 = domination_font.menu_heading.render("Domination", False, Colour.white)
        header_text2 = domination_font.menu_button.render("Menu", False, Colour.white)
        surface.blit(header_text1, (centreJustifyIndent(self.x_pos_menu_buttons_container_indent,self.menu_button_width, header_text1), 5))
        surface.blit(header_text2, (centreJustifyIndent(self.x_pos_menu_buttons_container_indent,self.menu_button_width, header_text2), 75))

        save_text = domination_font.menu_button.render("Save Game", False, self.status_colour)
        help_text = domination_font.menu_button.render("Info", False, self.status_colour)
        quit_text = domination_font.menu_button.render("Quit", False, self.status_colour)
        surface.blit(save_text, (centreJustifyIndent(self.x_pos_menu_buttons_container_indent,self.menu_button_width, save_text), 155))
        surface.blit(help_text, (centreJustifyIndent(self.x_pos_menu_buttons_container_indent,self.menu_button_width, help_text), 255))
        surface.blit(quit_text, (centreJustifyIndent(self.x_pos_menu_buttons_container_indent,self.menu_button_width, quit_text), 355))

        stage_text = domination_font.menu_title.render("Stage", False, Colour.white)
        surface.blit(stage_text, (centreJustifyIndent(self.x_pos_menu_buttons_container_indent, self.menu_button_width, stage_text), 825))

        allocation_text = domination_font.menu_action.render("Allocate", False, self._stage_colour)
        attack_text = domination_font.menu_action.render("Attack", False, self._stage_colour)
        fortify_text = domination_font.menu_action.render("Fortify", False, self._stage_colour)

        if stage > 0:
            surface.blit(allocation_text, (centreJustifyIndent(self.x_pos_stage_allocate, self.stage_button_width, allocation_text), 890))
        if stage > 1:
            pygame.draw.rect(surface, self.status_colour, (self.x_pos_stage_attack, self.y_pos_stage_menu, self.stage_button_width, self.stage_height))
            surface.blit(attack_text,(centreJustifyIndent(self.x_pos_stage_attack, self.stage_button_width, attack_text), 890))
        if stage > 2:
            pygame.draw.rect(surface, self.status_colour, (self.x_pos_stage_fortify, self.y_pos_stage_menu, self.stage_button_width, self.stage_height))
            surface.blit(fortify_text,(centreJustifyIndent(self.x_pos_stage_fortify, self.stage_button_width, fortify_text), 890))



class SideMenuRight():
    def __init__(self):

        # Sections
        self.status_colour = Colour.white
        self.current_colour = Colour.red

        # Menu Container
        self.menu_width = 300
        self.menu_height = 0


class Board():
    def __init__(self):

        # Side menu left
        self.side_menu_left = SideMenuLeft()


        # Board
        self.board_width = 484 # width of map jpg
        self.board_height = 941 # width of map jpg
        self.board_position_x = 0 + self.side_menu_left.menu_width
        self.board_position_y = 0
        self.stage = 1

        # Side menu right
        self.side_menu_right = SideMenuRight()
        self.side_menu_right_position_x = 0 + self.side_menu_left.menu_width + self.board_width
        self.side_menu_right_position_y = 0

        # Display  size
        self.display_width = self.side_menu_left.menu_width + self.board_width + self.side_menu_right.menu_width
        self.display_height = max(self.side_menu_left.menu_container_height, self.board_height, self.side_menu_right.menu_height)

        # Icon information
        self.icon_colour = Colour.medium_blue
        self.icon_list = []

        # setting up the display
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')
        self.game_display.fill(Colour.darkGrey)
        self.clock = pygame.time.Clock()
        ######
        self.side_menu_left.drawItems(self.game_display, self.stage)
        self.setUpIcons()
        self.DisplayMap()


        pygame.display.update()

    def setUpMenuButtons(self):
        pass

    def setUpIcons(self):
        # X and Y coordinates of each icon
        self.icon_list.append(Icon(self.icon_colour, 520, 25, "A", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 525, 225, "B", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 371, 473, "C", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 505, 518, "D", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 628, 459, "E", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 414, 593, "F", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 613, 593, "G", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 468, 704, "H", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 620, 735, "I", 'Shield1.fw.PNG'))
        self.icon_list.append(Icon(self.icon_colour, 492, 853, "J", 'Shield1.fw.PNG'))


    def setUpMenuButtons(self):
        pass

    def DisplayMap(self):
        # loading the map
        map_img = pygame.image.load('GOT map 2.JPG')
        self.game_display.blit(map_img, (self.board_position_x, self.board_position_y))

        pygame.display.update()

        # Drawing the icons onto the map
        for icon in self.icon_list:
            pygame.draw.rect(self.game_display, icon.colour, (icon.x, icon.y, icon.width, icon.height))
            pygame.display.update()

        return self

class PlayGame():
    def __init__(self, board):
        # side menu assistance variables
        self.network_graph = {
            "A": {"connections": ["B"],
                  "coords": [520, 25]},
            "B": {"connections": ["A", "C", "D", "E"],
                  "coords": [525, 225]},
            "C": {"connections": ["B", "F"],
                  "coords": [371, 473]},
            "D": {"connections": ["B", "E", "F", "G"],
                  "coords": [505, 518]},
            "E": {"connections": ["B", "D", "G"],
                  "coords": [628, 459]},
            "F": {"connections": ["C", "D", "H"],
                  "coords": [414, 593]},
            "G": {"connections": ["D", "E", "H", "I"],
                  "coords": [613, 593]},
            "H": {"connections": ["F", "G", "I"],
                  "coords": [468, 704]},
            "I": {"connections": ["G", "H", "J"],
                  "coords": [620, 735]},
            "J": {"connections": ["H", "I"],
                  "coords": [492, 853]}}

        # mouse
        self.mouse_selected_node = ""

        # Variables used to store player turns
        self.player1_turns = 0
        self.player2_turns = 0

        # Varioables used for the change between players
        self.current_player = "p2"
        self.current_player_data = {}
        self.current_player_no_of_territories = 0
        # sets up dictionary for main game loop
        # self.currentNode = 'A'

        self.player1 = {
            "shield": "Shield 5.fw.PNG",
            "playerOccupied": ["A", "D", "E", "H", "I"],
            "unallocated_troops": 0,
            "troops_at_node": {}
        }
        # player 1 initial territory allocation
        for node in self.player1["playerOccupied"]:
            #self.player1[node] = len(self.network_graph[node]["connections"])
            self.player1["troops_at_node"][node] = 1
            self.player1["unallocated_troops"] = 10


        self.player1_no_of_territories = 0
        self.player2 = {
            "shield": "Shield 2.fw.PNG",
            "playerOccupied": ["B", "C", "F", "G", "J"],
            "unallocated_troops": 0,
            "troops_at_node": {}
        }
        # player 2 initial territory allocation
        for node in self.player2["playerOccupied"]:
            #self.player2[node] = len(self.network_graph[node]["connections"])
            self.player2["troops_at_node"][node] = 1
            self.player2["unallocated_troops"] = 10



        self.player2_no_of_territories = 0
        # print (self.player1["p1Occupied"])

        ##        if self.curretnNode in self.player1["p1Occupied"]:
        ##            print("this is a valid move")
        self.crashed = False
        self.board = board
        # self.sideMenuAssistance()

        self.loadBoardState(self.player1, self.player2)
        self.playGame()
        self.allocationStage()


###TODO sort out current players and call in players as an object

    def playGame(self):

        if self.current_player == "p1":
            self.current_player_data = self.player1
            self.opposition_player_data = self.player2
            self.current_player_no_of_territories = self.player1_no_of_territories
            self.current_player = "p2"

        else:
            self.current_player_data = self.player2
            self.opposition_player_data = self.player1
            self.current_player_no_of_territories = self.player2_no_of_territories
            self.current_player = "p1"

        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    self.crashed = True
                mouse = pygame.mouse.get_pos()
                if board.stage == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for icon in board.icon_list:
                            if icon.x + icon.width > mouse[0] > icon.x and icon.y + icon.height > mouse[1] > icon.y:
                                if icon.node not in self.current_player_data["playerOccupied"]:
                                    self.mouse_selected_node = ""
                                else:
                                    print(icon.node, "node")
                                    self.mouse_selected_node = icon.node
                                ### TODO need a visual indication that a node is selected
                    elif event.type == pygame.KEYDOWN:
                        if self.mouse_selected_node:
                            print("selected node: " + self.mouse_selected_node)
                            if event.key == pygame.K_UP:
                                if self.current_player_data["unallocated_troops"] > 0:
                                    self.current_player_data["unallocated_troops"] = self.current_player_data["unallocated_troops"] - 1
                                    self.current_player_data["troops_at_node"][self.mouse_selected_node] = self.current_player_data["troops_at_node"][self.mouse_selected_node] + 1

                            elif event.key == pygame.K_DOWN:
                                if self.current_player_data["troops_at_node"][self.mouse_selected_node] > 1:
                                    self.current_player_data["unallocated_troops"] = self.current_player_data[ "unallocated_troops"] + 1
                                    self.current_player_data["troops_at_node"][self.mouse_selected_node] = self.current_player_data["troops_at_node"][self.mouse_selected_node] - 1
                            self.loadBoardState(self.current_player_data, self.opposition_player_data)
                        else:
                            print("no mouse selected node!" + self.mouse_selected_node)





                    # print (board.stage)
                    # board.stage = board.stage + 1
                    # board.side_menu_left.drawItems(board.game_display, board.stage)
                    # pygame.display.update()

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
        #
        count = 0
        print ("this is the allocation of your troops")
        #implementing breadth first search for nodes around the users current nodes for troop allocation
        # Traversing the network graph to find neighbouring nodes
        for current_node in self.current_player_data["playerOccupied"]:
            #print("this is the node in the allocation stage", node)
            current_vertex_list = self.network_graph[current_node]
            #print (current_vertex_list)
            for vertex in current_vertex_list:
                count = count + 1
        print ("the number of troopps that the player will receive is", count)
        NoOfTroops = count

    def loadBoardState(self, current_player, opposition_player):

        def centreJustifyIndent(indent, button_width, text_object):
            return indent + round((button_width - text_object.get_width()) /2)

        board.DisplayMap()
        for player in [current_player, opposition_player]:
            for node in self.network_graph:
                if node in player["playerOccupied"]:
                    node_pos_x = self.network_graph[node]["coords"][0]
                    node_pos_y = self.network_graph[node]["coords"][1]
                    node_width = 30
                    node_height = 60
                    self.board.game_display.blit(pygame.image.load(player["shield"]), (node_pos_x, node_pos_y))
                    myfont = pygame.font.SysFont("Comic Sans MS", 20)
                    text_surface = myfont.render(str(player["troops_at_node"][node]), False, Colour.white)
                    self.board.game_display.blit(text_surface, (centreJustifyIndent(node_pos_x, node_width, text_surface),node_pos_y + (node_height/2)))

            pygame.display.update()
        pygame.display.update()

    def makeMove(self):
        pass

    def attack(self):
        pass

    def fortify(self):
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
