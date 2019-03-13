# Programming Project - Domination
# By Oliver Middleton

# things to do
# flow of game display
import pygame
import pickle
import random
import pprint
import time

pp = pprint.PrettyPrinter(indent=4)


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

class SigilBanner():
    height= 100
    width = 100


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
                text_surface = domination_font.splash_button.render("New Game", False, Colour.white)
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


def centreJustifyButton(button_xpos, button_width, text_object):
    return button_xpos + round((button_width - text_object.get_width()) / 2)


def verticalJustifyButton(button_ypos, button_height, text_object):
    return button_ypos + round((button_height - text_object.get_height()) / 2)


game_buttons = {}


def setButtonState(operation, button_id, button):
    if operation == "add":
        # add a button to the dictionary of buttons
        game_buttons[button_id] = button

    if operation == "remove":
        # remove a button from the array of buttons
        game_buttons.pop(button_id, None)


def getButtonState():
    return game_buttons


class PaperButton():
    def __init__(self):
        # defaults
        self.button_rectangle = (0, 0, 0, 0)
        self.save_text_x = 0
        self.save_text_y = 0
        self.btn_label = ""
        self.text_on_paper = Colour.black
        self.domination_font = CustomFont()
        self.picture = pygame.image.load("empty aged paper 30pc.jpg")
        self.button_id = ""

    def drawButton(self, surface, background_image, btn_width, btn_height, btn_x, btn_y, btn_text, btn_id):
        self.picture = pygame.image.load(background_image)
        self.picture = pygame.transform.scale(self.picture, (btn_width, btn_height))
        self.button_id = btn_id
        self.button_rectangle = self.picture.get_rect()
        self.button_rectangle = self.button_rectangle.move(btn_x, btn_y)
        if any(char.isalpha() for char in str(btn_text)):
            btn_label = self.domination_font.menu_button.render(btn_text, False, self.text_on_paper)
        else:
            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            btn_label = myfont.render(str(btn_text), False, self.text_on_paper)

        surface.blit(self.picture, self.button_rectangle)

        btn_label_x = centreJustifyButton(self.button_rectangle.x, self.button_rectangle.width, btn_label)
        btn_label_y = verticalJustifyButton(self.button_rectangle.y, self.button_rectangle.height, btn_label)
        surface.blit(btn_label, (btn_label_x, btn_label_y))
        setButtonState("add", btn_id, self.button_rectangle)

