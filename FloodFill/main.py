from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINT v2.1")


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, colour in enumerate(row):
            pygame.draw.rect(win,colour, ((j * PIXEL_SIZE), (i * 
            PIXEL_SIZE) + 100, PIXEL_SIZE, PIXEL_SIZE))
            

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0,(i * PIXEL_SIZE) + 100),
                             (WIDTH, (i * PIXEL_SIZE) + 100))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 100),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def fillSquare(pos):
    x,y = pos
    row,col = x//20, y//20 - 5
    grid[col][row] = BLACK

def draw(win, grid,button):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    fillButton.show(win)
    pygame.display.update()




run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
fillButton = Button(20,20,WHITE,40,40)



while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            fillSquare(pos)

            

    draw(WIN, grid, fillButton)
print(grid[0][0])
pygame.quit()