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

import random
from player import Player
from enemy import Enemy
from bullet import Bullet

class Game_Manager():
    def __init__(self,game_height,game_width):
        self.game_height = game_height
        self.game_width = game_width
        self.game_map = []
        self.player = Player(self.game_height -3,self.game_width//2,100)

    def world_gen(self):
        for y in range (self.game_height):
            row =[]
            for x in range(self.game_width):
                if y == 0 or y == self.game_height -1 or x == 0 or x == self.game_width -1:
                    row.append("@")
                else:
                    row.append(" ")
            self.game_map.append(row)

    def spawn_enemy(self):
        Enemy.timer += 1

        if Enemy.timer > 45:
            Enemy.timer = 0
            Enemy.enemys.append(Enemy(0,random.randint(3,self.game_width -3)))

    def update_objects(self):
        self.player.update(self.game_map)
        for bullet in Bullet.bullets:
            bullet.update()

        # Enemys
        for enemy in Enemy.enemys:
            for bullet in Bullet.bullets:
                if bullet.ypos == enemy.ypos and abs(bullet.xpos - enemy.xpos) < 2:
                    Enemy.enemys.remove(enemy)
                    Bullet.bullets.remove(bullet)
                    break
            enemy.update(self.player,self.game_height,self.game_width)

    def render_world(self):
        print(f"Ammo: {self.player.ammo:<100}")
        for y in range(self.game_height):
            for x in range(self.game_width):

                # Render Bullets
                bullet_here = False
                for bullet in Bullet.bullets:
                    if bullet.ypos == y and bullet.xpos == x:
                        bullet_here = True
                        print(f"{"."}",end="")
                        break
                if bullet_here:
                    continue

                # Render Enemys
                enemy_here = False
                for enemy in Enemy.enemys:
                    if enemy.ypos == y and enemy.xpos == x:
                        enemy_here = True
                        print(f"{RED}{"V"}{RESET}",end="")
                        break
                if enemy_here:
                    continue

                # Render Player
                if y == self.player.ypos and x == self.player.xpos:
                    print(f"{GREEN}M{RESET}",end="")
                else:
                    print(f"{DARK_GRAY}{self.game_map[y][x]}{RESET}",end="")
            print()

    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()