class PaperTroopArea():
    def __init__(self):
        # defaults
        self.button_rectangle = (0, 0, 0, 0)
        self.save_text_x = 0
        self.save_text_y = 0
        self.btn_label = ""
        self.text_on_paper = Colour.black
        self.domination_font = CustomFont()
        self.picture = pygame.image.load("empty aged paper 30pc.jpg")
        self.button_id = ""

    def drawArea(self, surface, background_image, btn_width, btn_height, btn_x, btn_y, btn_text):
        self.picture = pygame.image.load(background_image)
        self.picture = pygame.transform.scale(self.picture, (btn_width, btn_height))
        self.button_rectangle = self.picture.get_rect()
        self.button_rectangle = self.button_rectangle.move(btn_x, btn_y)
        if any(char.isalpha() for char in str(btn_text)):
            btn_label = self.domination_font.menu_button.render(btn_text, False, self.text_on_paper)
        else:
            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            btn_label = myfont.render(str(btn_text), False, self.text_on_paper)

        surface.blit(self.picture, self.button_rectangle)

        btn_label_x = centreJustifyButton(self.button_rectangle.x, self.button_rectangle.width, btn_label)
        btn_label_y = verticalJustifyButton(self.button_rectangle.y, self.button_rectangle.height, btn_label)
        surface.blit(btn_label, (btn_label_x, btn_label_y))

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
        self.text_on_paper = Colour.black
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

    def drawItems(self, surface, stage):  # example of method overloading
        # border lines for side menu
        pygame.draw.line(surface, Colour.white, (self.x_pos_menu_container, self.y_pos_menu_container), (self.menu_width, self.y_pos_menu_container), 3)  # across top
        pygame.draw.line(surface, Colour.white, (self.x_pos_menu_container, self.menu_container_height), (self.menu_width, self.menu_container_height), 3) # across bottom
        pygame.draw.line(surface, Colour.white, (self.x_pos_menu_container, self.y_pos_menu_container), (self.x_pos_menu_container, self.menu_container_height), 3) # down left side
        pygame.draw.line(surface, Colour.white, (self.menu_width, self.y_pos_menu_container), (self.menu_width, self.menu_container_height), 3) # down right side

        # side menu left buttons
        btn_background = "empty aged paper 30pc.jpg"
        btn_save = PaperButton()
        btn_save.drawButton(surface, btn_background, self.menu_button_width, self.menu_button_height, self.x_pos_menu_buttons_container_indent, self.y_pos_menu_buttons_container_top, "Save Game", "save")
        btn_info = PaperButton()
        btn_info.drawButton(surface, btn_background, self.menu_button_width, self.menu_button_height, self.x_pos_menu_buttons_container_indent, self.y_pos_menu_buttons_container_top + self.menu_button_vertical_spacing, "Info", "info")
        btn_quit = PaperButton()
        btn_quit.drawButton(surface, btn_background, self.menu_button_width, self.menu_button_height, self.x_pos_menu_buttons_container_indent, self.y_pos_menu_buttons_container_top + 2 * self.menu_button_vertical_spacing, "Quit", "quit")

        # side menu left stages buttons
        pygame.draw.rect(surface, self.status_colour, (self.x_pos_stage_allocate, self.y_pos_stage_menu, self.stage_button_width, self.stage_height))

        domination_font = CustomFont()
        header_text1 = domination_font.menu_heading.render("Domination", False, Colour.white)
        header_text2 = domination_font.menu_button.render("Menu", False, Colour.white)
        surface.blit(header_text1, (centreJustifyButton(self.x_pos_menu_buttons_container_indent,self.menu_button_width, header_text1), 5))
        surface.blit(header_text2, (centreJustifyButton(self.x_pos_menu_buttons_container_indent,self.menu_button_width, header_text2), 75))
        
        stage_text = domination_font.menu_title.render("Stage", False, Colour.white)
        surface.blit(stage_text, (centreJustifyButton(self.x_pos_menu_buttons_container_indent, self.menu_button_width, stage_text), 825))

        allocation_text = domination_font.menu_action.render("Allocate", False, self._stage_colour)
        attack_text = domination_font.menu_action.render("Attack", False, self._stage_colour)
        fortify_text = domination_font.menu_action.render("Fortify", False, self._stage_colour)

        if stage > 0:
            surface.blit(allocation_text, (centreJustifyButton(self.x_pos_stage_allocate, self.stage_button_width, allocation_text), 890))
        if stage > 1:
            pygame.draw.rect(surface, self.status_colour, (self.x_pos_stage_attack, self.y_pos_stage_menu, self.stage_button_width, self.stage_height))
            surface.blit(attack_text,(centreJustifyButton(self.x_pos_stage_attack, self.stage_button_width, attack_text), 890))
        if stage > 2:
            pygame.draw.rect(surface, self.status_colour, (self.x_pos_stage_fortify, self.y_pos_stage_menu, self.stage_button_width, self.stage_height))
            surface.blit(fortify_text,(centreJustifyButton(self.x_pos_stage_fortify, self.stage_button_width, fortify_text), 890))
        pygame.display.update()

