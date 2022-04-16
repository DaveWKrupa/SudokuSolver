# SudokuSolver
This project provides classes that will solve Sudoku puzzles.

The SudokuPOE class uses the process of elimination to either solve,
or narrow down the possible values for each blank cell in the puzzle.

The SudokuBacktracker class uses an algorithm described here:

https://en.wikipedia.org/wiki/Sudoku_solving_algorithms

The SudokuSolver class takes in as an argument to use either the 
process of elimination or the backtracking method. 

The difference is the process of elimination method will only solve
easy puzzles. It will stop when it is no longer capable of reducing
cells to a single possible value, so difficult puzzles will not be solved completely.

The SudokuBacktracker class uses the SudokuPOE class to reduce the 
puzzles possible numbers in each cell before using the backtracking method
to complete the solution. This eliminates a lot of processing beforehand.

There is also an Extreme Suduko parameter, which when true says that 
both the diagonal lines in the puzzle also have to be 1 - 9.
