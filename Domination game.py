# Programming Project - Domination
# By Oliver Middleton

# things to do
# flow of game display
import pygame
import pickle
import random
import copy
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

class SigilBanner():
    height= 50
    width = 45

theme_got = {
    "id": "theme_got",
    "font": "./theme_got/MyDominationFont.ttf",
    "map_image": "./theme_got/GOT map 2.JPG",
    "map_width": 460,
    "map_height": 950,
    "button_background": "./theme_got/empty aged paper 30pc.jpg",
    "button_add1": "button_add1.png",
    "button_add5": "button_add5.png",
    "button_rem1": "button_remove1.png",
    "button_rem5": "button_remove5.png",
    "shield_p1": "./theme_got/Shield 5.fw.PNG",
    "shield_p2": "./theme_got/Shield 2.fw.PNG",
    "troop_area_image_p1": "./theme_got/scroll compass map 30pc.jpg",
    "troop_area_image_p2": "./theme_got/background grassy 30pc.jpg",
    "network_graph": {
        "A": {"connections": ["B"],
              "coords": [520, 25],
              "banner": "./theme_got/House-Whitewalker-Main-Shield.png"},
        "B": {"connections": ["A", "C", "D", "E"],
              "coords": [525, 225],
              "banner": "./theme_got/House-Stark-Main-Shield.png"},
        "C": {"connections": ["B", "F"],
              "coords": [371, 473],
              "banner": "./theme_got/House-Greyjoy-Main-Shield.png"},
        "D": {"connections": ["B", "E", "F", "G", "C"],
              "coords": [505, 518],
              "banner": "./theme_got/House-Tully-Main-Shield.png"},
        "E": {"connections": ["B", "D", "G"],
              "coords": [628, 459],
              "banner": "./theme_got/House-Arryn-Main-Shield.png"},
        "F": {"connections": ["C", "D", "H"],
              "coords": [414, 593],
              "banner": "./theme_got/House-Lannister-Main-Shield.png"},
        "G": {"connections": ["D", "E", "H", "I"],
              "coords": [613, 593],
              "banner": "./theme_got/House-Hoare-Main-Shield.png"},
        "H": {"connections": ["F", "G", "I", "J"],
              "coords": [468, 704],
              "banner": "./theme_got/House-Tyrell-Main-Shield.png"},
        "I": {"connections": ["G", "H", "J"],
              "coords": [620, 735],
              "banner": "./theme_got/House-Durrandon-Main-Shield.png"},
        "J": {"connections": ["H", "I"],
              "coords": [492, 853],
              "banner": "./theme_got/House-Martell-Main-Shield.png"}
    },
    "p1_occupied": ["A", "D", "E", "H", "I"],
    "p2_occupied": ["B", "C", "F", "G", "J"]
}
# theme_space = {
#     "id": "theme_space",
#     "font": "./theme_space/Deadspace.ttf",
#     "map_image": "./theme_space/Space map.JPG",
#     "map_width": 862,
#     "map_height": 1019,
#     "button_background": "./theme_space/orange_paper.jpg",
#     "button_add1": "button_add1.png",
#     "button_add5": "button_add5.png",
#     "button_rem1": "button_remove1.png",
#     "button_rem5": "button_remove5.png",
#     "shield_p1": "./theme_space/Shield 2.fw.PNG",
#     "shield_p2": "./theme_space/Shield 5.fw.PNG",
#     "troop_area_image_p1": "./theme_got/scroll compass map 30pc.jpg",
#     "troop_area_image_p2": "./theme_got/background grassy 30pc.jpg",
#     "network_graph": {
#         "A": {"connections": ["B"],
#               "coords": [414, 135],
#               "banner": "./theme_space/alien 1.png"},
#         "B": {"connections": ["A", "C", "L"],
#               "coords": [473, 204],
#               "banner": "./theme_space/alien 2.png"},
#         "C": {"connections": ["B", "D"],
#               "coords": [666, 105],
#               "banner": "./theme_space/alien 3.png"},
#         "D": {"connections": ["C", "F", "J"],
#               "coords": [756, 247],
#               "banner": "./theme_space/alien 4.png"},
#         "E": {"connections": ["F"],
#               "coords": [1044, 88],
#               "banner": "./theme_space/alien 5.png"},
#         "F": {"connections": ["E", "G"],
#               "coords": [1095, 155],
#               "banner": "./theme_space/alien 6.png"},
#         "G": {"connections": ["F", "D", "H"],
#               "coords": [1105, 219],
#               "banner": "./theme_space/alien 7.png"},
#         "H": {"connections": ["G", "I"],
#               "coords": [1087, 276],
#               "banner": "./theme_space/alien 8.png"},
#         "I": {"connections": ["H", "J"],
#               "coords": [1063, 394],
#               "banner": "./theme_space/alien 9.png"},
#         "J": {"connections": ["I"],
#               "coords": [1014, 431],
#               "banner": "./theme_space/alien 10.png"},
#         "K": {"connections": ["D", "L", "O"],
#               "coords": [697, 495],
#               "banner": "./theme_space/alien 11.png"},
#         "L": {"connections": ["K", "M"],
#               "coords": [650, 536],
#               "banner": "./theme_space/alien 12.png"},
#         "M": {"connections": ["B", "L", "N"],
#               "coords": [606, 568],
#               "banner": "./theme_space/alien 13.png"},
#         "N": {"connections": ["M", "O"],
#               "coords": [540, 861],
#               "banner": "./theme_space/alien 14.png"},
#         "O": {"connections": ["K", "N"],
#               "coords": [859, 807],
#               "banner": "./theme_space/alien 15.png"}
#     },
#     "p1_occupied": ["A", "C", "E", "G", "I", "K", "M"],
#     "p2_occupied": ["B", "D", "F", "H", "J", "L", "N", "O"]
# }

