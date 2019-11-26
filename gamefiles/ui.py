import pygame
import time
from gamefiles import locations as location

# Resolution
Screen_Width, Screen_Height = 1000, 700
win = pygame.display.set_mode((Screen_Width, Screen_Height))

# Shape and size
Shape_Width, Shape_Height = 100, 100
Shape_X, Shape_Y = (Screen_Width / 2) - (Shape_Width / 2), (Screen_Height / 2) - (Shape_Height / 2)

# Player info
place = "None"

# Click handling
click = pygame.mouse.get_pressed()
mouse = pygame.mouse.get_pos()
click_state = "Released"

# Dialogues List

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

    def type_writer(font, text):
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
        type_writer(font, message)


def draw_chat():
    # Text Box UI
    pygame.draw.rect(win, [60, 60, 60], (20, 375, 240, 300), 0)
    pygame.draw.rect(win, [30, 30, 30], (20, 375, 240, 300), 3)


# Ui
def display_text(message, y_position):
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(message, True, (20, 60, 255))
    textrect = text.get_rect()
    textrect.center = (Screen_Width // 2, y_position)
    win.blit(text, textrect)


def draw_bot_context():
    # Context UI
    pygame.draw.polygon(win, (250, 250, 250), [(300, 600), (350, 650), (350, 550)])
    pygame.draw.polygon(win, (250, 250, 250), [(700, 600), (650, 650), (650, 550)])
    pygame.draw.rect(win, (180, 180, 180), (360, 575, 280, 55))
    display_text(location.actual.return_context_name(), 600)


def draw_top_context():
    # Top UI
    pygame.draw.rect(win, (180, 180, 180), (360, 25, 280, 50))
    display_text(place, 50)


def draw_shape_ui():
    # Shape UI
    pygame.draw.rect(win, [255, 0, 0], [Shape_X - Shape_Width / 2, Shape_Y - Shape_Height / 2, Shape_Width * 2,
                                        Shape_Height * 2], 1)


# Controls
def button_index(index):
    # Left arrow clickable
    if 300 < mouse[0] < 350 and 550 < mouse[1] < 650:
        pygame.draw.polygon(win, (100, 200, 200), [(300, 600), (350, 650), (350, 550)])
        if click_state == "Pressed":
            if not index == 0:
                index -= 1
            else:
                index = location.actual.max_index - 1
            hasclicked = True

    # Right arrow clickable
    elif 700 > mouse[0] > 650 > mouse[1] > 550:
        pygame.draw.polygon(win, (100, 200, 200), [(700, 600), (650, 650), (650, 550)])
        if click_state == "Pressed":
            if not index == location.actual.max_index - 1:
                index += 1
            else:
                index = 0
                hasclicked = True
    elif 360 > mouse[0] > 640 and 575 < mouse[1] < 640:
        pass
    elif click_state != "Released" or click_state != "Pressed":
        draw_bot_context()
    else:
        draw_bot_context()
    return index


def button_action(context, locations):
    # Menu between arrows
    if 360 < mouse[0] < 640 and 575 < mouse[1] < 630:
        pygame.draw.rect(win, (255, 255, 255), (360, 575, 280, 55))
        display_text(location.actual.return_context_name(), 600)

        if click[0] == 1:
            if isinstance(context, location.Move):
                draw_top_context()
                return context.direction
            if isinstance(context, location.Talk):
                draw_dialogue(context.message)
            else:
                print("Error:Button_action Class")

    return locations.name


def initialize_ui():
    draw_bot_context()
    draw_top_context()
    draw_shape_ui()
    draw_chat()
    draw_dialogue("None")
    return True
