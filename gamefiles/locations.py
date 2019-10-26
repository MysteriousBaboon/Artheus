context_list_outdoor = ["Entrance", "First house ", "Second House", "third house"]
context_list_indoor = ["Door", "chair ", "Table"]



class Location:
    def __init__(self, location):

        self.Location = location
        print(self.Location)


def convert_index_outdoor(index):
    return context_list_outdoor[index]

def get_list_len():
    return len(context_list_outdoor)