# default theme
game_theme = theme_got

def setTheme(new_theme):
    game_theme = new_theme

class CustomFont():
    def __init__(self):
        pygame.font.init()
        domination_font = game_theme["font"]
        self.splash_title = pygame.font.Font(domination_font, 50)
        self.splash_button = pygame.font.Font(domination_font, 30)
        self.menu_heading = pygame.font.Font(domination_font, 30)
        self.menu_title = pygame.font.Font(domination_font, 20)
        self.menu_action = pygame.font.Font(domination_font, 15)
        self.menu_button = pygame.font.Font(domination_font, 30)


class PlayLoadGameMenu():
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

        # An initial array of identical buttons
        for i in range(3):
            button_text_no = button_text_no + 1
            text_pos_y = y + 20
            self.button_list.append(Button(x, y, self.game_display))

            if button_text_no == 1:
                text_surface = domination_font.splash_button.render("New GOT Game", False, Colour.white)
                self.game_display.blit(text_surface, (text_pos_x, text_pos_y))

            # elif button_text_no == 2:
            #     text_surface = domination_font.splash_button.render("New Space Game", False, Colour.white)
            #     self.game_display.blit(text_surface, (text_pos_x, text_pos_y))

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
        self.picture = pygame.image.load(game_theme["button_background"])
        self.button_id = ""

    def drawButton(self, surface, background_image, btn_width, btn_height, btn_x, btn_y, btn_text, btn_id):
        self.picture = pygame.image.load(background_image)
        self.picture = pygame.transform.scale(self.picture, (btn_width, btn_height))
        self.button_id = btn_id
        self.button_rectangle = self.picture.get_rect()
        self.button_rectangle = self.button_rectangle.move(btn_x, btn_y)
        if all(char.isalpha() for char in str(btn_text)):
            btn_label = self.domination_font.menu_button.render(btn_text, False, self.text_on_paper)
        else:
            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            btn_label = myfont.render(str(btn_text), False, self.text_on_paper)

        surface.blit(self.picture, self.button_rectangle)

        btn_label_x = centreJustifyButton(self.button_rectangle.x, self.button_rectangle.width, btn_label)
        btn_label_y = verticalJustifyButton(self.button_rectangle.y, self.button_rectangle.height, btn_label)
        surface.blit(btn_label, (btn_label_x, btn_label_y))
        setButtonState("add", btn_id, self.button_rectangle)  #used to add and remove buttons from view

