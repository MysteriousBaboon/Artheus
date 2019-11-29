import pygame
import time
from gamefiles import locations as location

# Resolution (Compare current aspect ratio with 1280/720 and will scale all the UI with this value
screen_width, screen_height = 1280, 720
ratio_width, ratio_height = screen_width / 1280.0, screen_height / 720.0
win = pygame.display.set_mode((screen_width, screen_height))

# Shape and size
shape_width, shape_height = 100, 100
shape_X, shape_Y = (screen_width / 2) - (shape_width / 2), (screen_height / 2) - (shape_height / 2)

# Player info
place = "None"
istalking = "False"

# Click handling
click = pygame.mouse.get_pressed()
mouse = pygame.mouse.get_pos()
click_state = "Released"

# Dialogues List which will be used by the typewriter
lines = ["",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         ]

actual_line = 0


########################################################################################################################
# Draw Dialogue will be used for the chatbox, display text will be used for the different context(Top,Soul,Bot)
def draw_dialogue(message):
    # Handle UI and Font
    pygame.draw.rect(win, [60, 60, 60], (20, 375, 240, 300), 0)
    pygame.draw.rect(win, [30, 30, 30], (20, 375, 240, 300), 3)
    font = pygame.font.SysFont("Arial", 16, bold=False)

    # Navigate through the list
    i = 0
    while i < len(lines):
        if actual_line == 12:
            if i == 12:
                pass
            else:
                lines[i] == i + 1
        text = font.render(lines[i], True, (200, 200, 200))
        pygame.display.update()
        textrect = text.get_rect()
        textrect.midleft = (25, 390 + i * 20)
        win.blit(text, textrect)
        i += 1

    def type_writer(font):
        global actual_line
        for char in message:
            if font.render(lines[actual_line] + char, True, (200, 200, 200)).get_width() > 230:
                actual_line += 1

            time.sleep(0.1)
            lines[actual_line] += char
            text = font.render(lines[actual_line], True, (200, 200, 200))
            pygame.display.update()
            textrect = text.get_rect()
            textrect.midleft = (25, 390 + actual_line * 20)
            win.blit(text, textrect)
        actual_line += 1

    if message != "None":
        type_writer(font)


