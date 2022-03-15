from collections import namedtuple
from SudokuCell import SudokuCell
from SudokuTester import SudokuTester
from SudokuPOE import SudokuPOE
from SudokuLogger import SudokuLogger, SudokuLogType
from Constants import ROW_INDEX, COL_INDEX, KEY_LIST
from datetime import datetime


class SudokuBacktracker:
    
    def __init__(self):
        self.__puzzle_dictionary = dict()
        self.__is_extreme_sudoku = False
        self.__sudoku_tester = SudokuTester()
        self.__enable_logging = False  # only for testing
        self.__suduko_logger = None

    # When this is call all the unsolved cells in the puzzle have
    # more than one possible value.
    # This uses a list as a stack to implement
    # the backtracking technique to finish solving the puzzle
    def solve_puzzle(self, puzzle_dictionary, is_extreme_sudoku):
        try:
            self.__puzzle_dictionary = puzzle_dictionary.copy()
            self.__is_extreme_sudoku = is_extreme_sudoku
            if self.__enable_logging:
                date_time = datetime.now().strftime("%m%d%Y-%H%M%S")
                self.__suduko_logger = SudokuLogger(date_time + ".log")

            # Initialize the dictionary using SudokuPOE class
            # If puzzle can be solved with that code
            # this will return true and the puzzle will be completed
            if self.__initialize_puzzle_dictionary():
                puzzle_solved = True
            else:
                # We will append and pop items on the stack_list
                stack_list = list()
                # key_list keeps all the keys for cells needing to be solved
                cell_dictionary_key_list = list()
                # For backtracking use SudokuCell
                # objects to manage the process.
                # Keep these objects in their own dictionary
                cell_dictionary = dict()
                self.__load_cell_dictionary_key_list(cell_dictionary,
                                                     cell_dictionary_key_list)

                # Append the first item onto the list
                stack_list.append(
                    cell_dictionary[cell_dictionary_key_list[0]])
                self.__write_log_file(f"Appending cell: {stack_list[-1].key}")
                counter = 0
                puzzle_solved = True
                continue_looping = True
                counter = 0
                while continue_looping:
                    self.__write_log_file(
                        f"Testing cell {stack_list[-1].key} "
                        f"value {stack_list[-1].get_current_value()}")
                    if not self.__is_valid(stack_list,
                                           cell_dictionary_key_list,
                                           stack_list[-1].key):
                        # check to see if we are on the last item
                        # in the possible_values list
                        if stack_list[-1].current_index == \
                                stack_list[-1].values_count - 1:
                            stack_list[-1].set_current_index_zero()
                            self.__write_log_file(
                                f"Popping cell: {stack_list[-1].key}")
                            stack_list.pop()
                            if len(stack_list) == 0:
                                # the starting Sudoku puzzle
                                # is not a valid
                                # puzzle and cannot be solved
                                puzzle_solved = False
                                continue_looping = False  # stop processing
                        if continue_looping:
                            # increment returns false if it would
                            # cause index out of bounds error
                            while not stack_list[-1].increment():
                                stack_list[-1].set_current_index_zero()
                                self.__write_log_file(
                                    f"Popping cell: {stack_list[-1].key}")
                                stack_list.pop()
                                if len(stack_list) == 0:
                                    # the starting Sudoku puzzle
                                    # is not a valid puzzle
                                    # and cannot be solved
                                    puzzle_solved = False
                                    continue_looping = False
                                    break
                    else:
                        if len(stack_list) == len(cell_dictionary_key_list):
                            # we have solved the puzzle
                            self.__initialize_validation_dictionary(
                                self.__puzzle_dictionary, stack_list,
                                cell_dictionary_key_list)
                            continue_looping = False
                        else:
                            item_count = len(stack_list)
                            stack_list.append(
                                cell_dictionary[
                                    cell_dictionary_key_list[item_count]])
                            self.__write_log_file(
                                f"Appending cell: {stack_list[-1].key}")
            if puzzle_solved:
                message = "Puzzle was solved"
            else:
                message = "The input puzzle is not a valid " \
                          "Sudoku puzzle and cannot be solved."
            result = namedtuple(
                "result", ["completed", "puzzle_dictionary", "message"])
            return result(puzzle_solved, self.__puzzle_dictionary, message)
        except IndexError:
            result = namedtuple(
                "result", ["completed", "puzzle_dictionary", "message"])
            return result(False, self.__puzzle_dictionary,
                          "Unexpected error processing the puzzle.")

    def __load_cell_dictionary_key_list(self, cell_dictionary, key_list):
        # Instantiate the SudokuCell objects
        # and add them to the cell_dictionary.
        # We only need the items from puzzle_dictionary where the value
        # is a list of possible values.
        for key in KEY_LIST:
            if isinstance(self.__puzzle_dictionary[key], list):
                cell_dictionary[key] = \
                    SudokuCell(key, self.__puzzle_dictionary[key])
                key_list.append(key)

    # This checks to make sure the stack list is valid *at this point*
    # when the values are inserted into the puzzle.
    # If this returns false then other numbers need to be tried.
    def __is_valid(self, stack_list, key_list, row_col):
        puzzle_dictionary_copy = self.__puzzle_dictionary.copy()
        self.__initialize_validation_dictionary(
            puzzle_dictionary_copy, stack_list, key_list)
        return self.__sudoku_tester.test_puzzle(
            puzzle_dictionary_copy, self.__is_extreme_sudoku,
            row_col[ROW_INDEX], row_col[COL_INDEX])

    # The validation dictionary is a copy of the puzzle dictionary
    # that has the values from the stack list added to it.
    # This creates a puzzle dictionary that can be tested
    # against the Sudoku rules to find out if the current
    # set of numbers needs to be changed before going further.
    def __initialize_validation_dictionary(self, puzzle_dictionary,
                                           stack_list, key_list):
        # initialize the self.__puzzle_dictionary values by setting to 0
        for key in key_list:
            puzzle_dictionary[key] = 0
    
        for sudoku_cell in stack_list:
            puzzle_dictionary[sudoku_cell.key] = \
                sudoku_cell.get_current_value()

    # When solving the puzzle using backtracking make sure
    # the puzzle dictionary has an item for every cell
    # and unsolved cells have a list of numbers
    # representing possible solutions for the cell
    # the code that does this is in the SudokuPOE class
    def __initialize_puzzle_dictionary(self):
        sudoku_poe = SudokuPOE()
        solution = sudoku_poe.solve_puzzle(
            self.__puzzle_dictionary, self.__is_extreme_sudoku)
        self.__puzzle_dictionary = solution.puzzle_dictionary
        return solution.completed

    def __write_log_file(self, message, log_type=SudokuLogType.DEBUG):
        if self.__enable_logging:
            self.__suduko_logger.write_log(message, log_type)