class PaperTroopArea():
    def __init__(self):
        # defaults
        self.button_rectangle = (0, 0, 0, 0)
        self.save_text_x = 0
        self.save_text_y = 0
        self.btn_label = ""
        self.text_on_paper = Colour.black
        self.domination_font = CustomFont()
        self.picture = pygame.image.load(game_theme["button_background"])
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
        btn_background = game_theme["button_background"]
        btn_save = PaperButton()
        btn_save.drawButton(surface, btn_background, self.menu_button_width, self.menu_button_height, self.x_pos_menu_buttons_container_indent, self.y_pos_menu_buttons_container_top, "Save", "save")
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
        self.domination_font = CustomFont()

        # Player Troop area
        self.troop_area_indent_from_left = 0
        self.troop_area_indent_from_top = 60
        self.troop_area_width = 0
        self.troop_area_height = 300
        self.troop_area_xpos = 0
        self.troop_area_ypos = 0
        self.text_on_troop_area = Colour.black
        self.shield_square_height = self.domination_font.menu_button.get_height()
        self.shield_square_width = self.shield_square_height

        ## Sigil
        self.sigil_width = SigilBanner.width
        self.sigil_height = SigilBanner.height
        self.sigil_spacer = 10  # gap between army stack
        self.army_index_new_row = 0  # set to zero to start army drawing a new row
        self.army_index_row = 0  # track the row to draw the troops on

        # btn confirm to next stage
        self.btn_confirm_indent_from_left = 60
        self.btn_confirm_indent_from_bottom = 60
        self.btn_confirm_background = game_theme["button_background"]
        self.btn_confirm_width = 200
        self.btn_confirm_height = 75

    def drawTroopArea(self, board, player, pos_x, pos_y):
        self.troop_area_width = board.side_menu_right.menu_width
        self.troop_area_xpos = pos_x
        self.troop_area_ypos = pos_y
        players_shield_img = pygame.image.load(player["shield"])
        players_shield_img = pygame.transform.scale(players_shield_img, (self.shield_square_width , self.shield_square_height))
        shield_rectangle = players_shield_img.get_rect()
        shield_rectangle = shield_rectangle.move(self.troop_area_xpos, self.troop_area_ypos)
        board.game_display.blit(players_shield_img, shield_rectangle)
        player_text = self.domination_font.menu_button.render(player["display_name"], False, self.text_on_troop_area)
        board.game_display.blit(player_text, (self.troop_area_xpos + self.shield_square_width, self.troop_area_ypos))

        ## Troop Stack
        if player["selected_node"] != "":
            if board.stage <= 2:
                armies_at_this_node = player["troops_at_node"][player["selected_node"]]
                army_count_text_size = round(self.sigil_height / 1.5)
                army_count_font = pygame.font.SysFont("Comic Sans MS", army_count_text_size)
                max_renderable_armies = 32
                army_display_spaces = min(max_renderable_armies, armies_at_this_node)  # don't render more than 32 armies
                army_count_display = str(armies_at_this_node)

                players_launch_army_img = pygame.image.load(player["selected_node_banner"])
                players_launch_army_img = pygame.transform.scale(players_launch_army_img, (self.sigil_width, self.sigil_height))
                sigil_xpos_spacer = self.sigil_width + self.sigil_spacer
                sigil_ypos_spacer = self.sigil_height + self.sigil_spacer

                for army_index in range(army_display_spaces):
                    ## Stack the Sigils
                    if player["selected_node_banner"]:
                        # spaced along x
                        sigil_xpos = pos_x + (army_index - self.army_index_new_row) * sigil_xpos_spacer
                        sigil_ypos = pos_y + self.shield_square_height + self.sigil_spacer + self.army_index_row * sigil_ypos_spacer
                        # rowed down y
                        if sigil_xpos + 2 * sigil_xpos_spacer > self.troop_area_xpos + self.troop_area_width:
                            self.army_index_new_row = army_index
                            self.army_index_row = self.army_index_row + 1
                            sigil_xpos = pos_x + (army_index - self.army_index_new_row) * sigil_xpos_spacer
                            sigil_ypos = pos_y + self.shield_square_height + + self.sigil_spacer + self.army_index_row * sigil_ypos_spacer

                        # dray army item
                        sigil_rectangle = players_launch_army_img.get_rect()
                        sigil_rectangle = sigil_rectangle.move(sigil_xpos, sigil_ypos)
                        board.game_display.blit(players_launch_army_img, sigil_rectangle)

                        # display the army size
                        if army_index == army_display_spaces - 1:
                            if armies_at_this_node > max_renderable_armies:
                                army_count_display = ".." + army_count_display  ## > max renderable
                            army_count_surface = army_count_font.render(army_count_display, False, Colour.black)
                            board.game_display.blit(army_count_surface, (sigil_xpos + sigil_xpos_spacer, sigil_ypos))

        ## Confirm Allocate Button
        if board.stage == 1:
            btn_confirm_xpos = self.troop_area_xpos + board.side_menu_right.menu_width - self.btn_confirm_width
            btn_confirm_ypos = self.troop_area_ypos + self.troop_area_height - self.btn_confirm_height
            btn_id = "confirm" + player["shield"]
            if player["unallocated_troops"] == 0:
                if player["display_name"] == "Available Troops":
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
        self.menu_width = 500
        self.menu_height = menu_height

        # Side Menu Right Title
        self.menu_title_height = 60

        # Troop Area
        self.troop_area_background = game_theme["troop_area_image_p1"]
        troop_area_indent_from_left = 0
        self.troop_area_height = 300
        troop_area_indent_from_top = self.menu_title_height
        self.player_troop_banner_width = 100
        self.player_troop_banner_height = 100
        self.troop_area_gap_height = 60

        self.top_troop_area_xpos = self.menu_xpos + troop_area_indent_from_left
        self.top_troop_area_ypos = self.menu_ypos + troop_area_indent_from_top
        self.troop_area_gap_xpos = self.menu_xpos + troop_area_indent_from_left
        self.troop_area_gap_ypos = self.menu_ypos + troop_area_indent_from_top + self.troop_area_height
        self.lower_troop_area_xpos = self.menu_xpos + troop_area_indent_from_left
        self.lower_troop_area_ypos = self.menu_ypos + troop_area_indent_from_top + self.troop_area_height + self.troop_area_gap_height
        self.lower_troop_banner_xpos = self.menu_xpos + troop_area_indent_from_left
        self.lower_troop_banner_ypos = self.menu_ypos + troop_area_indent_from_top + self.troop_area_height + self.troop_area_gap_height
        self.btn_attack_xpos = self.menu_xpos + troop_area_indent_from_left
        self.btn_attack_ypos = self.menu_ypos + troop_area_indent_from_top + 2 * self.troop_area_height + self.troop_area_gap_height
        self.btn_attack_height = 60
        self.btn_attack_background = game_theme["button_background"]

    def drawItems(self, surface, stage):
        domination_font = CustomFont()
        stage_text = ""
        pygame.draw.rect(surface, self.initial_colour,(self.menu_xpos, self.menu_ypos, self.menu_width, self.menu_height))
        if stage == 1:
            stage_text = "Allocate troops"
            inbetween_text = domination_font.menu_heading.render("ADD REMOVE", False, Colour.white)
            surface.blit(inbetween_text, (centreJustifyButton(self.menu_xpos, self.menu_width, inbetween_text), verticalJustifyButton(self.troop_area_gap_ypos, self.troop_area_gap_height, inbetween_text)))

        elif stage == 2:
            stage_text = "Prepare the Attack"
            inbetween_text = domination_font.menu_heading.render("Vs", False, Colour.white)
            surface.blit(inbetween_text, (centreJustifyButton(self.menu_xpos, self.menu_width, inbetween_text), verticalJustifyButton(self.troop_area_gap_ypos, self.troop_area_gap_height, inbetween_text)))

        header_text1 = domination_font.menu_heading.render(stage_text, False, Colour.white)
        surface.blit(header_text1, (centreJustifyButton(self.menu_xpos, self.menu_width, header_text1), 5))

    def drawTroopAllocationArea(self, board, game_state):
        top_troop_area_backing = PaperTroopArea()
        lower_troop_area_backing = PaperTroopArea()
        backing_text_p1 = ""
        backing_text_p2 = ""
        if board.stage == 1:
            # ADD REMOVE troops Controls
            # Putting troops on the bench if they are unallocated.
            bench_state = copy.deepcopy(game_state["current_player"])
            bench_state["display_name"] = "Available Troops"
            bench_state["selected_node_banner"] = bench_state["shield"]
            if bench_state["selected_node"] != "":
                bench_state["troops_at_node"][bench_state["selected_node"]] = bench_state["unallocated_troops"]
            btn_gap_between_width = 20
            btn_in_gap_width = 40
            btn_add5_id = "add5"
            btn_add1_id = "add1"
            btn_rem1_id = "rem1"
            btn_rem5_id = "rem5"
            btn_add_five_xpos = self.troop_area_gap_xpos
            btn_add_one_xpos = self.troop_area_gap_xpos + btn_in_gap_width + btn_gap_between_width
            btn_rem_one_xpos = self.troop_area_gap_xpos + self.menu_width - btn_in_gap_width - btn_gap_between_width - btn_in_gap_width
            btn_rem_five_xpos = self.troop_area_gap_xpos + self.menu_width - btn_in_gap_width
            btn_add_five = PaperButton()
            btn_add_one = PaperButton()
            btn_rem_one = PaperButton()
            btn_rem_five = PaperButton()
            btn_add_five.drawButton(board.game_display, game_theme["button_add5"], btn_in_gap_width, self.troop_area_gap_height, btn_add_five_xpos, self.troop_area_gap_ypos, "", btn_add5_id)
            btn_add_one.drawButton(board.game_display, game_theme["button_add1"], btn_in_gap_width, self.troop_area_gap_height, btn_add_one_xpos,  self.troop_area_gap_ypos, "", btn_add1_id)
            btn_rem_one.drawButton(board.game_display, game_theme["button_rem1"], btn_in_gap_width, self.troop_area_gap_height, btn_rem_one_xpos,  self.troop_area_gap_ypos, "", btn_rem1_id)
            btn_rem_five.drawButton(board.game_display, game_theme["button_rem5"], btn_in_gap_width, self.troop_area_gap_height, btn_rem_five_xpos,  self.troop_area_gap_ypos, "", btn_rem5_id)
            top_troop_area_backing.drawArea(board.game_display, game_state["current_player"]["troop_area_background"], self.menu_width, self.troop_area_height, self.top_troop_area_xpos, self.top_troop_area_ypos, backing_text_p1)
            lower_troop_area_backing.drawArea(board.game_display, game_state["current_player"]["troop_area_background"], self.menu_width, self.troop_area_height, self.lower_troop_area_xpos, self.lower_troop_area_ypos, backing_text_p2)
            top_troop_area = TroopArea()
            lower_troop_area = TroopArea()
            top_troop_area.drawTroopArea(board, game_state["current_player"], self.top_troop_area_xpos, self.top_troop_area_ypos)
            lower_troop_area.drawTroopArea(board, bench_state, self.lower_troop_area_xpos, self.lower_troop_area_ypos)
        elif board.stage == 2:
            if game_state["current_player"]["selected_node"] != "" and game_state["opposition_player"]["selected_node"] != "":
                ## Confirm Attack Button
                btn_attack = PaperButton()
                btn_id = "attack"
                btn_attack.drawButton(board.game_display, self.btn_attack_background, self.menu_width, self.btn_attack_height, self.btn_attack_xpos, self.btn_attack_ypos, "Attack", btn_id)
            else:
                # Redraw self to remove "attack" button
                self.drawItems(board.game_display, board.stage)
            top_troop_area_backing.drawArea(board.game_display, game_state["current_player"]["troop_area_background"], self.menu_width, self.troop_area_height, self.top_troop_area_xpos, self.top_troop_area_ypos, backing_text_p1)
            lower_troop_area_backing.drawArea(board.game_display, game_state["opposition_player"]["troop_area_background"], self.menu_width, self.troop_area_height, self.lower_troop_area_xpos, self.lower_troop_area_ypos, backing_text_p2)
            player1_troop_area = TroopArea()
            player2_troop_area = TroopArea()
            player1_troop_area.drawTroopArea(board, game_state["current_player"], self.top_troop_area_xpos, self.top_troop_area_ypos)
            player2_troop_area.drawTroopArea(board, game_state["opposition_player"], self.lower_troop_area_xpos, self.lower_troop_area_ypos)

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
            # print("Available to select", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_available, highlight_rectangle, self.highlight_border_thickness)
        # Selected
        if self.node_network_name == board.mouse_selected_node:
            # print("Selected", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_selected, highlight_rectangle)
        # Possible Enemy Node
        if self.node_network_name in board.possible_targets:
            # print("Possible Enemy", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_enemy, highlight_rectangle, self.highlight_border_thickness)
        # Selected Enemy Node
        if self.node_network_name == board.mouse_selected_attack_node:
            # print("Selected Enemy", self.node_network_name)
            pygame.draw.rect(board.game_display, self.highlight_border_colour_enemy, highlight_rectangle)

        board.game_display.blit(pygame.image.load(player["shield"]), (self.pos_x, self.pos_y))
        myfont = pygame.font.SysFont("Comic Sans MS", 20)
        text_surface = myfont.render(str(player["troops_at_node"][self.node_network_name]), False, Colour.white)
        board.game_display.blit(text_surface, (centreJustifyButton(self.pos_x, self.width, text_surface), self.pos_y + round(self.height / 2)))

