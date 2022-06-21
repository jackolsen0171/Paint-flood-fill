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
    row = x//PIXEL_SIZE
    col = (y//PIXEL_SIZE) - (ROWS//10)
    grid[col][row] = BLACK

def checkFillPress(pos):
    x,y = pos
    if (x > fillButton.x) and (x < fillButton.x + fillButton.width) and (y > fillButton.y) and (y < fillButton.y + fillButton.height):
        print('hi')


def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    fillButton.show(win)
    pygame.display.update()



run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
fillButton = Button(110,20,WHITE,40,40,'Fill: ', True)



while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            fillSquare(pos)
            if checkFillPress(pos):
                pass

            

    draw(WIN, grid)




pygame.quit()