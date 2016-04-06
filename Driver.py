import converter
import cspbase
import propagators

def main():
    #Regular 6x6 board
    board = [[0, 0, 0, 0, 0, 0],
             [-1, 0, 0, 0, -1, 0],
             [0, 1, 0, 0, -1, 0],
             [0, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 1, 0],
             [-1, 0, 0, -1, 0, 0]]

    #Regular 6x6 board
    boardTwo = [[0, 0, 0, 1, 0, 0],
             [0, 1, 1, 0, -1, 0],
             [0, 1, 0, 0, -1, 0],
             [0, 0, 0, 0, 0, -1],
             [0, 0, 0, 1, 0, 0],
             [0, 0, -1, 0, 0, -1]]

    #14x14 Board
    boardThree = [[0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, -1, -1, 0],
                [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, -1,0, 0, 0, 0, -1, 1, 0, -1,0, 0, 0],
                [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, -1, 0, -1],
                [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0],
                [1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0],
                [0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, -1],
                [1, -1, 0, -1, 1, 0, 0, 1, 0, 0, 1, 0, 0, -1],
                [1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0]]


    boardOneSolution =  [[1, -1, -1, 1, 1, -1],
                        [-1, 1, 1, -1, -1, 1],
                        [1, 1, -1, 1, -1, -1],
                        [1, -1, -1, 1, 1, -1],
                        [-1, -1, 1, -1, 1, 1],
                        [-1, 1, 1, -1, -1, 1]]

    boardTwoSolution =  [[1, -1, -1, 1, 1, -1],
                        [-1, 1, 1, -1, -1, 1],
                        [-1, 1, -1, 1, -1, 1],
                        [1, -1, 1, -1, 1, -1],
                        [-1, -1, 1, 1, -1, 1],
                        [1, 1, -1, -1, 1, -1]]

    boardThreeSolution =    [[1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1],
                            [-1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1],
                            [1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1],
                            [-1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1],
                            [-1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1],
                            [1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1],
                            [-1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1],
                            [1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1],
                            [-1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1],
                            [-1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1],
                            [1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1],
                            [-1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1],
                            [1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1],
                            [1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1]]

    boardSolved = solve(board, False, propagators.prop_GAC)
    boardTwoSolved = solve(boardTwo, False, propagators.prop_GAC)
    boardThreeSolved = solve(boardThree, False, propagators.prop_GAC)

    if boardSolved == boardOneSolution:
        print("Test case 1 passed")
    else:
        print("Test case 1 failed")

    if boardTwoSolved == boardTwoSolution:
        print("Test case 2 passed")
    else:
        print("Test case 2 failed")

    if boardThreeSolved == boardThreeSolution:
        print("Test case 3 passed")
    else:
        print("Test case 3 failed")

def solve(board, Print, prop):
    """
    :param board: 3-In-A-Row board to solve
    :param Print: Boolean which indicates whether or not to print the solution in console
    :param prop: Propagator function (either FC or GAC)
    :return: return board with values assigned by backtracking if a solution exists.
    """
    CSP = converter.toCSP(board)
    backtracker = cspbase.BT(CSP)
    backtracker.bt_search(prop)
    if(Print):
        backtracker.trace_on()
    values = []

    for var in CSP.get_all_vars():
         values.append(var.assignedValue)

    i=0
    for row in board:
        for j in range(len(row)):
            row[j]=values[i]
            i = i +1
    if Print:
        for row in board:
            print(row)

    return board

if __name__ == "__main__":
    main()