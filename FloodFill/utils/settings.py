import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

FPS = 240

WIDTH, HEIGHT = 1000, 600

ROWS =  COLS = 20 #cols is row / 2 

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

OFFSET = 140

drawing_colour = BLACK

fill_colour = RED

fill_mode = False

def getTextSize(size,text):
    font = pygame.font.SysFont("comicsans", size)
    textSize = font.size(text)
    return textSize    

def get_font(size):
    return pygame.font.SysFont("comicsans", size)