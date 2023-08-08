from settings import *

class Composite:
    def __init__(self, tile_character: str = "X") -> None:
        self.position = Position2D()
        self.character = tile_character

class User(Composite):
    def __init__(self):
        Composite.__init__(self, "o")

    def get_character(self):
        return self.character 

    
class Position2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def get_position(self):
        return [self.x, self.y]


class Map:
    def __init__(self):
        self.size_x = MAP_SIZE_X
        self.size_y = MAP_SIZE_Y
        self.map = []
        self.users = []


    def add_user(self, user: User):
        self.users.append(user)

    def insert_on_map(self, composite):
        self.map[composite.position.x][composite.position.y] = composite.get_character()



    def create_map(self, size_x = MAP_SIZE_X, size_y = MAP_SIZE_Y):
        self.size_x = size_x
        self.size_y = size_y
        self.map = []
        for x_tile in range(size_x):
            self.map.append([])
            for y_tile in range(size_y):
                self.map[x_tile].append([])
                self.map[x_tile][y_tile] = "X"

    def get_string_char_map(self) -> str:
        map: str = ""
        for x in range(self.size_x):
            for y in range(self.size_y):
                if y % 10 == 0:
                   map += "\n" 
                map += str(self.map[x][y])

        return map



    def get_map(self):
        return self.map

def run():
    map = Map()
    map.create_map()
    print(map.get_string_char_map())
    user = User()
    map.insert_on_map(user)
    print(map.get_string_char_map())


if __name__ == '__main__':
    run()


    
