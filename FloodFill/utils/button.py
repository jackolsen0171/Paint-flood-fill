from .settings import *

class Button:
    def __init__(self,x,y, width,height,colour, text=None,text2=None,text_colour=None,name=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.text2 = text2
        self.text_colour = text_colour

    def show(self,win):
        font = get_font(30)
        pygame.draw.rect(win, self.colour, (self.x + 10, self.y + 25, self.width, self.height))
        
        pygame.draw.rect(win, WHITE, (self.x + 10, self.y + 25, self.width, self.height), 3)
        
        txt = font.render(self.text,1, True, self.text_colour)
        if self.text2 != None:
            txt2 = font.render(self.text2,1, True, self.text_colour)
            win.blit(txt2, (self.x - 100, self.y))
        win.blit(txt, (self.x - 100,self.y))
        
    def showClicked(self,win):#fill button only
        font = get_font(30)
        txt = font.render(self.text ,1,True, self.text_colour)
        win.blit(txt, (self.x + 13,self.y + 28))
