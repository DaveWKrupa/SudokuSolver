from SudokuSolver import SudokuSolver, SolutionType

sudoku_solver = SudokuSolver()

# Easy puzzle that can be solved by process of elimination
# is_extreme_sudoku = False
solution = [4, 5, 6, 7, 9, 8, 1, 3, 2,
            7, 3, 1, 5, 2, 4, 8, 6, 9,
            9, 8, 2, 1, 6, 3, 5, 4, 7,
            8, 1, 7, 6, 4, 2, 3, 9, 5,
            5, 4, 3, 9, 7, 1, 6, 2, 8,
            2, 6, 9, 3, 8, 5, 4, 7, 1,
            3, 2, 4, 8, 5, 9, 7, 1, 6,
            6, 9, 8, 4, 1, 7, 2, 5, 3,
            1, 7, 5, 2, 3, 6, 9, 8, 4]

easy_puzzle_one = {(0, 1): 5, (0, 3): 7, (0, 5): 8, (0, 7): 3,
                   (1, 0): 7, (1, 2): 1, (1, 4): 2, (1, 8): 9,
                   (2, 0): 9, (2, 5): 3, (2, 7): 4, (2, 8): 7,
                   (3, 2): 7, (3, 3): 6, (3, 5): 2, (3, 6): 3, (3, 8): 5,
                   (4, 4): 7,
                   (5, 0): 2, (5, 2): 9, (5, 3): 3, (5, 5): 5, (5, 6): 4,
                   (6, 0): 3, (6, 1): 2, (6, 3): 8, (6, 8): 6,
                   (7, 0): 6, (7, 4): 1, (7, 6): 2, (7, 8): 3,
                   (8, 1): 7, (8, 3): 2, (8, 5): 6, (8, 7): 8}

return_value = sudoku_solver.solve_puzzle(easy_puzzle_one, False, SolutionType.PROCESS_OF_ELIMINATION)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])

assert solution == result, "easy_puzzle_one has failed using SolutionType.process_of_elimination"

# Now test same puzzle using backtracker
return_value = sudoku_solver.solve_puzzle(easy_puzzle_one, False, SolutionType.BACKTRACKING)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])

assert solution == result, "easy_puzzle_one has failed using SolutionType.backtracking"

# hard puzzle not extreme
# test using backtracker
solution = [1, 7, 5, 8, 3, 2, 4, 9, 6,
            3, 6, 9, 7, 4, 5, 2, 1, 8,
            2, 4, 8, 1, 9, 6, 7, 5, 3,
            4, 5, 1, 3, 7, 8, 9, 6, 2,
            7, 3, 6, 4, 2, 9, 1, 8, 5,
            9, 8, 2, 5, 6, 1, 3, 7, 4,
            6, 2, 7, 9, 8, 4, 5, 3, 1,
            8, 1, 3, 2, 5, 7, 6, 4, 9,
            5, 9, 4, 6, 1, 3, 8, 2, 7]

hard_puzzle = {(0, 0): 1, (0, 3): 8, (0, 4): 3, (0, 5): 2,
               (1, 3): 7, (1, 4): 4, (1, 8): 8,
               (2, 0): 2, (2, 1): 4, (2, 6): 7,
               (3, 1): 5, (3, 5): 8, (3, 6): 9,
               (4, 5): 9, (4, 6): 1, (4, 8): 5,
               (5, 0): 9, (5, 2): 2, (5, 3): 5, (5, 4): 6,
               (6, 0): 6, (6, 8): 1,
               (7, 0): 8, (7, 2): 3, (7, 6): 6,
               (8, 1): 9, (8, 2): 4, (8, 7): 2}

return_value = sudoku_solver.solve_puzzle(hard_puzzle, False)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])

assert solution == result, "hard_puzzle has failed"

# Easy puzzle with diagonals can be solve by process of elimination
# is_extreme_sudoku = True