class TroopArea():
    def __init__(self):
        # Player 1 Troop area
        self.troop_area_background = "scroll compass map 30pc.jpg"
        self.troop_area_indent_from_left = 0
        self.troop_area_indent_from_top = 60
        self.troop_area_width = 0
        self.troop_area_height = 300
        self.troop_area_xpos = 0
        self.troop_area_ypos = 0
        self.text_on_troop_area = Colour.black

        ## Sigil
        self.sigil_width = SigilBanner.width
        self.sigil_height = SigilBanner.height

        # btn confirm to next stage
        self.btn_confirm_indent_from_left = 60
        self.btn_confirm_indent_from_bottom = 60
        self.btn_confirm_background = "empty aged paper 30pc.jpg"
        self.btn_confirm_width = 200
        self.btn_confirm_height = 75


    def drawTroopArea(self, board, player, pos_x, pos_y, player_string):
        domination_font = CustomFont()
        self.troop_area_width = board.side_menu_right.menu_width
        self.troop_area_xpos = pos_x
        self.troop_area_ypos = pos_y
        player_text = domination_font.menu_button.render(player_string, False, self.text_on_troop_area)
        board.game_display.blit(player_text, (self.troop_area_xpos, self.troop_area_ypos))

        ## Sigil
        if player["selected_node_banner"]:
            sigil_xpos = pos_x
            sigil_ypos = pos_y + (self.troop_area_height - self.sigil_height) / 2
            picture = pygame.image.load(player["selected_node_banner"])
            picture = pygame.transform.scale(picture, (self.sigil_width, self.sigil_height))
            sigil_rectangle = picture.get_rect()
            sigil_rectangle = sigil_rectangle.move(sigil_xpos, sigil_ypos)
            board.game_display.blit(picture, sigil_rectangle)

        # # Confirm Button
        if board.stage == 1:
            btn_confirm_xpos = self.troop_area_xpos + board.side_menu_right.menu_width - self.btn_confirm_width
            btn_confirm_ypos = self.troop_area_ypos + self.troop_area_height - self.btn_confirm_height
            btn_id = "confirm" + player["shield"]
            if player["unallocated_troops"] == 0:
                btn_confirm = PaperButton()
                btn_confirm.drawButton(board.game_display, self.btn_confirm_background, self.btn_confirm_width, self.btn_confirm_height, btn_confirm_xpos, btn_confirm_ypos, "Confirm", btn_id)



class SideMenuRight():
    def __init__(self, menu_xpos, menu_ypos, menu_height):

        # Colours
        self.status_colour = Colour.white
        self.current_colour = Colour.red
        self.initial_colour = Colour.darkGrey

        # Menu Container
        self.menu_xpos = menu_xpos
        self.menu_ypos = menu_ypos
        self.menu_width = 450
        self.menu_height = menu_height

        # Side Menu Right Title
        self.menu_title_height = 60

        # Troop Area
        self.troop_area_background = "scroll compass map 30pc.jpg"
        troop_area_indent_from_left = 0
        self.troop_area_height = 300
        troop_area_vertical_gap = 60
        troop_area_indent_from_top = self.menu_title_height
        self.player_troop_banner_width = 100
        self.player_troop_banner_height = 100
        self.player1_troop_area_xpos = self.menu_xpos + troop_area_indent_from_left
        self.player1_troop_area_ypos = self.menu_ypos + troop_area_indent_from_top
        self.player2_troop_area_xpos = self.menu_xpos + troop_area_indent_from_left
        self.player2_troop_area_ypos = self.menu_ypos + troop_area_indent_from_top + self.troop_area_height + troop_area_vertical_gap
        self.player2_troop_banner_xpos = self.menu_xpos + troop_area_indent_from_left
        self.player2_troop_banner_ypos = self.menu_ypos + troop_area_indent_from_top + self.troop_area_height + troop_area_vertical_gap


    def drawItems(self, surface, stage):
        domination_font = CustomFont()
        stage_text = ""
        if stage == 1:
            stage_text = "Allocate troops"
        elif stage == 2:
            stage_text = "Launch the Attack"
        pygame.draw.rect(surface, self.initial_colour, (self.menu_xpos, self.menu_ypos, self.menu_width, self.menu_height))
        header_text1 = domination_font.menu_heading.render(stage_text, False, Colour.white)
        surface.blit(header_text1, (centreJustifyButton(self.menu_xpos, self.menu_width, header_text1), 5))

    def drawTroopAllocationArea(self, board, player1_state, player2_state):
        player1_troop_area_backing = PaperTroopArea()
        player2_troop_area_backing = PaperTroopArea()
        if board.stage == 1:
            player1_troop_area_backing.drawArea(board.game_display, self.troop_area_background, self.menu_width, self.troop_area_height, self.player1_troop_area_xpos, self.player1_troop_area_ypos, player1_state["unallocated_troops"])
            player2_troop_area_backing.drawArea(board.game_display, self.troop_area_background, self.menu_width, self.troop_area_height, self.player2_troop_area_xpos, self.player2_troop_area_ypos, player2_state["unallocated_troops"])
        elif board.stage == 2:
            troops_at_p1_node = ""
            troops_at_p2_node = ""
            if player1_state["selected_node"] != "":
                troops_at_p1_node = player1_state["troops_at_node"][player1_state["selected_node"]]
                if board.player_turn["id"] == player1_state["id"]:
                    # TODO: highlight the player attacking in the side menu right.
                    print("highlight green rect on p1")
                else:
                    print("highlight red rect on p1")
            if player2_state["selected_node"] != "":
                troops_at_p2_node = player2_state["troops_at_node"][player2_state["selected_node"]]
                if board.player_turn["id"] == player2_state["id"]:
                    print("highlight green rect on p2")
                else:
                    print("highlight red rect on p2")
            player1_troop_area_backing.drawArea(board.game_display, self.troop_area_background, self.menu_width, self.troop_area_height, self.player1_troop_area_xpos, self.player1_troop_area_ypos, troops_at_p1_node)
            player2_troop_area_backing.drawArea(board.game_display, self.troop_area_background, self.menu_width, self.troop_area_height, self.player2_troop_area_xpos, self.player2_troop_area_ypos, troops_at_p2_node)
        player1_troop_area = TroopArea()
        player2_troop_area = TroopArea()
        player1_troop_area.drawTroopArea(board, player1_state, self.player1_troop_area_xpos, self.player1_troop_area_ypos, "Player One")
        player2_troop_area.drawTroopArea(board, player2_state, self.player2_troop_area_xpos, self.player2_troop_area_ypos, "Player Two")