class Board():
    def __init__(self):

        # Side menu left
        self.side_menu_left = SideMenuLeft()
        self.side_menu_right = SideMenuRight(0,0,0)

        # Board
        self.theme = game_theme
        self.board_width = game_theme["map_width"]  # width of map jpg
        self.board_height = game_theme["map_height"]  # height of map jpg
        self.stage = 1
        self.player_turn = ""
        self.possible_targets = []

        # Icon information
        self.icon_colour = Colour.medium_blue
        self.icon_list = []

    def renderLayout(self):
        self.theme = game_theme
        self.board_position_x = 0 + self.side_menu_left.menu_width
        self.board_position_y = 0

        # Side menu right
        self.side_menu_right_position_x = 0 + self.side_menu_left.menu_width + self.board_width
        self.side_menu_right_position_y = 0
        self.side_menu_right = SideMenuRight(self.side_menu_right_position_x, self.side_menu_right_position_y, self.board_height)

        # Display  size
        self.display_width = self.side_menu_left.menu_width + self.board_width + self.side_menu_right.menu_width
        self.display_height = max(self.side_menu_left.menu_container_height, self.board_height, self.side_menu_right.menu_height)

        # setting up the display
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Domination Game!')
        self.game_display.fill(Colour.darkGrey)
        self.clock = pygame.time.Clock()
        ######
        self.side_menu_left.drawItems(self.game_display, self.stage)
        self.side_menu_right.drawItems(self.game_display, self.stage)
        self.setUpIcons()
        self.DisplayMap(self.theme)
        pygame.display.update()

        # mouse
        self.mouse_selected_node = ""
        self.mouse_selected_launch_node = ""
        self.mouse_selected_attack_node = ""


    def setUpMenuButtons(self):
        pass

    def setUpIcons(self):
        # X and Y coordinates of each icon
        for key in game_theme["network_graph"]:
            print ('setupIons', key)
            x = game_theme["network_graph"][key]["coords"][0]
            y = game_theme["network_graph"][key]["coords"][1]
            self.icon_list.append(Icon(self.icon_colour, x, y, key, 'Shield1.fw.PNG'))


    def setUpMenuButtons(self):
        pass

    def DisplayMap(self, game_theme):
        # loading the map
        print(game_theme)
        map_width = game_theme["map_width"]
        map_height = game_theme["map_height"]
        map_img = pygame.image.load(game_theme["map_image"])

        map_img = pygame.transform.scale(map_img, (map_width, map_height))
        self.game_display.blit(map_img, (self.board_position_x, self.board_position_y))

        pygame.display.update()

        return self