solution = [5, 6, 9, 7, 1, 3, 8, 4, 2,
            1, 2, 4, 8, 6, 5, 7, 9, 3,
            8, 3, 7, 4, 2, 9, 5, 1, 6,
            6, 8, 2, 9, 3, 7, 1, 5, 4,
            9, 4, 5, 1, 8, 2, 3, 6, 7,
            3, 7, 1, 6, 5, 4, 9, 2, 8,
            7, 9, 3, 2, 4, 1, 6, 8, 5,
            2, 1, 6, 5, 7, 8, 4, 3, 9,
            4, 5, 8, 3, 9, 6, 2, 7, 1]

extreme_puzzle_one = {(0, 2): 9, (0, 3): 7, (0, 5): 3, (0, 8): 2,
                      (1, 0): 1, (1, 3): 8, (1, 6): 7,
                      (2, 1): 3, (2, 2): 7, (2, 3): 4, (2, 8): 6,
                      (3, 1): 8, (3, 2): 2, (3, 4): 3, (3, 5): 7, (3, 8): 4,
                      (4, 1): 4, (4, 7): 6,
                      (5, 0): 3, (5, 3): 6, (5, 4): 5, (5, 6): 9, (5, 7): 2,
                      (6, 0): 7, (6, 5): 1, (6, 6): 6, (6, 7): 8,
                      (7, 2): 6, (7, 5): 8, (7, 8): 9,
                      (8, 0): 4, (8, 3): 3, (8, 5): 6, (8, 6): 2}

return_value = sudoku_solver.solve_puzzle(extreme_puzzle_one, True, SolutionType.PROCESS_OF_ELIMINATION)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])

assert solution == result, "extreme_puzzle_one has failed using SolutionType.process_of_elimination"

# run same puzzle using backtracker
return_value = sudoku_solver.solve_puzzle(extreme_puzzle_one, True, SolutionType.PROCESS_OF_ELIMINATION)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])

assert solution == result, "extreme_puzzle_one has failed using SolutionType.process_of_elimination"

# This puzzle cannot be solved completely using process of elimination
# is_extreme_sudoku = True

solution = [6, [1, 2, 4, 8], [1, 4, 8], [3, 7, 9], [3, 7, 9], [3, 7, 8], 5, [2, 8, 9], [2, 9],
            [1, 2, 5, 8], 3, 7, 4, [5, 9], [5, 8], [1, 8], [2, 8, 9], [2, 6, 9],
            [5, 8], [5, 8], 9, 1, 2, 6, 4, 7, 3,
            7, [1, 2], [1, 3], 8, 6, [2, 3, 5], 9, [2, 3, 4, 5], [2, 4, 5],
            4, [2, 6, 8, 9], [3, 8], [2, 3, 7, 9], [5, 7], [2, 3, 5, 7], [3, 7], [2, 3, 5, 6], 1,
            [2, 3, 9], [2, 6, 9], 5, [2, 3, 7, 9], 1, 4, [3, 7], [2, 3, 6], 8,
            [1, 3, 9], 7, 6, 5, 8, [1, 3], 2, [3, 4, 9], [4, 9],
            [3, 5, 8], [5, 8], [3, 4, 8], [2, 3, 7], [3, 4, 7], 9, 6, 1, [4, 5, 7],
            [1, 3, 5, 8, 9], [1, 4, 5, 8, 9], 2, [3, 6, 7], [3, 4, 7], [1, 3, 7], [3, 7, 8], [3, 4, 5, 8, 9], [5, 7]]

extreme_puzzle_two = {(0, 6): 5,
                      (1, 1): 3, (1, 2): 7, (1, 3): 4,
                      (2, 4): 2, (2, 5): 6, (2, 6): 4, (2, 7): 7,
                      (3, 0): 7, (3, 3): 8, (3, 4): 6, (3, 6): 9,
                      (4, 0): 4, (4, 8): 1,
                      (5, 2): 5, (5, 4): 1, (5, 5): 4, (5, 8): 8,
                      (6, 1): 7, (6, 2): 6, (6, 3): 5, (6, 4): 8,
                      (7, 5): 9, (7, 6): 6, (7, 7): 1,
                      (8, 2): 2}

return_value = sudoku_solver.solve_puzzle(extreme_puzzle_two, True, SolutionType.PROCESS_OF_ELIMINATION)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])
assert solution == result, "extreme_puzzle_two has failed"

