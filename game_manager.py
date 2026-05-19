# Teddy Rodd
# Morbanaa Studios
# Galaga

import sys

# Colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY  = '\033[90m'
# Reset Color
RESET = '\033[0m'

class Game_Manager():
    def __init__(self,game_height,game_width):
        self.game_height = game_height
        self.game_width = game_width
        self.game_map = []

    def world_gen(self):
        for y in range (self.game_height):
            row =[]
            for x in range(self.game_width):
                if y == 0 or y == self.game_height -1 or x == 0 or x == self.game_width -1:
                    row.append("@")
                else:
                    row.append(" ")
            self.game_map.append(row)

    def update_objects(self):
        pass

    def render_world(self):
        for y in range(self.game_height):
            for x in range(self.game_width):
                print(f"{DARK_GRAY}{self.game_map[y][x]}{RESET}",end="")
            print()

    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()
