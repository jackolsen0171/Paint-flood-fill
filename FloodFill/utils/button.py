from .settings import *

class Button:
    def __init__(self,x,y,colour, width,height):
        self.x = x
        self.y = y
        self.colour = colour
        self.width = width
        self.height = height
    
    def show(self,win):
        pygame.draw.rect(
            win, self.colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(
            win, BLACK, (self.x, self.y, self.width, self.height), 2)

