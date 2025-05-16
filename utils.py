def get_adjacent_cells(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    adjacent = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                adjacent.append((i, j))
    return adjacent

def is_valid_assignment(grid, original_grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isinstance(original_grid[i][j], int):
                count = sum(1 for x, y in get_adjacent_cells(grid, i, j) if grid[x][y] == 'T')
                if count != original_grid[i][j]:
                    return False
    return True

def is_partial_valid(grid, original_grid, row, col):
    for i in range(max(0, row - 1), min(len(grid), row + 2)):
        for j in range(max(0, col - 1), min(len(grid[0]), col + 2)):
            if isinstance(original_grid[i][j], int):
                count_t = count_ = 0
                for x, y in get_adjacent_cells(grid, i, j):
                    if grid[x][y] == 'T':
                        count_t += 1
                    elif grid[x][y] == '_':
                        count_ += 1
                if count_t > original_grid[i][j] or count_t + count_ < original_grid[i][j]:
                    return False
    return True
