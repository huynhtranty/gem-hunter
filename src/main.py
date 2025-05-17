import os
import time
import sys
from pysat_sol import solve_pysat
from backtrack_sol import solve_backtrack
from brute_force_sol import solve_brute_force
from utils import read_grid, write_grid

def main():
    # Get the testcases directory (one level up from src)
    src_dir = os.path.dirname(os.path.abspath(__file__))
    testcases_dir = os.path.join(src_dir, '..', 'testcases')
    
    # Ensure testcases directory exists
    if not os.path.exists(testcases_dir):
        print(f"Error: Testcases directory {testcases_dir} does not exist")
        sys.exit(1)

    # Process all input files in testcases directory
    for filename in os.listdir(testcases_dir):
        if filename.startswith('input_') and filename.endswith('.txt'):
            # Extract input number
            input_num = filename.split('_')[1].split('.')[0]
            input_path = os.path.join(testcases_dir, filename)
            output_path = os.path.join(testcases_dir, f'output_{input_num}.txt')

            print(f"\nProcessing {filename}...")

            # Read grid
            try:
                grid = read_grid(input_path)
            except Exception as e:
                print(f"Error reading {input_path}: {e}")
                continue

            # Run and time PySAT solver
            start_time = time.time()
            pysat_result = solve_pysat(grid)
            pysat_time = time.time() - start_time

            # Run and time Backtracking solver
            start_time = time.time()
            backtrack_result = solve_backtrack(grid)
            backtrack_time = time.time() - start_time

            # Run and time Brute Force solver
            start_time = time.time()
            brute_force_result = solve_brute_force(grid)
            brute_force_time = time.time() - start_time

            # Print timing results
            print(f"PySAT Time: {pysat_time:.6f} seconds")
            print(f"Backtracking Time: {backtrack_time:.6f} seconds")
            print(f"Brute Force Time: {brute_force_time:.6f} seconds")

            # Use PySAT result for output (assumed most reliable)
            if pysat_result:
                try:
                    write_grid(pysat_result, output_path)
                    print(f"Solution written to output_{input_num}.txt")
                except Exception as e:
                    print(f"Error writing {output_path}: {e}")
            else:
                print(f"No solution found for {filename}")

if __name__ == '__main__':
    main()