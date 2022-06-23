from utils import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINT v2.1")
fill_mode = False

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
            pygame.draw.rect(win,colour, ((j * PIXEL_SIZE), (i * PIXEL_SIZE) + 100, PIXEL_SIZE, PIXEL_SIZE))
            

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0,(i * PIXEL_SIZE) + 100),
                             (WIDTH, (i * PIXEL_SIZE) + 100))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 100),
                             (i * PIXEL_SIZE, HEIGHT))

def getRowCol(pos):
    x,y = pos
    row = (y//PIXEL_SIZE) - (ROWS//10)
    col = x//PIXEL_SIZE
    return row,col

# def fillSquare(pos):
#     x,y = pos
#     row = (y//PIXEL_SIZE) - (ROWS//10)
#     col = x//PIXEL_SIZE
#     grid[row][col] = BLACK

def clickedOnFill(pos):
    x,y = pos
    if (x > fillButton.x) and (x < fillButton.x + fillButton.width) and (y > fillButton.y) and (y < fillButton.y + fillButton.height):
        return True
                
def floodFill(x,y, start_colour, new_colour):
    if grid[x][y] != start_colour:
        return None
    else:
        grid[x][y] = new_colour
        neighbours = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for n in neighbours:
            if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                floodFill(n[0], n[1], BG_COLOR, FILL_COLOUR)
    
    
    
    

def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    fillButton.show(win)
    fillButton.showClicked(WIN)
    pygame.display.update()


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
fillButton = Button(110,20,WHITE,60,45,'Fill: ', 'Off', BLACK)



while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]: 
            pos = pygame.mouse.get_pos()
            row,col = getRowCol(pos)
            if fill_mode == False:   
                grid[row][col] = drawing_color
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if clickedOnFill(pos) and fill_mode == False:
                fill_mode = True
                fillButton.checkboxColour = BLACK
                fillButton.checkboxText = 'On'
            
            elif clickedOnFill(pos) and fill_mode == True:
                fill_mode = False
                fillButton.checkboxColour = BLACK
                fillButton.checkboxText = 'Off'
        
        if fill_mode == True:
            width = len(grid)
            height = len(grid[0])
            pos = getRowCol(pos)
            floodFill(pos[0], pos[1], BG_COLOR, FILL_COLOUR)


            

    draw(WIN, grid)




pygame.quit()
