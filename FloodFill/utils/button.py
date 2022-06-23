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
        pygame.draw.rect(win, self.colour, (self.x + 10, self.y + 25, self.width, self.height))
        
        pygame.draw.rect(win, WHITE, (self.x + 10, self.y + 25, self.width, self.height), 3)
        
        txt = self.font.render(self.text, True, BLACK)
        win.blit(txt, (self.x - 100,self.y))
        
    def showClicked(self,win):
        font = get_font(30)
        txt = font.render(self.checkboxText, True, self.checkboxColour)
        win.blit(txt, (self.x + 13,self.y + 28))
