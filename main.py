# Teddy Rodd
# Morbanaa Studios
# Galaga

from game_manager import Game_Manager

def main():
    game_manager = Game_Manager(25,80)
    game_manager.world_gen() # creates world one time

    while True:
        game_manager.render_world()
        game_manager.clear_move_cursor()

if __name__ == "__main__":
    main()