class NodeGraphic():
    def __init__(self):
        self.width = 30
        self.height = 60
        self.pos_x = 0
        self.pos_y = 0
        self.node_network_name = ""
        self.highlight_border_thickness = 1
        self.highlight_border_colour_available = Colour.blue
        self.highlight_border_colour_selected = Colour.green
        self.highlight_border_colour_enemy = Colour.red

    def drawNode(self, board, player):

        highlight_rectangle = (self.pos_x - self.highlight_border_thickness,
                               self.pos_y - self.highlight_border_thickness,
                               self.width + 2*self.highlight_border_thickness,
                               self.height + self.highlight_border_thickness)

        # Available to select
        if board.player_turn["id"] == player["id"]:
            print("Available to select", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_available, highlight_rectangle, self.highlight_border_thickness)
        # Selected
        if self.node_network_name == board.mouse_selected_node:
            print("Selected", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_selected, highlight_rectangle)
        # Possible Enemy Node
        if self.node_network_name in board.possible_targets:
            print("Possible Enemy", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_enemy, highlight_rectangle, self.highlight_border_thickness)
        # Selected Enemy Node
        if self.node_network_name == board.mouse_selected_attack_node:
            print("Selected Enemy", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_enemy, highlight_rectangle)

        board.game_display.blit(pygame.image.load(player["shield"]), (self.pos_x, self.pos_y))
        myfont = pygame.font.SysFont("Comic Sans MS", 20)
        text_surface = myfont.render(str(player["troops_at_node"][self.node_network_name]), False, Colour.white)
        board.game_display.blit(text_surface, (
        centreJustifyButton(self.pos_x, self.width, text_surface), self.pos_y + round(self.height / 2)))

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
        self.player_turn = ""
        self.possible_targets = []

        # Side menu right
        self.side_menu_right_position_x = 0 + self.side_menu_left.menu_width + self.board_width
        self.side_menu_right_position_y = 0
        self.side_menu_right = SideMenuRight(self.side_menu_right_position_x, self.side_menu_right_position_y, self.board_height)

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
        self.side_menu_right.drawItems(self.game_display, self.stage)
        self.setUpIcons()
        self.DisplayMap()

        # mouse
        self.mouse_selected_node = ""
        self.mouse_selected_launch_node = ""
        self.mouse_selected_attack_node = ""

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

        return self

