from settings import *
from time import sleep
import os

# Idea file system for libraries and docs and instant project integration so it makes people reuse their own code and do better docs/code
# new Class of simulation that executes and action/triggered/constant simulation, as in actions_performed, key_pressed, every x time/ticks.
# TODO FIX MOVEMENT

class Simulation:
    def __init__(self, map):
        self.sim_time_s = 1 
        self.is_running = True
        self.map: Map = map
        self.action_stack = []
        self.is_manual: bool = True
        self.step_counter: int = 0
        self.cursor_pos = Position2D()
    
    def tick(self):
        sleep(self.sim_time_s)

    def sim_logic(self):
        if self.is_manual == False:
            self.count_simulation_steps()
            print("\n[SIM] - STEPS ->", str(self.step_counter))
        if self.is_manual == False and self.step_counter >= SIMULATION_DEFAULT_RUNS:
            self.is_manual = True
            self.step_counter = 0

    def move_cursor(self, dir):
        self.cursor_pos.move(dir)


    def stop_simulation(self):
        self.is_running = False

    def count_simulation_steps(self):
        self.step_counter += 1 

    def set_cursor(self):
        print("[CURSOR] -> UPDATE.")
        for entity in self.map.entities:
            if entity.position.x == self.cursor_pos.x and entity.position.y == self.cursor_pos.y:
                print("[CURSOR] -> CURSOR SET.")
                entity.is_cursor_selected = True
            else:
                entity.is_cursor_selected = False

    def get_events(self):
        if not self.is_manual:
            return
        user_input: str = self.get_input().lower()
        os.system('cls||clear')
        print("[INPUT] - COMMAND:", user_input)
        if user_input == "exit":
            self.is_running = False

        elif user_input == "in":
            self.is_manual = not self.is_manual

        self.move_cursor(user_input)
        


    def render(self):
        os.system('cls||clear')
        print(str(self.map.get_string_char_map()))
        print("\n[CONFIG] - MANUAL? ", str(self.is_manual))
        print("[WASD] - MOVE CURSOR TO\n[R] - SET CURSOR AS RESOURCE AREA\n[H] - SET HOME AREA\n[IN] - SWITCH INPUT NEED\n[EXIT] TYPE EXIT TO CLOSE")
   
    def get_input(self) -> str:
        return input()

    def logic(self):
        for entity in self.map.entities:
            entity.update()
        self.set_cursor()


    def loop(self):
        while self.is_running:
            self.render()
            self.get_events()
            self.logic()
            self.sim_logic()
            self.tick()
        os.system('exit')

class Composite:
    def __init__(self, tile_character: str = "X") -> None:
        self.position = Position2D()
        self.character = tile_character
        self.is_cursor_selected = False
        self.stored_character = tile_character
        self.to_call_function = None

    def set_characted_to_cursor(self):
        if self.is_cursor_selected:
            self.stored_character = self.character
            self.character = "#"

    def set_cursor_to_character(self):
        if self.is_cursor_selected == False:
            self.character = self.stored_character

    ### TODO CURSOR HOVER DETECTION AND RESPONSE

    def __str__(self) -> str:
        return self.character

    def cursor_logic(self):
        self.set_cursor_to_character()
        self.set_characted_to_cursor()

    def update(self):
        self.cursor_logic()

    def move_to_dir(self, dir):
        self.position.move(dir)
        


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
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == "w":
            self.y -= 1
        elif direction == "s":
            self.y += 1
        elif direction == "a":
            self.x -= 1
        elif direction == "d":
            self.x += 1
        print(self.x, self.y)

    
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
        self.entities = []


    def add_user(self, user: User):
        self.users.append(user)

    def insert_on_map(self, composite):
        self.map[composite.position.x][composite.position.y] = composite
        self.entities.append(composite)

    def create_map(self, size_x = MAP_SIZE_X, size_y = MAP_SIZE_Y):
        self.size_x = size_x
        self.size_y = size_y
        self.map = []
        for x_tile in range(size_x):
            self.map.append([])
            for y_tile in range(size_y):
                composite = Composite()
                composite.position.set_position(x_tile, y_tile)
                self.entities.append(composite)
                self.map[x_tile].append([])
                self.map[x_tile][y_tile] = composite

    def get_string_char_map(self) -> str:
        map: str = ""
        for x in range(self.size_x):
            for y in range(self.size_y):
                if y % self.size_x == 0:
                   map += "\n" 
                map += str(self.map[x][y])

        return map



    def get_map(self):
        return self.map

def run():
    map = Map()
    map.create_map()
    user = User()
    map.insert_on_map(user)
    sim = Simulation(map)
    sim.loop()


if __name__ == '__main__':
    run()


    
