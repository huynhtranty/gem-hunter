from pysat.formula import CNF
from pysat.solvers import Solver
import itertools
from utils import get_adjacent_cells

def setup_variable_maps(grid):
    variable_map = {}
    reverse_map = {}
    var_count = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            variable_map[(i, j)] = var_count
            reverse_map[var_count] = (i, j)
            var_count += 1
    return variable_map, reverse_map

def add_exact_n_constraint(cnf, variable_map, cells, n):
    variables = [variable_map[cell] for cell in cells]
    if n > 0:
        for comb in itertools.combinations(variables, len(variables) - n + 1):
            cnf.append([v for v in comb])
    if n < len(cells):
        for comb in itertools.combinations(variables, n + 1):
            cnf.append([-v for v in comb])

def generate_cnf_constraints(grid, variable_map):
    cnf = CNF()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isinstance(grid[i][j], int):
                adjacent = get_adjacent_cells(grid, i, j)
                add_exact_n_constraint(cnf, variable_map, adjacent, grid[i][j])
    return cnf

def solve_with_pysat(grid, cnf, reverse_map):
    solver = Solver(name='g3')
    solver.append_formula(cnf)
    if solver.solve():
        model = solver.get_model()
        result_grid = [row[:] for row in grid]
        for var in model:
            if var > 0 and var in reverse_map:
                i, j = reverse_map[var]
                if grid[i][j] == '_':
                    result_grid[i][j] = 'T'
            elif var < 0 and -var in reverse_map:
                i, j = reverse_map[-var]
                if grid[i][j] == '_':
                    result_grid[i][j] = 'G'
        solver.delete()
        return result_grid
    solver.delete()
    return None
