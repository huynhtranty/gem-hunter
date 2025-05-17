from utils import get_adjacent_cells

def is_valid_assignment(grid, i, j, value):
    # Check if assigning value ('T' or 'G') at (i, j) is valid
    if grid[i][j] != '_':
        return False
    # Temporarily assign value
    grid[i][j] = value
    # Check all numbered cells
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if isinstance(grid[x][y], int):
                adjacent = get_adjacent_cells(grid, x, y)
                gems = sum(1 for ai, aj in adjacent if grid[ai][aj] == 'T')
                unknowns = sum(1 for ai, aj in adjacent if grid[ai][aj] == '_')
                required = grid[x][y]
                # Check if current gems exceed required or if remaining unknowns can't meet required
                if gems > required or (gems + unknowns < required):
                    grid[i][j] = '_'
                    return False
    grid[i][j] = '_'
    return True

def backtrack(grid, unknowns, index, gem_counts):
    if index >= len(unknowns):
        # Verify all constraints are met exactly
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if isinstance(grid[i][j], int):
                    adjacent = get_adjacent_cells(grid, i, j)
                    gems = sum(1 for ai, aj in adjacent if grid[ai][aj] == 'T')
                    if gems != grid[i][j]:
                        return None
        return grid
    i, j = unknowns[index]
    # Try 'T' (gem)
    if is_valid_assignment(grid, i, j, 'T'):
        grid[i][j] = 'T'
        result = backtrack(grid, unknowns, index + 1, gem_counts)
        if result:
            return result
        grid[i][j] = '_'
    # Try 'G' (safe)
    if is_valid_assignment(grid, i, j, 'G'):
        grid[i][j] = 'G'
        result = backtrack(grid, unknowns, index + 1, gem_counts)
        if result:
            return result
        grid[i][j] = '_'
    return None

def solve_backtrack(grid):
    # Deep copy grid to avoid modifying original
    grid = [row[:] for row in grid]
    # Collect all unknown cells
    unknowns = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '_']
    # Track gem counts for each numbered cell (not strictly necessary but kept for extensibility)
    gem_counts = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isinstance(grid[i][j], int):
                gem_counts[(i, j)] = grid[i][j]
    return backtrack(grid, unknowns, 0, gem_counts)