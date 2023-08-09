from settings import *
from time import sleep
import os
# Idea file system for libraries and docs and instant project integration so it makes people reuse their own code and do better docs/code

# new Class of simulation that executes and action/triggered/constant simulation, as in actions_performed, key_pressed, every x time/ticks.

class Simulation:
    def __init__(self, map):
        self.sim_time_s = 1 
        self.is_running = True
        self.map: Map = map
        self.action_stack = []
        self.is_manual: bool = True
    
    def tick(self):
        sleep(self.sim_time_s)

    def stop_simulation(self):
        self.is_running = False

    def get_events(self):
        if not self.is_manual:
            return
        user_input: str = self.get_input().lower()
        print("[INPUT] - Was:", user_input)
        if user_input == "exit":
            self.is_running = False

        if user_input == "in":
            self.is_manual = not self.is_manual

    def render(self):
        os.system('cls||clear')
        print(str(self.map.get_string_char_map()))
        print("[CONFIG] - MANUAL? ", str(self.is_manual))
        print("[WASD] - MOVE CURSOR TO\n[R] - SET CURSOR AS RESOURCE AREA\n[H] - SET HOME AREA\n[IN] - SWITCH INPUT NEED\n[EXIT] TYPE EXIT TO CLOSE")
   
    def get_input(self) -> str:
        return input()

    def logic(self):
        pass

    def loop(self):
        while self.is_running:
            self.render()
            self.get_events()
            self.logic()
            self.tick()
        os.system('exit')




class Composite:
    def __init__(self, tile_character: str = "X") -> None:
        self.position = Position2D()
        self.character = tile_character

class User(Composite):
    def __init__(self):
        Composite.__init__(self, "o")
        self.position.x = 5
        self.position.y = 5

    def get_character(self):
        return self.character
    
    def __str__(self) -> str:
        return self.character 

    
class Position2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def get_position(self):
        return [self.x, self.y]

    def set_position(self, x: int, y: int):
        self.x, self.y = x, y


class Map:
    def __init__(self):
        self.size_x = MAP_SIZE_X
        self.size_y = MAP_SIZE_Y
        self.map = []
        self.users = []


    def add_user(self, user: User):
        self.users.append(user)

    def insert_on_map(self, composite):
        self.map[composite.position.x][composite.position.y] = composite

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
    sim = Simulation(map)
    sim.loop()


if __name__ == '__main__':
    run()


    
