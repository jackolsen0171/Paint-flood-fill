from utils import *
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINT v2.1")
fill_mode = False
GREY = (51,51,51)

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
            pygame.draw.rect(win,colour, ((j * PIXEL_SIZE), (i * PIXEL_SIZE) + 140, PIXEL_SIZE, PIXEL_SIZE))
            

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0,(i * PIXEL_SIZE) + 140),
                             (WIDTH, (i * PIXEL_SIZE) + 140))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 140),
                             (i * PIXEL_SIZE, HEIGHT))


def getRowCol(pos):
    x,y = pos
    y = y - 140 #top 140 pixels are not part of the grid
    row = y//PIXEL_SIZE
    col = x//PIXEL_SIZE
    return row,col

def clickedOnButton(pos,button):
    x,y = pos
    if (x > button.x) and (x < button.x + button.width) and (y > button.y) and (y < button.y + button.height):
        return True

def floodFill(x,y, start_colour, new_colour):
    if grid[x][y] != start_colour:
        return None
    else:
        grid[x][y] = new_colour
        neighbours = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for n in neighbours:
            if 0 <= n[0] <= WIDTH-1 and 0 <= n[1] <= HEIGHT-1:
                floodFill(n[0], n[1], BG_COLOR, fill_colour)
    
    
    
    

def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    statusBar.show(WIN)
    for button in buttons:
        button.show(WIN)
    fillButton.show(WIN)
    pygame.display.update()


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
fillButton = Button(900,90,50,30,WHITE,'fill','', 30)
statusBar = Button(400,5,50,50,WHITE,'status:','',50)
buttons = [
    Button(900,0,50,30,WHITE, 'erase','',30),
    Button(900,45,50,30,WHITE, 'clear', '', 30),
    Button(10,10,50,50,BLACK,'Black'),
    Button(70,10,50,50,RED,'Red'),
    Button(10,70,50,50,GREEN,'Green'),
    Button(70,70,50,50,BLUE,'Blue'),

]


while run:
    clock.tick(FPS)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False


        if pygame.mouse.get_pressed()[0] and not fill_mode:
            row,col = getRowCol(pos)
            grid[row][col] = drawing_colour
            
            for index,button in enumerate(buttons):
                if clickedOnButton(pos,buttons[index]):
                    statusBar.text2 = buttons[index].text
                    drawing_colour = buttons[index].colour
                    fill_colour = buttons[index].colour
                    
                    if buttons[index].text == 'clear':
                        for i,colour in enumerate(grid):
                            for j,colour in enumerate(grid):
                                grid[i][j] = WHITE
            
            
            if clickedOnButton(pos, fillButton) and (fill_mode == False):
                    fill_mode = True
                    statusBar.text2 = 'fill' 
        
        if fill_mode == True:
            x,y = getRowCol(pos)
            if pygame.mouse.get_pressed()[0] and (x >= 0) and (y >= 0):
                floodFill(x,y,BG_COLOR, fill_colour)
                fill_mode = False
                statusBar.text2 = ''         

            
    draw(WIN, grid)




pygame.quit()

