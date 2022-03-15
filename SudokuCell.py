class SudokuCell:
    def __init__(self, key, possible_values):
        self.key = key
        self.possible_values = possible_values
        self.values_count = len(possible_values)
        self.current_index = 0
        self.solution_value = 0

    def increment(self):
        if self.current_index < self.values_count - 1:
            self.current_index += 1
            return True
        else:
            return False

    def set_current_index_zero(self):
        self.current_index = 0

    def get_current_value(self):
        return self.possible_values[self.current_index]

