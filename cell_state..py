def count_neighbors(grid, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid):
                continue
            count += grid[i][j]
    return count
    
def next_generation(grid):
    n = len(grid)
    new_grid = [[0]*n for _ in range(n)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = count_neighbors(grid, i, j)
            if neighbors == 3:
                new_grid[i][j] = 1
            elif neighbors == 2:
                new_grid[i][j] = grid[i][j]
            else:
                new_grid[i][j] = 0
    return new_grid