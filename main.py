import os
import time
from backtracking import solve_backtracking
from brute_force import solve_brute_force
from pysat_lib import setup_variable_maps, generate_cnf_constraints, solve_with_pysat

def read_input(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for cell in line.strip().split(','):
                cell = cell.strip()
                if cell.isdigit():
                    row.append(int(cell))
                elif cell == '_':
                    row.append('_')
                else:
                    row.append(cell)
            row and grid.append(row)
    return grid

def write_output(grid, output_file):
    with open(output_file, 'w') as file:
        for i, row in enumerate(grid):
            file.write(', '.join(str(cell) for cell in row))
            if i < len(grid) - 1:
                file.write('\n')

def solve_file(input_file, output_file, method='pysat'):
    grid = read_input(input_file)
    result = None
    if method == 'pysat':
        variable_map, reverse_map = setup_variable_maps(grid)
        cnf = generate_cnf_constraints(grid, variable_map)
        start_time = time.time()
        result = solve_with_pysat(grid, cnf, reverse_map)
        print(f"PySAT time: {time.time() - start_time:.6f} seconds")
    elif method == 'brute_force':
        result = solve_brute_force(grid)
    elif method == 'backtracking':
        result = solve_backtracking(grid)
    elif method == 'all':
        print("Trying PySAT...")
        variable_map, reverse_map = setup_variable_maps(grid)
        cnf = generate_cnf_constraints(grid, variable_map)
        result = solve_with_pysat(grid, cnf, reverse_map)
        print("Trying brute force...")
        solve_brute_force(grid)
        print("Trying backtracking...")
        solve_backtracking(grid)
    else:
        raise ValueError("Invalid method")

    if result:
        write_output(result, output_file)
        return True
    return False

def main():
    input_files = [f for f in os.listdir('testcases') if f.startswith('input') and f.endswith('.txt')]
    input_files = [os.path.join('testcases', f) for f in input_files]
    if not input_files:
        print("No input files found.")
        return
    for input_file in input_files:
        output_file = input_file.replace('input', 'output')
        print(f"Solving {input_file}...")
        solve_file(input_file, output_file, method='pysat')

if __name__ == '__main__':
    main()
