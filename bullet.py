# Teddy Rodd
# Morbanaa Studios
# Galaga

class Bullet():
    bullets = []
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

    def update(self):
        self.ypos -=1