class PlayGame():
    def __init__(self, board):

        # side menu assistance variables
        self.network_graph = {}
        self.current_player_data = {}
        self.opposition_player_data = {}

        # Variables used to store player turns
        self.player1_turns = 0
        self.player2_turns = 0

        self.crashed = False
        self.board = board
        self.side_menu_left = board.side_menu_left
        self.side_menu_right = board.side_menu_right

    def saveGame(self, game_state):
        print('Save:', game_state)
        with open('test_pickle.pkl', 'wb') as pickle_out:
            pickle.dump(game_state, pickle_out)

    def quitGame(self):
        pygame.quit()

    def allocationStage(self, game_state):
        #
        count = 0
        print ("this is the allocation of your troops", game_state)
        #implementing breadth first search for nodes around the users current nodes for troop allocation
        # Traversing the network graph to find neighbouring nodes
        for current_node in game_state["current_player"]["playerOccupied"]:
            #print("this is the node in the allocation stage", node)
            current_vertex_list = self.network_graph[current_node]
            #print (current_vertex_list)
            for vertex in current_vertex_list:
                count = count + 1
        print ("the number of troopps that the player will receive is", count)
        NoOfTroops = count

    def loadBoardState(self, game_state):
        board.DisplayMap()
        player1 = game_state["current_player"]
        player2 = game_state["opposition_player"]
        if game_state["current_player"]["id"] == "p2":
            player1 = game_state["opposition_player"]
            player2 = game_state["current_player"]

        for player in [player1, player2]:
            for node in self.network_graph:
                node_shape = NodeGraphic()  # instance of the Node graphics for rendering the shield, highlighting etc.
                if node in player["playerOccupied"]:
                    node_shape.pos_x = self.network_graph[node]["coords"][0]
                    node_shape.pos_y = self.network_graph[node]["coords"][1]
                    node_shape.node_network_name = node
                    node_shape.drawNode(board, player)
                    board.side_menu_right.drawTroopAllocationArea(board, player1, player2)
            pygame.display.update()
        pygame.display.update()

    def makeMove(self):
        pass

    def nearestEnemiesOfNode(self, node):

        # search to find the neighbours of a node
        # find the neighbours which are enemies
        neighbours = self.network_graph[node]["connections"]
        enemy_neighbours = []
        for neighbour in neighbours:
            if neighbour in self.opposition_player_data["playerOccupied"]:
                enemy_neighbours.append(neighbour)

        print ("the node", node )
        print ("the neighbours", neighbours)
        print("the neighbours that are enemies", enemy_neighbours)
        return enemy_neighbours

    def attack(self, game_state):
        self.side_menu_left.drawItems(board.game_display, game_state["stage"])
        self.side_menu_right.drawItems(board.game_display, game_state["stage"])
        print ("Executing Attack function")
        pass

    def fortify(self):
        pass


    def playGame(self, game_state):

        self.current_player_data = game_state["current_player"]
        self.opposition_player_data = game_state["opposition_player"]
        board.stage = game_state["stage"]
        self.network_graph = game_state["network_graph"]

        board.player_turn = game_state["current_player"]

        if board.stage == 1:
            print("confirmed stage of allocate!", game_state)
            self.allocationStage(game_state)
        elif board.stage == 2:
            print("confirmed stage of attack!")
            self.attack(game_state)
        print('0')
        self.loadBoardState(game_state)
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    self.crashed = True
                mouse = pygame.mouse.get_pos()
                #######################
                ##### MOUSE CLICKED ###
                #######################
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Was a players node selected?
                    for icon in board.icon_list:
                        if icon.x + icon.width > mouse[0] > icon.x and icon.y + icon.height > mouse[1] > icon.y:
                            # A node was selected with mouse
                            if icon.node not in self.current_player_data["playerOccupied"]:
                                # An enemy node was selected with mouse
                                if board.stage == 2:
                                    if board.mouse_selected_launch_node != "":
                                        # the launch node is present ..
                                        if icon.node in board.possible_targets:
                                            # and the enemy is reachable from the node
                                            print("Enemy selected", icon.node)
                                            board.mouse_selected_attack_node = icon.node
                                            game_state["opposition_player"]["selected_node"] = icon.node
                                            game_state["opposition_player"]["selected_node_banner"] = self.network_graph[icon.node]["banner"]
                                            print(game_state["opposition_player"]["selected_node_banner"])
                                            self.loadBoardState(game_state)
                                    else:
                                        # the launch node was missing
                                        board.mouse_selected_node = ""
                                        board.mouse_selected_attack_node = ""
                                        game_state["opposition_player"]["selected_node"] = ""
                                        game_state["opposition_player"]["selected_node_banner"] = ""
                                else:
                                    # default stage behaviour is selecting enemy node cancels current node selection
                                    board.mouse_selected_node = ""
                                    # game_state["current_player"]["selected_node_banner"] = ""
                                    # game_state["opposition_player"]["selected_node_banner"] = ""
                            else:
                                # A node of the current player was clicked on
                                if board.mouse_selected_node != icon.node:
                                    # A different node of the current player was clicked on
                                    board.mouse_selected_node = icon.node
                                    if board.stage == 2:
                                        board.mouse_selected_launch_node = icon.node
                                        game_state["current_player"]["selected_node"] = icon.node
                                        game_state["current_player"]["selected_node_banner"] = self.network_graph[icon.node]["banner"]
                                        game_state["opposition_player"]["selected_node"] = ""
                                        game_state["opposition_player"]["selected_node_banner"] = ""
                                        board.mouse_selected_attack_node = ""
                                        board.possible_targets = self.nearestEnemiesOfNode(board.mouse_selected_launch_node)

                                    self.loadBoardState(game_state)
                                else:
                                    # same node clicked again
                                    pass
                        else:
                            # mouse clicked away from any node
                            pass

                    for button in getButtonState():
                        if game_buttons[button].x + game_buttons[button].width > mouse[0] > game_buttons[button].x and game_buttons[button].y + game_buttons[button].height > mouse[1] > game_buttons[button].y:
                            # Allocate
                            if board.stage == 1:
                                if button == ("confirm" + self.current_player_data["shield"]):
                                    # Proceed to next player or next stage
                                    if self.current_player_data["id"] == "p1":
                                        game_state["opposition_player"] = self.current_player_data
                                        game_state["current_player"] = self.opposition_player_data
                                        self.playGame(game_state)
                                    else:
                                        game_state["stage"] = board.stage + 1
                                        self.playGame(game_state)
                            # Save Game
                            if button == "save":
                                self.saveGame(game_state)

                            # Quit Game
                            if button == "quit":
                                self.quitGame()



                elif event.type == pygame.KEYDOWN:
                    if board.mouse_selected_node:
                        print("selected node: " + board.mouse_selected_node)

                        if event.key == pygame.K_UP:
                            if board.stage == 1:
                                if self.current_player_data["unallocated_troops"] > 0:
                                    self.current_player_data["unallocated_troops"] = self.current_player_data["unallocated_troops"] - 1
                                    self.current_player_data["troops_at_node"][board.mouse_selected_node] = self.current_player_data["troops_at_node"][board.mouse_selected_node] + 1

                        elif event.key == pygame.K_DOWN:
                            if board.stage == 1:
                                if self.current_player_data["troops_at_node"][board.mouse_selected_node] > 1:
                                    self.current_player_data["unallocated_troops"] = self.current_player_data[ "unallocated_troops"] + 1
                                    self.current_player_data["troops_at_node"][board.mouse_selected_node] = self.current_player_data["troops_at_node"][board.mouse_selected_node] - 1
                        self.loadBoardState(game_state)
                    else:
                        print("no mouse selected node!" + board.mouse_selected_node)

