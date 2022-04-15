from collections import namedtuple
from Constants import ROW_INDEX, COL_INDEX, FORWARD_DIAG_CELL_KEYS, KEY_LIST


# Process of elimination
class SudokuPOE:
    def __init__(self):
        self.puzzle_dictionary = dict()
        self.is_extreme_sudoku = False

    def solve_puzzle(self, puzzle_dictionary, is_extreme_sudoku):
        try:
            self.puzzle_dictionary = puzzle_dictionary.copy()
            self.is_extreme_sudoku = is_extreme_sudoku

            #  For any cells that do not have an item in the puzzle dictionary
            #  need to have an item with the row-col key and value = 0
            self.__initialize_puzzle_dictionary()

            # keep track of how many cells still need to be solved
            total_unsolved_cells = \
                sum(x == 0 for x in self.puzzle_dictionary.values())
            current_unsolved_cells = total_unsolved_cells
            previous_unsolved_cells = total_unsolved_cells

            # loop through the rows and columns repeatedly
            # until all cells are solved (have only one possible number)
            while current_unsolved_cells > 0:
                # for comparison later
                previous_unsolved_cells = current_unsolved_cells
                for row_col in KEY_LIST:
                    # the puzzle cell is not solved if it has either
                    # a 0 in it or a list of possible solution numbers
                    if self.puzzle_dictionary[row_col] == 0 \
                            or isinstance(self.puzzle_dictionary[row_col],
                                          list):
                        # using the Sudoku rules narrow down the cell's value
                        # to either a single number or a list of numbers
                        cell_value = \
                            self.__get_cell_value(row_col)
                        # cell_value will be an int if solved
                        # and a list of numbers if not yet solved
                        if isinstance(cell_value, int):
                            current_unsolved_cells -= 1
                        # update the value in self.puzzle_dictionary
                        # for the cell
                        self.puzzle_dictionary[row_col] = cell_value
                if previous_unsolved_cells == current_unsolved_cells:
                    # we did not have enough starting numbers to solve
                    # the puzzle using only the process of elimination
                    break


            # We have completely solved the puzzle.
            # when previous_unsolved_cells != current_unsolved_cells,
            # because the while loop above will exit
            # before previous_unsolved_cells is reset.
            # The exception being if the puzzle cannot be
            # completely solved using process of elimination.

            if previous_unsolved_cells != current_unsolved_cells:
                message = "Puzzle was solved"
            else:
                message = "Puzzle was not solved"
            result = namedtuple(
                "result", ["completed", "puzzle_dictionary", "message"])
            return result(previous_unsolved_cells != current_unsolved_cells,
                          self.puzzle_dictionary, message)
        except IndexError:
            result = namedtuple(
                "result", ["completed", "puzzle_dictionary", "message"])
            return result(False, self.__puzzle_dictionary,
                          "Unexpected error processing the puzzle.")

    # This returns a puzzle that is unsolved, but has lists 
    # for all the unknown values showing what the available numbers are
    def get_puzzle_with_lists(self, puzzle_dictionary, is_extreme_sudoku):
        self.puzzle_dictionary = puzzle_dictionary.copy()
        self.is_extreme_sudoku = is_extreme_sudoku
        #  For any cells that do not have an item in the puzzle dictionary
        #  need to have an item with the row-col key and value = 0
        self.__initialize_puzzle_dictionary()

        for row_col in KEY_LIST:
            if self.puzzle_dictionary[row_col] == 0:
                used_numbers = self.__get_numbers_in_use(row_col)
                list_of_nums = self.__get_numbers_not_in_use(used_numbers)
                self.puzzle_dictionary[row_col] = list_of_nums
        return self.puzzle_dictionary

    # Return either an integer that is the solution to the cell
    # or a list of numbers that could be the solution to the cell
    def __get_cell_value(self, row_col):
        # get the numbers that the cell cannot be
        # then find out what is left over and pass that back
        numbers_in_use = self.__get_numbers_in_use(row_col)
        return self.__get_numbers_not_in_use(numbers_in_use)

    # Return all the numbers that cannot be the solution to the cell
    # because they already exist in other
    # cells associated with the current cell
    def __get_numbers_in_use(self, row_col):
        used_numbers = set()
        # get all the known values currently in the row
        used_numbers.update(
            self.__get_used_numbers_for_row(row_col[ROW_INDEX]))
        # get all the known values currently in the column
        used_numbers.update(
            self.__get_used_numbers_for_col(row_col[COL_INDEX]))
        # get all the known values currently
        # in the 9 cell box the cell belongs to
        used_numbers.update(self.__get_used_numbers_for_box(row_col))
        #  if the game is Extreme Sudoku
        #  need to check the diagonal cells as well
        if self.is_extreme_sudoku:
            used_numbers.update(
                self.__get_used_numbers_for_forward_diag(row_col))
            used_numbers.update(
                self.__get_used_numbers_for_backward_diag(row_col))

        return used_numbers

    # Takes the list of numbers that are currently exist in other cells
    # and returns either a single number that
    # is the solution to the current cell,
    # or a list of numbers that could be the solution to the cell.
    def __get_numbers_not_in_use(self, numbers_set):
        list_of_numbs = list()
        # loop from 1 to 9 and if the digit is not in numbers_set,
        # add it to the list
        for num in range(1, 10):
            if num not in numbers_set:
                list_of_numbs.append(num)
        # if there are more than one number in the list, send the list,
        # otherwise just send the number
        return list_of_numbs if len(list_of_numbs) > 1 else list_of_numbs[0]

    # Takes the current row of the current cell,
    # and returns all the known numbers in the other cells.
    def __get_used_numbers_for_row(self, row):
        used_numbers_set = set()
        # loop through the cells in the row
        for col in range(9):
            self.__check_add_cell_value_to_used_numbers(
                self.puzzle_dictionary[(row, col)], used_numbers_set)
        return used_numbers_set

    # Takes the current column of the current cell,
    # and returns all the known numbers in the other cells.
    def __get_used_numbers_for_col(self, col):
        used_numbers_set = set()
        # loop through the rows in the column
        for row in range(9):
            self.__check_add_cell_value_to_used_numbers(
                self.puzzle_dictionary[(row, col)], used_numbers_set)
        return used_numbers_set

    # Takes the current box of the current cell,
    # and returns all the known numbers in the other cells
    def __get_used_numbers_for_box(self, row_col):
        used_numbers_set = set()
        # loop through the cells in the 9 cell box
        # the cell value is known if it is an int and not 0
        # so add it to the set
        if row_col[ROW_INDEX] < 3 and row_col[COL_INDEX] < 3:  # top left
            for r in range(3):
                for c in range(3):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        elif row_col[ROW_INDEX] < 3 and row_col[COL_INDEX] < 6:  # top middle
            for r in range(3):
                for c in range(3, 6):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        elif row_col[ROW_INDEX] < 3:  # top right
            for r in range(3):
                for c in range(6, 9):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        elif row_col[ROW_INDEX] < 6 and row_col[COL_INDEX] < 3:  # middle left
            for r in range(3, 6):
                for c in range(3):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        elif row_col[ROW_INDEX] < 6 and row_col[COL_INDEX] < 6:  # middle
            for r in range(3, 6):
                for c in range(3, 6):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        elif row_col[ROW_INDEX] < 6:  # middle right
            for r in range(3, 6):
                for c in range(6, 9):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        elif row_col[COL_INDEX] < 3:  # bottom left
            for r in range(6, 9):
                for c in range(3):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        elif row_col[COL_INDEX] < 6:  # bottom middle
            for r in range(6, 9):
                for c in range(3, 6):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)
        else:  # bottom right
            for r in range(6, 9):
                for c in range(6, 9):
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(r, c)], used_numbers_set)

        return used_numbers_set

    # First checks to see if the current cell
    # is in the cells that make up the
    # forward diagonal list. If it is not then returns an empty list.
    # Otherwise return all the known numbers in the other cells.
    def __get_used_numbers_for_forward_diag(self, row_col):
        used_numbers_set = set()
        # forward diagonal cells start at the
        # bottom left and work up to top right
        if row_col in FORWARD_DIAG_CELL_KEYS:
            for puzzle_cell in FORWARD_DIAG_CELL_KEYS:
                if puzzle_cell != row_col:
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[puzzle_cell], used_numbers_set)

        return used_numbers_set

    # First checks to see if the current cell is in the cells that make up the
    # backward diagonal list. If it is not then returns an empty list.
    # Otherwise return all the known numbers in the other cells.
    def __get_used_numbers_for_backward_diag(self, row_col):
        used_numbers_set = set()
        # the backward diagonal cells have the same row and column number
        if row_col[ROW_INDEX] == row_col[COL_INDEX]:
            for x in range(9):
                # no need to check the cell we are currently looking at
                if x != row_col[ROW_INDEX]:
                    self.__check_add_cell_value_to_used_numbers(
                        self.puzzle_dictionary[(x, x)], used_numbers_set)

        return used_numbers_set

    # If value is an int greater than 0 add it to used_numbers_set
    def __check_add_cell_value_to_used_numbers(self, value, used_numbers_set):
        # so add it to the set
        if isinstance(value, int) and value > 0:
            used_numbers_set.add(value)

    # The puzzle dictionary passed into the solve_puzzle method
    # will likely not contain any key-value pairs for unknown cells.
    # Initialize the dictionary to add the key-value pairs for the
    # missing cells and set the value = 0
    def __initialize_puzzle_dictionary(self):
        for row in range(9):
            for col in range(9):
                if (row, col) not in self.puzzle_dictionary:
                    self.puzzle_dictionary[(row, col)] = 0
