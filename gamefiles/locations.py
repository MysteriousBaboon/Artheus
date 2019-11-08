# Class definition
class Move:
    def __init__(self, direction):
        self.direction = direction


# Move class
house1 = Move("house1")
mayor = Move("mayor")

chair = Move("chair")
desk = Move("desk")


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
        else:
            return "None"

    def return_context(self):
        current_selection = self.context_list[self.location_index]
        return current_selection


Beginning = Location("Village", [house1, mayor])
Outside = Location("Outside", [chair, desk])

actual = Beginning
every = {"Village": Beginning, "Outside": Outside}




