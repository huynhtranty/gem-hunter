from itertools import product
from utils import get_adjacent_cells, is_valid_solution

def solve_brute_force(grid):
    from itertools import product
    grid = [row[:] for row in grid]  # shallow copy, OK if no nested lists
    unknowns = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '_']

    for assignment in product(['T', 'G'], repeat=len(unknowns)):
        for (i, j), val in zip(unknowns, assignment):
            grid[i][j] = val
        if is_valid_solution(grid):
            assert is_valid_solution(grid)
            return [row[:] for row in grid]  # clone again to avoid side effects
        # Reset for next iteration
        for i, j in unknowns:
            grid[i][j] = '_'

    return None
