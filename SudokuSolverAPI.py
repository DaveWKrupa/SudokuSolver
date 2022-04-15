from flask import Flask
from SudokuSolver import SudokuSolver, SolutionType

app = Flask(__name__)


@app.route('/')
def index():
    return {"Greetings": "How are you?"}


@app.route('/submit_puzzle/<numbers>', methods=['POST', 'GET'])
def submit_puzzle(numbers):

    if len(numbers) == 81 and numbers.isnumeric():
        num_index = 0
        puzzle_dictionary = dict()
        for row in range(9):
            for col in range(9):
                number = int(numbers[num_index])
                if number > 0:
                    puzzle_dictionary[(row, col)] = number
                num_index += 1

        sudoku_solver = SudokuSolver()
        return_value = sudoku_solver.solve_puzzle(puzzle_dictionary, False, SolutionType.BACKTRACKING)
        completed_puzzle = ""
        for row in range(9):
            for col in range(9):
                completed_puzzle += str(return_value.puzzle_dictionary[row, col])
            completed_puzzle += '\n'
        return {"Completed puzzle": str(completed_puzzle)}


if __name__ == '__main__':
    # debug mode
    app.run(host="0.0.0.0", debug=True, port=6060)







# 100832000000740008240000700050008900000009105902560000600000001803000600094000020
# solution = [1, 7, 5, 8, 3, 2, 4, 9, 6,
#             3, 6, 9, 7, 4, 5, 2, 1, 8,
#             2, 4, 8, 1, 9, 6, 7, 5, 3,
#             4, 5, 1, 3, 7, 8, 9, 6, 2,
#             7, 3, 6, 4, 2, 9, 1, 8, 5,
#             9, 8, 2, 5, 6, 1, 3, 7, 4,
#             6, 2, 7, 9, 8, 4, 5, 3, 1,
#             8, 1, 3, 2, 5, 7, 6, 4, 9,
#             5, 9, 4, 6, 1, 3, 8, 2, 7]