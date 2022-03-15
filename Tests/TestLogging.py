# In SudokuBacktracker set self.__enable_logging = True
from SudokuSolver import SudokuSolver

sudoku_solver = SudokuSolver()

extreme_puzzle_two = {(0, 6): 5,
                      (1, 1): 3, (1, 2): 7, (1, 3): 4,
                      (2, 4): 2, (2, 5): 6, (2, 6): 4, (2, 7): 7,
                      (3, 0): 7, (3, 3): 8, (3, 4): 6, (3, 6): 9,
                      (4, 0): 4, (4, 8): 1,
                      (5, 2): 5, (5, 4): 1, (5, 5): 4, (5, 8): 8,
                      (6, 1): 7, (6, 2): 6, (6, 3): 5, (6, 4): 8,
                      (7, 5): 9, (7, 6): 6, (7, 7): 1,
                      (8, 2): 2}

return_value = sudoku_solver.solve_puzzle(extreme_puzzle_two, True)
print(return_value.message)