class PlayGame():
    def __init__(self, board):

        # side menu assistance variables
        self.network_graph = game_theme["network_graph"]
        self.current_player_data = {}
        self.opposition_player_data = {}

        # Variables used to store player turns
        self.player1_turns = 0
        self.player2_turns = 0

        self.crashed = False
        self.board = board
        self.side_menu_left = board.side_menu_left
        self.side_menu_right = board.side_menu_right

        board.renderLayout()



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
        board.DisplayMap(game_state["game_theme"])
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
            board.side_menu_right.drawTroopAllocationArea(board, game_state)
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

        print("the node", node )
        print("the neighbours", neighbours)
        print("the neighbours that are enemies", enemy_neighbours)
        return enemy_neighbours

    def fight(self, game_state):
        # need player 1 vs player 2
        # need to find selected nodes
        # get number of troops on each node
        # randomly work out which army wins
        # get army sizes

        attacking_army_size = self.current_player_data["troops_at_node"][self.current_player_data["selected_node"]]
        defending_army_size = self.opposition_player_data["troops_at_node"][self.opposition_player_data["selected_node"]]
        print(attacking_army_size, defending_army_size)

        # dice roll generator
        def getDiceRollsFor(army_size):
            dice_array = []
            for i in range(army_size):
                dice_number = random.randint(1,100)
                dice_array.append(dice_number)
            return dice_array

        # compare dice roll arrays
        def compareDiceRolls(attacking_size, defending_size):
            attacking_dice_rolls = getDiceRollsFor(attacking_size)
            defending_dice_rolls = getDiceRollsFor(defending_size)

            for battle in range((min(attacking_size, defending_size))):
                if attacking_dice_rolls[battle] >= defending_dice_rolls[battle]:
                    defending_size = defending_size - 1
                else:
                    attacking_size = attacking_size - 1
                if attacking_size <= 2 or defending_size == 0:
                    break

            return attacking_size, defending_size

        finished_fighting = False
        while not finished_fighting:
            # spot the defeat conditions
            if (attacking_army_size == 2 and defending_army_size < attacking_army_size) or defending_army_size == 0:
                finished_fighting = True
            elif attacking_army_size == 1 and defending_army_size > attacking_army_size:
                finished_fighting = True
            else:
                # nobody defeated, roll dice again (recursion)
                attacking_army_size, defending_army_size = compareDiceRolls(attacking_army_size, defending_army_size)

        # set result of battle to update display
        if attacking_army_size > defending_army_size:
            self.current_player_data["playerOccupied"].append(self.opposition_player_data["selected_node"])
            self.opposition_player_data["playerOccupied"].remove(self.opposition_player_data["selected_node"])
            self.current_player_data["troops_at_node"][self.current_player_data["selected_node"]] = attacking_army_size - 1
            self.current_player_data["troops_at_node"][self.opposition_player_data["selected_node"]] = 1
            del self.opposition_player_data["troops_at_node"][self.opposition_player_data["selected_node"]]

        else:
            self.current_player_data["troops_at_node"][self.current_player_data["selected_node"]] = 1
            self.opposition_player_data["troops_at_node"][self.opposition_player_data["selected_node"]] = defending_army_size

        self.current_player_data["selected_node"] = ""
        self.current_player_data["selected_node_banner"] = ""
        self.opposition_player_data["selected_node"] = ""
        self.opposition_player_data["selected_node_banner"] = ""
        game_state["current_player"] = self.current_player_data
        game_state["opposition_player"] = self.opposition_player_data

        print(game_state["stage"])
        game_state["stage"] = 3
        board.mouse_selected_node = ""
        board.mouse_selected_attack_node = ""
        board.mouse_selected_launch_node = ""
        board.possible_targets = []

        self.loadBoardState(game_state)
        self.renderStage(game_state)

    def renderStage(self, game_state):
        self.side_menu_left.drawItems(board.game_display, game_state["stage"])
        self.side_menu_right.drawItems(board.game_display, game_state["stage"])
        print("Executing ", game_state["stage"], " function")
        pass

    def fortify(self, game_state):

        for current_node in game_state["current_player"]["playerOccupied"]:
           pass


    def playGame(self, game_state):

        self.current_player_data = game_state["current_player"]
        self.opposition_player_data = game_state["opposition_player"]
        board.stage = game_state["stage"]
        self.network_graph = game_state["network_graph"]

        board.player_turn = game_state["current_player"]
        board.theme = game_state["game_theme"]

        if board.stage == 1:
            print("confirmed stage of allocate!", game_state)
            self.allocationStage(game_state)
        elif board.stage == 2:
            print("confirmed stage of attack!", game_state)
            self.renderStage(game_state)
        elif board.stage == 3:
            print("confirm stage of fortify!", game_state)
            # self.renderStage(game_state)
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
                    mouse = pygame.mouse.get_pos()
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
                                        self.loadBoardState(game_state)
                                else:
                                    # default stage behaviour is selecting enemy node cancels current node selection
                                    board.mouse_selected_node = ""
                                    # game_state["current_player"]["selected_node_banner"] = ""
                                    # game_state["opposition_player"]["selected_node_banner"] = ""
                            else:
                                # A node of the current player was clicked on
                                game_state["current_player"]["selected_node"] = icon.node
                                game_state["current_player"]["selected_node_banner"] = self.network_graph[icon.node]["banner"]

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
                                    elif board.stage == 3:
                                        pass

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

                            # Attack
                            if board.stage == 2:
                                if button == "attack":
                                    self.fight(game_state)
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
    player1 = {
        "id": "p1",
        "display_name": "Player One",
        "shield": game_theme["shield_p1"],
        "playerOccupied": game_theme["p1_occupied"],
        "unallocated_troops": 0,
        "troops_at_node": {},
        "selected_node": "",
        "selected_node_banner": "",
        "troop_area_background": game_theme["troop_area_image_p1"]
    }
    # player 1 initial territory allocation
    for node in player1["playerOccupied"]:
        player1["troops_at_node"][node] = 1
        player1["unallocated_troops"] = 125

    player2 = {
        "id": "p2",
        "display_name": "Player Two",
        "shield": game_theme["shield_p2"],
        "playerOccupied": game_theme["p2_occupied"],
        "unallocated_troops": 0,
        "troops_at_node": {},
        "selected_node": "",
        "selected_node_banner": "",
        "troop_area_background": game_theme["troop_area_image_p2"]
    }
    # player 2 initial territory allocation
    for node in player2["playerOccupied"]:
        player2["troops_at_node"][node] = 1
        player2["unallocated_troops"] = 130

    initial_game_state = {
        "stage": board.stage,
        "current_player": player1,
        "opposition_player": player2,
        "network_graph":   game_theme["network_graph"],
        "game_theme": game_theme
    }
    board.player_turn = "p1"

    initial_game_state["current_player"] = initialTroopDeployment(initial_game_state["current_player"])
    initial_game_state["opposition_player"] = initialTroopDeployment(initial_game_state["opposition_player"])
    initial_game_state["stage"] = 1

    play_game = PlayGame(board)
    play_game.playGame(initial_game_state)

