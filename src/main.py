import os
import time
import sys
import concurrent.futures
from pysat_sol import solve_pysat
from backtrack_sol import solve_backtrack
from brute_force_sol import solve_brute_force
from utils import read_grid, write_grid

class TimeoutException(Exception):
    pass

def main():
    # Get the testcases directory (one level up from src)
    src_dir = os.path.dirname(os.path.abspath(__file__))
    testcases_dir = os.path.join(src_dir, '..', 'testcases')
    
    # Ensure testcases directory exists
    if not os.path.exists(testcases_dir):
        print(f"Error: Testcases directory {testcases_dir} does not exist")
        sys.exit(1)

    # Menu for algorithm selection
    print("Choose the algorithm to solve the CNF:")
    print("1. PySAT Solver")
    print("2. Backtracking Solver")
    print("3. Brute Force Solver")
    algo_choice = input("Enter your choice (1/2/3): ").strip()

    if algo_choice == '1':
        solver_func = solve_pysat
        solver_name = "PySAT"
    elif algo_choice == '2':
        solver_func = solve_backtrack
        solver_name = "Backtracking"
    elif algo_choice == '3':
        solver_func = solve_brute_force
        solver_name = "Brute Force"
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    # Menu for input selection
    print("\nChoose the input to solve:")
    print("1. input_1.txt")
    print("2. input_2.txt")
    print("3. input_3.txt")
    print("4. input_4.txt")
    print("A. Solve all inputs")
    input_choice = input("Enter your choice (1/2/3/4/A): ").strip().upper()

    # Build list of files to process
    input_files = []
    if input_choice in {'1', '2', '3', '4'}:
        input_files = [f"input_{input_choice}.txt"]
    elif input_choice == 'A':
        input_files = [f"input_{i}.txt" for i in range(1, 5)]
    else:
        print("Invalid input choice. Exiting.")
        sys.exit(1)

    # Process selected input files
    for filename in input_files:
        input_num = filename.split('_')[1].split('.')[0]
        input_path = os.path.join(testcases_dir, filename)
        output_path = os.path.join(testcases_dir, f'output_{input_num}.txt')

        print(f"\nProcessing {filename}...")

        # Read grid
        try:
            grid = read_grid(input_path)
            unknown_count = sum(row.count('_') for row in grid)
            print(f"Input size: {len(grid)} rows x {len(grid[0])} columns ({len(grid) * len(grid[0])} tiles), unknown: {unknown_count}")
        except Exception as e:
            print(f"Error reading {input_path}: {e}")
            continue

        # Run and time selected solver
        start_time = time.time()
        result = None
        if algo_choice == '3':
            # Set timeout for brute force (10 minutes = 600 seconds)
            with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
                future = executor.submit(solver_func, grid)
                try:
                    result = future.result(timeout=600)
                except concurrent.futures.TimeoutError:
                    print("Brute Force Solver timed out after 10 minutes.")
                    future.cancel()
        else:
            result = solver_func(grid)
        elapsed_time = time.time() - start_time

        # Print timing results
        print(f"{solver_name} Time: {elapsed_time * 1000:.6f} ms")

        # Use result for output
        if result:
            try:
                write_grid(result, output_path)
                print(f"Solution written to output_{input_num}.txt")
            except Exception as e:
                print(f"Error writing {output_path}: {e}")
        else:
            print(f"No solution found for {filename}")

if __name__ == '__main__':
    main()