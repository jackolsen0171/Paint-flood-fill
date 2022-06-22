from .settings import *

class Button:
    def __init__(self,x,y,colour, width,height, text, checkboxText, checkboxColour):
        self.x = x
        self.y = y
        self.colour = colour
        self.width = width
        self.height = height
        self.text = text
        self.checkboxColour = checkboxColour
        self.checkboxText = checkboxText
        self.font = get_font(60)

    def show(self,win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))
        
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 3)
        
        txt = self.font.render(self.text, True, BLACK)
        win.blit(txt, (25,20))
        
    def showClicked(self,win):
        font = get_font(50)
        txt = font.render(self.checkboxText, True, self.checkboxColour)
        win.blit(txt, (115,25))