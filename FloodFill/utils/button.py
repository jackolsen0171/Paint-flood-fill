from webbrowser import get
from .settings import *

class Button:
    def __init__(self,x,y, width,height,colour, text=None,text2=None, font=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.text2 = text2
        self.font = font

    def show(self,win):
        pygame.draw.rect(win,self.colour, (self.x, self.y, self.width, self.height))
        
        # pygame.draw.rect(win, self.colour, (self.x + 60, self.y, self.width, self.height), 3)
        if self.font != None:
            font = get_font(self.font)
        
            txt = font.render(self.text,True, BLACK)
            if self.text2 != '':
                txt2 = font.render(self.text2,True, BLACK)
                win.blit(txt2,(self.x + 150, self.y))

            win.blit(txt, (self.x,self.y))

        
    # def onSwitch(self,win):#fill button only

    #     txt2 = self.font.render(self.text2, True, BLACK)

    #     win.blit(txt2, (self.x + 70 , self.y))
