import time
from utils import get_adjacent_cells, is_valid_assignment, is_partial_valid

def backtrack(grid, original_grid, empty_cells, idx):
    if idx == len(empty_cells):
        return is_valid_assignment(grid, original_grid)
    i, j = empty_cells[idx]
    for val in ['T', 'G']:
        grid[i][j] = val
        if is_partial_valid(grid, original_grid, i, j):
            if backtrack(grid, original_grid, empty_cells, idx + 1):
                return True
        grid[i][j] = '_'
    return False

def solve_backtracking(grid):
    start_time = time.time()
    result = [row[:] for row in grid]
    empty = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '_']
    success = backtrack(result, grid, empty, 0)
    print(f"Backtracking time: {time.time() - start_time:.6f} seconds" if success else "Backtracking failed.")
    return result if success else None
