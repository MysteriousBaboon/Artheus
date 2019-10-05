import pygame
pygame.init()


pygame.display.set_caption(("Artheus"))
#Resolution
Screen_Width = 1000
Screen_Height = 700
win = pygame.display.set_mode((Screen_Width, Screen_Height))

Shape_Width = 100
Shape_Height = 100
#Shape and size
Shape_X = (Screen_Width / 2) - (Shape_Width / 2)
Shape_Y = (Screen_Height / 2) - (Shape_Height / 2)
Shape = "Rectangle"
#Colors
Red = 55
Green = 100
Blue = 200


def draw_rectangle():
    pygame.draw.rect(win, (Red, Green, Blue), (Shape_X, Shape_Y,Shape_Width, Shape_Height))


run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if Shape == "Rectangle":
        draw_rectangle()
    pygame.display.update()
    win.fill((0, 0, 0))

pygame.quit()
    # keys = pygame.key.get_pressed()
   # if keys[pygame.K_LEFT]:
   #     x -= vel
   # if keys[pygame.K_RIGHT]:
   #     x += vel
   # if keys[pygame.K_UP]:
   #     y -= vel
   # if keys[pygame.K_DOWN]:
   #     y += vel




