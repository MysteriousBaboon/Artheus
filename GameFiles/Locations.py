context_list = ["Entrance", "First house ", "Second House", "third house"]


class Location:
    def __init__(self, location):

        self.Location = location
        print(self.Location)


def convert_index(index):
    return context_list[index]


def get_list_len():
    return len(context_list)
