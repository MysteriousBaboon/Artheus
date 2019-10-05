import pygame
import time
from GameFiles import Locations

pygame.init()
pygame.display.set_caption(("Artheus"))

# Initialize

# Resolution
Screen_Width = 1000
Screen_Height = 700
win = pygame.display.set_mode((Screen_Width, Screen_Height))

Shape_Width = 100
Shape_Height = 100
# Shape and size
Shape_X = (Screen_Width / 2) - (Shape_Width / 2)
Shape_Y = (Screen_Height / 2) - (Shape_Height / 2)
Shape = "Rectangle"
# Colors
Red = 55
Green = 100
Blue = 200
# State of the Player
Outdoor = True
Fame = 0
context = "nothing"
context_index = 0
context_max_index = Locations.get_list_len()


def Display_Text(message):
    # Text
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(message, True, (255, 255, 255))
    textrect = text.get_rect()
    textrect.center = (Screen_Width // 2, 600)
    win.blit(text, textrect)

def draw_rectangle():
    pygame.draw.rect(win, (Red, Green, Blue), (Shape_X, Shape_Y, Shape_Width, Shape_Height))


def button(context_index):
    index = context_index
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global hasclicked

    if(click[0] == 0):
        hasclicked = False;
    # Left arrow clickable
    if 200 < mouse[0] < 250 and 550 < mouse[1] < 700:
        pygame.draw.polygon(win, (200, 200, 200), [(200, 600), (250, 650), (250, 550)])
        if click[0] == 1 and not hasclicked:
            if not index == 0 :
                index -= 1
            else:
                index = context_max_index - 1
            hasclicked = True

    # Right arrow clickable
    elif 750 < mouse[0] < 800 and 550 < mouse[1] < 700:
        pygame.draw.polygon(win, (200, 200, 200), [(800, 600), (750, 650), (750, 550)])
        if click[0] == 1 and not hasclicked:
            if not index == context_max_index - 1:
                index += 1
            else:
                index = 0
            hasclicked = True

    return index

# While loop


while True:
    if not Outdoor:
        pygame.time.delay(100)
        draw_rectangle()
        button()
        pygame.display.update()


    if Outdoor:
        pygame.time.delay(100)
        draw_rectangle()
        pygame.draw.polygon(win, (250, 250, 250), [(200, 600), (250, 650), (250, 550)])
        pygame.draw.polygon(win, (250, 250, 250), [(800, 600), (750, 650), (750, 550)])
        context_index = button(context_index)
        print(context_index)
        context = Locations.convert_index(context_index)
        Display_Text(context)
        pygame.display.update()





# Common code



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
pygame.quit()






    # keys = pygame.key.get_pressed()




