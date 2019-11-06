import pygame
from gamefiles import locations
import time
from gamefiles import ui

# Initialize
pygame.init()
pygame.display.set_caption("Artheus")

# Resolution
Screen_Width, Screen_Height = 1000, 700
win = pygame.display.set_mode((Screen_Width, Screen_Height))

# Shape and size
Shape_Width, Shape_Height = 100, 100
Shape_X, Shape_Y = (Screen_Width / 2) - (Shape_Width / 2), (Screen_Height / 2) - (Shape_Height / 2)
Shape = "Rectangle"

# Colors
Red, Green, Blue = 55, 100, 200

# State of the Player
Fame = 0
place = "Outside"


# Class definition
class Move:
    def __init__(self, direction, name):
        self.direction = direction
        self.name = name

    def return_direction(self):
        return self.direction

    def return_name(self):
        return self.name


house = Move("house", "house")
mayor = Move("mayor", "mayor")
all_locations = {'house': house, 'mayor': mayor}


class Location:
    """This Class is used for handling the position where you are and what you can do
    and where you can
    Context_list is used to store every possible direction displayed
    location index is just to move between this list
    """
    def __init__(self, location_name, context_list):
        self.location_name = location_name
        self.context_list = context_list
        self.location_index = 1
        self.max_index = len(context_list)

    def return_context_name(self):
        current_selection = self.context_list[self.location_index]
        if isinstance(current_selection, Move):
            return current_selection.name
        else:
            return current_selection.name

    def return_context(self):
        current_selection = self.context_list[self.location_index]
        print(str(type(current_selection)) + "Type context")
        return current_selection


beginning = Location("Beginning", [house, mayor])
actual_location = beginning


# Ui
def display_text(message, y_position):
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(message, True, (20, 60, 255))
    textrect = text.get_rect()
    textrect.center = (Screen_Width // 2, y_position)
    win.blit(text, textrect)


def draw_ui():
    pygame.draw.polygon(win, (250, 250, 250), [(300, 600), (350, 650), (350, 550)])
    pygame.draw.polygon(win, (250, 250, 250), [(700, 600), (650, 650), (650, 550)])
    pygame.draw.rect(win, (180, 180, 180), (360, 575, 280, 55))
    pygame.draw.rect(win, [255, 0, 0], [Shape_X - Shape_Width/2, Shape_Y - Shape_Height/2, Shape_Width*2, Shape_Height*2], 1)
    pygame.draw.rect(win, (180, 180, 180), (360, 25, 280, 50))
    display_text(place, 50)


def draw_rectangle():
    pygame.draw.rect(win, (Red, Green, Blue), (Shape_X, Shape_Y, Shape_Width, Shape_Height))


# Controls
def button_index(index):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    hasclicked = False


# Left arrow clickable
    if 300 < mouse[0] < 350 and 550 < mouse[1] < 650:
        pygame.draw.polygon(win, (100, 200, 200), [(300, 600), (350, 650), (350, 550)])
        if click[0] == 1 and not hasclicked:
            if not index == 0:
                index -= 1
            else:
                index = actual_location.max_index - 1
            hasclicked = True

# Right arrow clickable
    elif 700 > mouse[0] > 650 > mouse[1] > 550:
        pygame.draw.polygon(win, (100, 200, 200), [(700, 600), (650, 650), (650, 550)])
        if click[0] == 1 and not hasclicked:
            if not index == actual_location.max_index - 1:
                index += 1
            else:
                index = 0
                hasclicked = True
    return index


# Menu between arrows
def button_action(pre_context,location):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    new_context = pre_context
    hasclicked = False

    if 360 < mouse[0] < 640 and 575 < mouse[1] < 630:
        pygame.draw.rect(win, (255, 255, 255), (360, 575, 280, 55))

        if click[0] == 1 and not hasclicked:
            print("Clicked")
            if isinstance(pre_context, Move):
                pre_context = pre_context
            else:
                pre_context = pre_context

        else:
            pre_context = pre_context

    return pre_context



# While loop
run = True
while run:
    pygame.time.delay(100)
    draw_ui()
    actual_location.location_index = button_index(actual_location.location_index)
    print(str(type(actual_location)) + "location before")
    actual_location = button_action(actual_location.return_context(), actual_location)
    print(str(type(actual_location)) + "location after")
    display_text(actual_location.return_context_name(), 600)
    pygame.display.update()

# Common code

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
pygame.display.quit()
pygame.quit()











