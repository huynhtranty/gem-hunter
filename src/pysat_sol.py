from pysat.solvers import Solver
from cnf_generate import setup_variable_maps, generate_cnf 


def solve_pysat(grid):
    var_map, reverse_map = setup_variable_maps(grid)
    cnf = generate_cnf(grid, var_map)
    solver = Solver(name='g3')
    solver.append_formula(cnf)
    if not solver.solve():
        solver.delete()
        return None

    model = solver.get_model()
    solver.delete()

    result = [row[:] for row in grid]
    for val in model:
        if val > 0 and reverse_map.get(val):
            i, j = reverse_map[val]
            if result[i][j] == '_':
                result[i][j] = 'G'  # Gem (will be 'T' in output)
        elif val < 0 and reverse_map.get(-val):
            i, j = reverse_map[-val]
            if result[i][j] == '_':
                result[i][j] = 'S'  # Safe (will be 'G' in output)
    return result