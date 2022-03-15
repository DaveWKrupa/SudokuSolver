from Constants import FORWARD_DIAG_CELL_KEYS, ROW_INDEX, COL_INDEX


class SudokuTester:

    def __init__(self):
        self.__puzzle_dictionary = dict()

    def test_puzzle(self, puzzle_dictionary, is_extreme_sudoku=False, row=-1, col=-1):
        self.__puzzle_dictionary = puzzle_dictionary
        self.__initialize_puzzle_dictionary()

        # It only takes one fail to fail the entire puzzle
        puzzle_is_valid = True
        if not self.__test_puzzle_rows(row):
            puzzle_is_valid = False

        if puzzle_is_valid and not self.__test_puzzle_cols(col):
            puzzle_is_valid = False

        if puzzle_is_valid and not self.__test_puzzle_boxes(row, col):
            puzzle_is_valid = False

        if is_extreme_sudoku:
            if puzzle_is_valid and not self.__test_puzzle_forward_diag(row, col):
                puzzle_is_valid = False

            if puzzle_is_valid and not self.__test_puzzle_backward_diag(row, col):
                puzzle_is_valid = False

        return puzzle_is_valid

    def __is_cell_valid(self, cell_list, row, col):
        cell_value = self.__puzzle_dictionary[(row, col)]
        if isinstance(cell_value, int) and cell_value > 0:
            if cell_list.count(cell_value) > 0:
                return False  # We have found an invalid value in a cell
            cell_list.append(cell_value)
        return True

    # Test to see any of the rows have a duplicate integer value
    def __test_puzzle_rows(self, current_row):
        try:
            if current_row == -1:
                for row in range(9):
                    row_list = list()
                    for col in range(9):
                        if not self.__is_cell_valid(row_list, row, col):
                            return False
            else:
                row_list = list()
                for col in range(9):
                    if not self.__is_cell_valid(row_list, current_row, col):
                        return False
            return True
        except KeyError:
            return False

    # Test to see any of the columns have a duplicate integer value
    def __test_puzzle_cols(self, current_col):
        if current_col == -1:
            for col in range(9):
                col_list = list()
                for row in range(9):
                    if not self.__is_cell_valid(col_list, row, col):
                        return False
            return True
        else:
            col_list = list()
            for row in range(9):
                if not self.__is_cell_valid(col_list, row, current_col):
                    return False
        return True

    # Test to see any of the cells in the forward diagonal have a duplicate integer value
    def __test_puzzle_forward_diag(self, current_row, current_col):
        diag_list = list()
        # forward diagonal cells start at the bottom left and work up to top right
        for puzzle_cell in FORWARD_DIAG_CELL_KEYS:
            if not self.__is_cell_valid(diag_list, puzzle_cell[ROW_INDEX], puzzle_cell[COL_INDEX]):
                return False
        return True

    # Test to see any of the cells in the backward diagonal have a duplicate integer value
    def __test_puzzle_backward_diag(self, current_row, current_col):
        diag_list = list()
        # the backward diagonal cells have the same row and column number
        for x in range(9):
            if not self.__is_cell_valid(diag_list, x, x):
                return False
        return True

    # Test to see any of the cells in the boxes have a duplicate integer value
    def __test_puzzle_boxes(self, current_row, current_col):

        if current_row == -1 or current_col == -1 \
                or (current_row in range(3) and current_col in range(3)):
            # top left
            box_list = list()  # reinit for each box
            for r in range(3):
                for c in range(3):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1 \
                or (current_row in range(3) and current_col in range(3, 6)):
            # top middle
            box_list = list()  # reinit for each box
            for r in range(3):
                for c in range(3, 6):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1 \
                or (current_row in range(3) and current_col in range(6, 9)):
            # top right
            box_list = list()  # reinit for each box
            for r in range(3):
                for c in range(6, 9):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1 \
                or (current_row in range(3, 6) and current_col in range(3)):
            # middle left
            box_list = list()  # reinit for each box
            for r in range(3, 6):
                for c in range(3):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1\
                or (current_row in range(3, 6) and current_col in range(3, 6)):
            # middle middle
            box_list = list()  # reinit for each box
            for r in range(3, 6):
                for c in range(3, 6):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1 \
                or (current_row in range(3, 6) and current_col in range(6, 9)):
            # middle right
            box_list = list()  # reinit for each box
            for r in range(3, 6):
                for c in range(6, 9):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1 \
                or (current_row in range(6, 9) and current_col in range(3)):
            # bottom left
            box_list = list()  # reinit for each box
            for r in range(6, 9):
                for c in range(3):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1 \
                or (current_row in range(6, 9) and current_col in range(3, 6)):
            # bottom middle
            box_list = list()  # reinit for each box
            for r in range(6, 9):
                for c in range(3, 6):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        if current_row == -1 or current_col == -1 \
                or (current_row in range(6, 9) and current_col in range(6, 9)):
            # bottom right
            box_list = list()  # reinit for each box
            for r in range(6, 9):
                for c in range(6, 9):
                    if not self.__is_cell_valid(box_list, r, c):
                        return False

        return True

    # Make sure the dictionary has all the rows and columns
    # set any unknown values (i.e. list datatype) to 0
    def __initialize_puzzle_dictionary(self):
        for row in range(9):
            for col in range(9):
                if (row, col) not in self.__puzzle_dictionary:
                    self.__puzzle_dictionary[(row, col)] = 0
                elif not isinstance(self.__puzzle_dictionary[(row, col)], int):
                    self.__puzzle_dictionary[(row, col)] = 0