def loadGame(board):
    with open('test_pickle.pkl', 'rb') as pickle_in:
        game_data = pickle.load(pickle_in)
        print('load', game_data)
        game_theme = game_data["game_theme"]
        board.theme = game_theme
        board.board_width = game_theme["map_width"]
        board.board_height = game_theme["map_height"]
        play_game = PlayGame(board)
        play_game.playGame(game_data)


if __name__ == "__main__":

    pygame.init()
    colour = Colour()
    menu = PlayLoadGameMenu()
    # icons = Icons()
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
                # sort out the button numbers, use iterative statements to define the button number// which button was pressed
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
                            game_theme = theme_got
                            board = Board()
                            play = PlayGame(board)
                            newGame(board)
                        # elif button_number == 2:
                        #     # NEW Game
                        #     pygame.quit()
                        #     game_theme = theme_space
                        #     board = Board()
                        #     play = PlayGame(board)
                        #     newGame(board)
                        elif button_number == 3:
                            # LOAD Game
                            pygame.quit()
                            board = Board()
                            loadGame(board)
                            pass
                        elif button_number == 4:
                            pygame.quit()
                            instructions = Instructions()
                            pygame.display.update()
                    else:
                        button_min_y = button_min_y + 100
                        button_max_y = button_max_y + 100
    # pygame.draw.rect(menu.gameDisplay,colour.red, (self.x,self.y,self.width,self.height))

    pygame.display.update()
    clock.tick(60)
