rows = cols = 5

grid = []
for i in range(rows):
    grid.append([])
    for _ in range(cols):
        grid[i].append('0')


for i, row in enumerate(grid):
    for j, val in enumerate(grid):
        print(j,val)