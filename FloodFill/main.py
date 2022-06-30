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
    row = (y//PIXEL_SIZE) - (ROWS//10)
    col = x//PIXEL_SIZE
    return row,col

# def fillSquare(pos):
#     x,y = pos
#     row = (y//PIXEL_SIZE) - (ROWS//10)
#     col = x//PIXEL_SIZE
#     grid[row][col] = BLACK

# def clickedOnButton(pos):
#     x,y = pos
#     if (x > fillButton.x) and (x < fillButton.x + fillButton.width) and (y > fillButton.y) and (y < fillButton.y + fillButton.height):
#         return True
                
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
    statusBar.show(WIN)
    # if fill_mode == True:  
    #     fillButton.onSwitch(WIN)
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
    Button(10,10,50,50,BLACK),
    Button(70,10,50,50,RED),
    Button(10,70,50,50,GREEN),
    Button(70,70,50,50,BLUE),

]


while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False


        if pygame.mouse.get_pressed()[0]: 
            for index,button in enumerate(buttons):
                pass
                


            
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # if clickedOnFill(pos) and fill_mode == False:
        #     if clickedOnFill(pos):
        #         fill_mode = True

        #         fillButton.text_colour = BLACK
        #         statusBar.text2 = 'Fill'
            
        #     elif clickedOnFill(pos) and fill_mode == True:
        #         fill_mode = False
        #         fillButton.text_colour = BLACK
        #         statusBar.text2 = ''

        #     for index,button in enumerate(buttons):
        #         if clickedOnFill(pos):
        #             print(index)
        # for index, button in buttons:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if clickedOnButton(pos):
        
        # if fill_mode == True:
        #     width = len(grid)
        #     height = len(grid[0])
        #     pos = getRowCol(pos)
        #     floodFill(pos[0], pos[1], BG_COLOR, FILL_COLOUR)


            
    draw(WIN, grid)




pygame.quit()
