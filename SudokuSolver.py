from SudokuBacktracker import SudokuBacktracker
from SudokuPOE import SudokuPOE
import enum

"""MIT License (MIT)
Copyright © 2022 Dave Krupa
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

""" Sudoku Rules
A standard Sudoku contains 81 cells, in a 9×9 grid, and has 9 boxes,
each box being the intersection of the first, middle, or last 3 rows,
and the first, middle, or last 3 columns.
Each cell may contain a number from one to nine,
and each number can only occur once in each row, column, and box. - Wikipedia

Extreme Sudoku is the standard but the corner to corner diagonal
cells also need to follow the row and column rule.

Easy Sudoku puzzles will provide enough numbers in the grid to solve
the puzzle using nothing but the process of elimination.
That is when looping through the cells there will always be at least
one additional cell that has been reduced to one number,
allowing the next loop a chance to find more
cells' numbers.

Hard Sudoku puzzles will not provide enough numbers to solve
the puzzle through the process of elimination.
At some point all the cells that need to be solved
will have 2 or more possible values.
When this point is reached we need to change strategies.
To complete the puzzle the code will take the results
of the currently processed puzzle, and use a 
backtracking technique to find the solution.

The puzzle_dictionary passed into the solve_puzzle method represents
the Sudoku puzzle in its initial state.
The dictionary key is a tuple that represents one of the
cells in the puzzle. (row, column)
For every known value in the puzzle add an item
to the dictionary.
Unknown puzzle cells can be represented by a 0 in the
dictionary, but are not required.
(e.g. (4, 5): 0, (4, 6): 0, (4, 7): 0, (4, 8): 0,)

The solve_puzzle method returns a dictionary in the
same format, completed.

Example puzzle for input:
puzzle_dictionary = {(0, 1): 5, (0, 3): 7, (0, 5): 8, (0, 7): 3,
                     (1, 0): 7, (1, 2): 1, (1, 4): 2, (1, 8): 9,
                     (2, 0): 9, (2, 5): 3, (2, 7): 4, (2, 8): 7,
                     (3, 2): 7, (3, 3): 6, (3, 5): 2, (3, 6): 3, (3, 8): 5,
                     (4, 4): 7,
                     (5, 0): 2, (5, 2): 9, (5, 3): 3, (5, 5): 5, (5, 6): 4,
                     (6, 0): 3, (6, 1): 2, (6, 3): 8, (6, 8): 6,
                     (7, 0): 6, (7, 4): 1, (7, 6): 2, (7, 8): 3,
                     (8, 1): 7, (8, 3): 2, (8, 5): 6, (8, 7): 8}
"""


class SolutionType(enum.Enum):
    PROCESS_OF_ELIMINATION = 0
    BACKTRACKING = 1


class SudokuSolver:

    def solve_puzzle(self, puzzle_dictionary,
                     is_extreme_sudoku=False,
                     solution_type=SolutionType.BACKTRACKING):

        if solution_type == SolutionType.BACKTRACKING:
            # Use the backtracker method to solve the puzzle
            sudoku_backtracker = SudokuBacktracker()
            return sudoku_backtracker.solve_puzzle(puzzle_dictionary,
                                                   is_extreme_sudoku)
        else:
            # Use the process of elimination to either solve the puzzle,
            # or solve as much as possible
            sudoku_poe = SudokuPOE()
            return sudoku_poe.solve_puzzle(puzzle_dictionary,
                                           is_extreme_sudoku)

