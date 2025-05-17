import os

def get_adjacent_cells(grid, i, j):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    rows, cols = len(grid), len(grid[0])
    return [
        (i + dx, j + dy)
        for dx, dy in directions
        if 0 <= i + dx < rows and 0 <= j + dy < cols
    ]

def read_grid(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Input file {filename} not found")
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            # Split by comma and strip whitespace
            row = [x.strip() for x in line.split(',')]
            # Convert '_' to '_' and numbers to int, raise error for invalid chars
            row = [x if x == '_' else int(x) if x.isdigit() else ValueError(f"Invalid character: {x}") for x in row]
            grid.append(row)
    if not grid or not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Invalid grid format")
    return grid

def write_grid(grid, filename):
    with open(filename, 'w') as f:
        for row in grid:
            # Convert to string, replace 'G' with 'T', 'S' with 'G'
            row_str = [str(x) if x != 'G' and x != 'S' else 'T' if x == 'G' else 'G' for x in row]
            f.write(', '.join(row_str) + '\n')

def is_valid_solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isinstance(grid[i][j], int):
                adjacent = get_adjacent_cells(grid, i, j)
                gems = sum(1 for ai, aj in adjacent if grid[ai][aj] == 'T')
                if gems != grid[i][j]:
                    return False
    return True