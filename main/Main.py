import pygame
import gamefiles.locations as location
import gamefiles.ui as ui
import time

# Initialize
pygame.init()
pygame.display.set_caption("Artheus")
run = True
new_room = False


def mouse():
    ui.click = pygame.mouse.get_pressed()
    ui.mouse = pygame.mouse.get_pos()
    if ui.click[0] == 1 and ui.click_state == "Pressed":
        ui.click_state = "Hold"
        return
    if ui.click[0] == 1 and ui.click_state == "Released":
        ui.click_state = "Pressed"
        ui.draw_bot_context()
        return
    elif ui.click_state != "Released" and ui.click[0] == 0:
        ui.click_state = "Released"
        return


# Step Loop
while run:
    pygame.time.delay(60)
    mouse()
    if not new_room:
        new_room = ui.initialize_ui()
    location.control_check(location.actual)
    pygame.display.update()


# Application Code for leaving
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # win.fill((0, 0, 0))
pygame.display.quit()
pygame.quit()











