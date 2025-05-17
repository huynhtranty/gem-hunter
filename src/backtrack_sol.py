from utils import get_adjacent_cells, is_valid_assignment

def backtrack(grid, unknowns, index):
    if index >= len(unknowns):
        return grid
    i, j = unknowns[index]
    # Try 'T' (gem)
    if is_valid_assignment(grid, i, j, 'T'):
        grid[i][j] = 'T'
        result = backtrack(grid, unknowns, index + 1)
        if result:
            return result
        grid[i][j] = '_'
    # Try 'G' (safe)
    if is_valid_assignment(grid, i, j, 'G'):
        grid[i][j] = 'G'
        result = backtrack(grid, unknowns, index + 1)
        if result:
            return result
        grid[i][j] = '_'
    return None

def solve_backtrack(grid):
    # Deep copy grid
    grid = [row[:] for row in grid]
    # Collect all unknown cells
    unknowns = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '_']
    return backtrack(grid, unknowns, 0)