def display_text(message, y_position, size, color):
    font = pygame.font.Font("font.ttf", size)
    text = font.render(message, True, color)
    textrect = text.get_rect()
    textrect.center = (screen_width // 2, y_position)
    win.blit(text, textrect)


########################################################################################################################
# Ui
def draw_chat():
    # Text Box UI
    pygame.draw.rect(win, [60, 60, 60], (20, 375, 240, 300), 0)
    pygame.draw.rect(win, [30, 30, 30], (20, 375, 240, 300), 3)


def draw_top_context():
    # Top UI
    pygame.draw.rect(win, (73, 76, 84), (500 * ratio_width, 25 * ratio_height,
                                         280 * ratio_width, 50 * ratio_height))
    pygame.draw.rect(win, (36, 36, 36), (500 * ratio_width, 25 * ratio_height,
                                         280 * ratio_width, 50 * ratio_height), 5)

    display_text(place, 45 * ratio_height, int(32 * ratio_height), (0, 27, 145))


def draw_bot_context():
    # Bot UI display (Arrows, action button)
    pygame.draw.polygon(win, (250, 250, 250), [(425 * ratio_width, 600 * ratio_height),
                                               (475 * ratio_width, 650 * ratio_height),
                                               (475 * ratio_width, 550 * ratio_height)])
    pygame.draw.polygon(win, (250, 250, 250), [(850 * ratio_width, 600 * ratio_height),
                                               (800 * ratio_width, 650 * ratio_height),
                                               (800 * ratio_width, 550 * ratio_height)])

    if 425 * ratio_width < mouse[0] < 475 * ratio_width and 550 * ratio_height < mouse[1] < 650 * ratio_height:
        pygame.draw.polygon(win, (100, 200, 200), [(425 * ratio_width, 600 * ratio_height),
                                                   (475 * ratio_width, 650 * ratio_height),
                                                   (475 * ratio_width, 550 * ratio_height)])
    elif 850 * ratio_width > mouse[0] > 800 * ratio_width and 550 * ratio_height < mouse[1] < 650 * ratio_height:
        pygame.draw.polygon(win, (100, 200, 200), [(850 * ratio_width, 600 * ratio_height),
                                                   (800 * ratio_width, 650 * ratio_height),
                                                   (800 * ratio_width, 550 * ratio_height)])

    pygame.draw.rect(win, (150, 150, 150), (500 * ratio_width, 570 * ratio_height,
                                            280 * ratio_width, 70 * ratio_height))
    pygame.draw.rect(win, (36, 36, 36), (500 * ratio_width, 570 * ratio_height,
                                         280 * ratio_width, 70 * ratio_height), 3)
    display_text(location.actual.return_context_name(), 600 * ratio_height, int(32 * ratio_height), (255, 255, 255))


def draw_shape_ui():
    # Shape UI
    pygame.draw.rect(win, [150, 150, 150], [490 * ratio_width, 150 * ratio_height, 300 * ratio_width,
                                            300 * ratio_height], 0)
    pygame.draw.rect(win, [140, 10, 0], [490 * ratio_width, 150 * ratio_height, 300 * ratio_width,
                                         300 * ratio_height], 4)
    location.Character_Test.draw_soul()
    display_text(location.Character_Test.name, 480 * ratio_height, 44, (255, 255, 255))
    draw_right_context()


def draw_right_context():
    i = 0
    ii = 0
    right_context_lines = location.Character_Test.dialogues
    while i < len(right_context_lines):
        if isinstance(right_context_lines[i], str):
            font = pygame.font.Font("freesansbold.ttf", 16)
            text = font.render(right_context_lines[i], True, (20, 60, 255))
            textrect = text.get_rect()
            textrect.center = (800, 300 + 20 * ii)
            win.blit(text, textrect)
            ii += 1
        else:
            right_context_lines[i]()
        i += 1


########################################################################################################################
# Controls
def button_index(index):
    # Left arrow clickable
    if 425 * ratio_width < mouse[0] < 475 * ratio_width and 550 * ratio_height < mouse[1] < 650 * ratio_height:
        if click_state == "Pressed":
            if not index == 0:
                index -= 1
            else:
                index = location.actual.max_index - 1
            hasclicked = True

    # Right arrow clickable
    elif 850 * ratio_width > mouse[0] > 800 * ratio_width and 550 * ratio_height < mouse[1] < 650 * ratio_height:
        if click_state == "Pressed":
            if not index == location.actual.max_index - 1:
                index += 1
            else:
                index = 0
                hasclicked = True
    elif 360 > mouse[0] > 640 and 575 < mouse[1] < 640:
        pass
    draw_bot_context()
    return index


def button_action(context, locations):
    # Menu between arrows
    global istalking
    if 500 * ratio_width < mouse[0] < 780 * ratio_width and 570 * ratio_height < mouse[1] < 640 * ratio_height:
        pygame.draw.rect(win, (160, 160, 160), (500 * ratio_width, 570 * ratio_height,
                                                280 * ratio_width, 70 * ratio_height))
        display_text(location.actual.return_context_name(), 600 * ratio_height, int(32 * ratio_height), (255, 255, 255))
        if click[0] == 1:
            if isinstance(context, location.Move):
                draw_top_context()
                return context.direction
            elif isinstance(context, location.Interact):
                draw_dialogue(context.message)
            elif isinstance(context, location.Character):
                istalking = True
                draw_shape_ui()
            else:
                print("UI Error:Button_action Class")

    return locations.name


########################################################################################################################
# Initialization of the UI , it's used when you move to a different place or need to redraw the entire interface
def initialize_ui():
    draw_bot_context()
    draw_top_context()
    if istalking is True:
        draw_shape_ui()
    draw_chat()
    draw_dialogue("None")
    return True