def initialTroopDeployment(player):
    while player["unallocated_troops"] > 0:
        random_min = 1
        random_max = len(player["playerOccupied"])
        node_index = random.randint(random_min, random_max) - 1
        node_to_update = player["playerOccupied"][node_index]

        player["unallocated_troops"] = player["unallocated_troops"] - 1
        player["troops_at_node"][node_to_update] = player["troops_at_node"][node_to_update] + 1

    return player

def newGame(board):
    network_graph = {
        "A": {"connections": ["B"],
              "coords": [520, 25],
              "banner": "House-Whitewalker-Main-Shield.png"},
        "B": {"connections": ["A", "C", "D", "E"],
              "coords": [525, 225],
              "banner": "House-Stark-Main-Shield.png"},
        "C": {"connections": ["B", "F"],
              "coords": [371, 473],
              "banner": "House-Greyjoy-Main-Shield.png"},
        "D": {"connections": ["B", "E", "F", "G"],
              "coords": [505, 518],
              "banner": "House-Tully-Main-Shield.png"},
        "E": {"connections": ["B", "D", "G"],
              "coords": [628, 459],
              "banner": "House-Arryn-Main-Shield.png"},
        "F": {"connections": ["C", "D", "H"],
              "coords": [414, 593],
              "banner": "House-Lannister-Main-Shield.png"},
        "G": {"connections": ["D", "E", "H", "I"],
              "coords": [613, 593],
              "banner": "House-Hoare-Main-Shield.png"},
        "H": {"connections": ["F", "G", "I"],
              "coords": [468, 704],
              "banner": "House-Tyrell-Main-Shield.png"},
        "I": {"connections": ["G", "H", "J"],
              "coords": [620, 735],
              "banner": "House-Durrandon-Main-Shield.png"},
        "J": {"connections": ["H", "I"],
              "coords": [492, 853],
              "banner": "House-Main-Shield.png"}}
    player1 = {
        "id": "p1",
        "display_name": "Player One",
        "shield": "Shield 5.fw.PNG",
        "playerOccupied": ["A", "D", "E", "H", "I"],
        "unallocated_troops": 0,
        "troops_at_node": {},
        "selected_node": "",
        "selected_node_banner": ""
    }
    # player 1 initial territory allocation
    for node in player1["playerOccupied"]:
        player1["troops_at_node"][node] = 1
        player1["unallocated_troops"] = 10

    player2 = {
        "id": "p2",
        "display_name": "Player Two",
        "shield": "Shield 2.fw.PNG",
        "playerOccupied": ["B", "C", "F", "G", "J"],
        "unallocated_troops": 0,
        "troops_at_node": {},
        "selected_node": "",
        "selected_node_banner": ""
    }
    # player 2 initial territory allocation
    for node in player2["playerOccupied"]:
        player2["troops_at_node"][node] = 1
        player2["unallocated_troops"] = 10

    initial_game_state = {
        "stage": board.stage,
        "current_player": player1,
        "opposition_player": player2,
        "network_graph":  network_graph
    }
    board.player_turn = "p1"

    initial_game_state["current_player"] = initialTroopDeployment(initial_game_state["current_player"])
    initial_game_state["opposition_player"] = initialTroopDeployment(initial_game_state["opposition_player"])
    initial_game_state["stage"] = 2

    play_game = PlayGame(board)
    play_game.playGame(initial_game_state)

def loadGame(board):
    with open('test_pickle.pkl', 'rb') as pickle_in:
        game_data = pickle.load(pickle_in)
        play_game = PlayGame(board)
        play_game.playGame(game_data)


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
                            # NEW Game
                            pygame.quit()
                            board = Board()
                            play = PlayGame(board)
                            newGame(board)
                        elif button_number == 2:
                            # LOAD Game
                            pygame.quit()
                            board = Board()
                            loadGame(board)
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