# Now run extreme_puzzle_two using SolutionType.backtracker
# This will solve the puzzle
solution = [6, 4, 1, 7, 9, 3, 5, 8, 2,
            2, 3, 7, 4, 5, 8, 1, 9, 6,
            8, 5, 9, 1, 2, 6, 4, 7, 3,
            7, 1, 3, 8, 6, 5, 9, 2, 4,
            4, 6, 8, 9, 7, 2, 3, 5, 1,
            9, 2, 5, 3, 1, 4, 7, 6, 8,
            3, 7, 6, 5, 8, 1, 2, 4, 9,
            5, 8, 4, 2, 3, 9, 6, 1, 7,
            1, 9, 2, 6, 4, 7, 8, 3, 5]

extreme_puzzle_two_backtracker = {(0, 6): 5,
                                  (1, 1): 3, (1, 2): 7, (1, 3): 4,
                                  (2, 4): 2, (2, 5): 6, (2, 6): 4, (2, 7): 7,
                                  (3, 0): 7, (3, 3): 8, (3, 4): 6, (3, 6): 9,
                                  (4, 0): 4, (4, 8): 1,
                                  (5, 2): 5, (5, 4): 1, (5, 5): 4, (5, 8): 8,
                                  (6, 1): 7, (6, 2): 6, (6, 3): 5, (6, 4): 8,
                                  (7, 5): 9, (7, 6): 6, (7, 7): 1,
                                  (8, 2): 2}

return_value = sudoku_solver.solve_puzzle(extreme_puzzle_two_backtracker, True, SolutionType.BACKTRACKING)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])

assert solution == result, "extreme_puzzle_two_backtracker has failed"


# This puzzle is considered extremely difficult
# solve using backtracker
solution = [9, 6, 3, 4, 1, 7, 2, 8, 5,
            5, 7, 8, 9, 3, 2, 1, 4, 6,
            4, 2, 1, 6, 5, 8, 9, 3, 7,
            6, 1, 2, 3, 7, 4, 8, 5, 9,
            8, 9, 7, 1, 6, 5, 3, 2, 4,
            3, 4, 5, 8, 2, 9, 6, 7, 1,
            1, 5, 9, 7, 8, 3, 4, 6, 2,
            7, 8, 4, 2, 9, 6, 5, 1, 3,
            2, 3, 6, 5, 4, 1, 7, 9, 8]

really_really_hard_puzzle = {(0, 1): 6, (0, 8): 5,
                             (1, 0): 5, (1, 2): 8, (1, 4): 3, (1, 7): 4,
                             (2, 1): 2, (2, 5): 8,
                             (3, 0): 6,
                             (4, 3): 1, (4, 7): 2,
                             (5, 0): 3, (5, 2): 5, (5, 5): 9, (5, 8): 1,
                             (6, 0): 1, (6, 2): 9, (6, 5): 3, (6, 8): 2,
                             (7, 1): 8,
                             (8, 4): 4, (8, 6): 7}

return_value = sudoku_solver.solve_puzzle(really_really_hard_puzzle, False)
result = list()

for row in range(9):
    for col in range(9):
        result.append(return_value.puzzle_dictionary[(row, col)])

assert solution == result, "really_really_hard_puzzle has failed"

# invalid puzzle, row 6 has two 1s in it
# this should return the invalid puzzle message
invalid_puzzle = {(0, 0): 1, (0, 3): 8, (0, 4): 3, (0, 5): 2,
                  (1, 3): 7, (1, 4): 4, (1, 8): 8,
                  (2, 0): 2, (2, 1): 4, (2, 6): 7,
                  (3, 1): 5, (3, 5): 8, (3, 6): 9,
                  (4, 5): 9, (4, 6): 1, (4, 8): 5,
                  (5, 0): 9, (5, 2): 2, (5, 3): 5, (5, 4): 6,
                  (6, 0): 1, (6, 8): 1,
                  (7, 0): 8, (7, 2): 3, (7, 6): 6,
                  (8, 1): 9, (8, 2): 4, (8, 7): 2}

return_value = sudoku_solver.solve_puzzle(invalid_puzzle, False)
assert return_value.message == \
       "The input puzzle is not a valid Sudoku puzzle and cannot be solved.", \
       "An invalid puzzle did not pass the correct message back."
