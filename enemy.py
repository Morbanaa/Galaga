# Teddy Rodd
# Morbanaa Studios
# Galaga

import random
from bullet import Bullet

class Enemy():
    enemys = []
    timer = 0
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

    def update(self,player,game_height,game_width):
        self.ypos +=1
        if abs(self.xpos -player.xpos) > random.randint(1,4):
            if self.xpos > player.xpos:
                self.xpos -=1
            else:
                self.xpos +=1
        
        if self.ypos > game_height + 20:
            self.ypos = 0
            self.xpos = random.randint(3,game_width -3)