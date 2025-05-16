import itertools
import time
from utils import is_valid_assignment

def solve_brute_force(grid):
    start_time = time.time()
    empty = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '_']
    for assignment in itertools.product(['T', 'G'], repeat=len(empty)):
        temp = [row[:] for row in grid]
        for idx, (i, j) in enumerate(empty):
            temp[i][j] = assignment[idx]
        if is_valid_assignment(temp, grid):
            print(f"Brute force time: {time.time() - start_time:.6f} seconds")
            return temp
    print(f"Brute force failed in {time.time() - start_time:.6f} seconds")
    return None
