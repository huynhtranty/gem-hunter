from itertools import product
from utils import get_adjacent_cells

def is_valid_solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isinstance(grid[i][j], int):
                adjacent = get_adjacent_cells(grid, i, j)
                gems = sum(1 for ai, aj in adjacent if grid[ai][aj] == 'T')
                if gems != grid[i][j]:
                    return False
    return True

def solve_brute_force(grid):
    grid = [row[:] for row in grid]
    unknowns = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '_']
    for assignment in product(['T', 'G'], repeat=len(unknowns)):
        # Apply assignment
        for (i, j), value in zip(unknowns, assignment):
            grid[i][j] = value
        if is_valid_solution(grid):
            return grid
        # Reset for next iteration
        for i, j in unknowns:
            grid[i][j] = '_'
    return None