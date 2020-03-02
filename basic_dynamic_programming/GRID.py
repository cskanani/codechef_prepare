for _ in range(int(input())):
    grid_size = int(input())
    grid = []
    for i in range(grid_size):
        grid.append(list(input()))
    
    for j in range(grid_size):
        mark_star = False
        for i in range(grid_size - 1, -1, -1):
            if grid[i][j] == '#':
                mark_star = True
            elif mark_star:
                grid[i][j] = '*'
    
    for i in range(grid_size):
        mark_star = False
        for j in range(grid_size - 1, -1, -1):
            if grid[i][j] == '#':
                mark_star = True
            elif mark_star:
                grid[i][j] = '*'
    
    possible_locations = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == '.':
                possible_locations += 1
    
    print(possible_locations)    
