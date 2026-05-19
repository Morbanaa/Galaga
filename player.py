# Teddy Rodd
# Morbanaa Studios
# Galaga

from bullet import Bullet
import keyboard

class Player():
    def __init__(self,ypos,xpos,ammo):
        self.ypos = ypos
        self.xpos = xpos
        self.ammo = ammo
        self.timer = 7

    def update(self,game_map):
        if keyboard.is_pressed("W") and game_map[self.ypos -1][self.xpos] != "@":
            self.ypos -= 1

        if keyboard.is_pressed("S") and game_map[self.ypos +1][self.xpos] != "@":
            self.ypos += 1

        if keyboard.is_pressed("A") and game_map[self.ypos][self.xpos -1] != "@":
            self.xpos -= 1

        if keyboard.is_pressed("D") and game_map[self.ypos][self.xpos +1] != "@":
            self.xpos += 1

        self.timer += 1
        if keyboard.is_pressed("SPACE") and self.ammo > 0 and self.timer >7:
            self.timer = 0
            Bullet.bullets.append(Bullet(self.ypos -1,self.xpos))
            self.ammo -=1