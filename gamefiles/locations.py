import pygame
import time
import gamefiles.ui as ui


# Class definition
class Move:
    def __init__(self, direction):
        self.direction = direction


class Character:
    def __init__(self, name, color, shape, dialogues):
        self.name = name
        self.red, self.green, self.blue = color
        self.shape = shape
        self.dialogues = dialogues

    def draw_soul(self):
        pygame.draw.polygon(ui.win, [self.red, self.green, self.blue], self.shape, 0)

    # Box where you will create the shapes
    # pygame.draw.rect(win, [255, 0, 0], [Shape_X - Shape_Width / 2, Shape_Y - Shape_Height / 2, Shape_Width * 2,
    #                                        Shape_Height * 2], 1)


class Interact:
    def __init__(self, name, message):
        self.name = name
        self.message = message


########################################################################################################################
# Move class
Move_Test = Move("Test")

# Characters Class
Character_Test = Character("Character_test", [255, 90, 60], [(450, 300), (550, 300),
                                                             (510, 325), (510, 400),
                                                             (490, 400), (490, 325),
                                                             ],
                           ["=) Hello , this is the first text box",
                            "Hello , this is the second text box",
                            "Hello , this is the third text box"]
                           )

# Interact class
Interact_Test = Interact("Interact_Test", "This is a test for written text ")


########################################################################################################################
# Class Location control the movement in the different places , each Location is like a room with it's own NPC
class Location:
    """This Class is used for handling the position where you are and what you can do
    and where you can
    Context_list is used to store every possible direction displayed
    location index is just to move between this list
    """

    def __init__(self, name, context_list):
        self.name = name
        self.context_list = context_list
        self.location_index = 1
        self.max_index = len(context_list)

    def return_context_name(self):
        current_selection = self.context_list[self.location_index]
        if isinstance(current_selection, Move):
            return current_selection.direction
        if isinstance(current_selection, Interact):
            return current_selection.name
        if isinstance(current_selection, Character):
            return current_selection.name

        else:
            return "None"

    def return_context(self):
        current_selection = self.context_list[self.location_index]
        return current_selection


########################################################################################################################
# actual is the location the player is actually in, and place is the name displayed of this location.
# every is a dictionnary with key for every location in the game

Beginning = Location("Test", [Move_Test, Character_Test, Interact_Test])
actual = Beginning
place = actual.name
every = {"Test": Beginning}


def control_check(actual):
    actual.location_index = ui.button_index(actual.location_index)
    a = ui.button_action(actual.return_context(), actual)
    ui.place = a
    actual = every[a]
