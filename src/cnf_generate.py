import itertools
from pysat.formula import CNF
from utils import get_adjacent_cells

def setup_variable_maps(grid):
    var_map, reverse_map = {}, {}
    var_count = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            var_map[(i, j)] = var_count
            reverse_map[var_count] = (i, j)
            var_count += 1
    return var_map, reverse_map

def add_exact_k_constraint(cnf, variables, k):
    if k > 0:
        for comb in itertools.combinations(variables, len(variables) - k + 1):
            cnf.append(list(comb))
    if k < len(variables):
        for comb in itertools.combinations(variables, k + 1):
            cnf.append([-v for v in comb])

def generate_cnf(grid, var_map):
    cnf = CNF()
    seen_clauses = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isinstance(grid[i][j], int):
                adjacent = get_adjacent_cells(grid, i, j)
                unknowns = [c for c in adjacent if grid[c[0]][c[1]] == '_']

                if len(unknowns) < grid[i][j]:
                    raise ValueError(f"Invalid puzzle at ({i},{j}) - not enough unknowns")

                vars_for_unknowns = [var_map[xy] for xy in unknowns]
                clauses = []

                for comb in itertools.combinations(vars_for_unknowns, len(vars_for_unknowns) - grid[i][j] + 1):
                    clauses.append(list(comb))
                for comb in itertools.combinations(vars_for_unknowns, grid[i][j] + 1):
                    clauses.append([-v for v in comb])

                for clause in clauses:
                    key = tuple(sorted(clause))
                    if key not in seen_clauses:
                        cnf.append(clause)
                        seen_clauses.add(key)

    return cnf