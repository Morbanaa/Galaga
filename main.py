# Teddy Rodd
# Morbanaa Studios
# Galaga

import time
from game_manager import Game_Manager

def main():
    game_speed = .05
    game_manager = Game_Manager(35,50)
    game_manager.world_gen() # creates world one time

    while True:
        game_manager.render_world()

        # Util
        time.sleep(game_speed)
        game_manager.clear_move_cursor()

if __name__ == "__main__":
    main()


