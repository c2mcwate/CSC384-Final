import converter
import cspbase
import propagators

def main():
    board = [[0, 0, 0, 0, 0, 0],
             [-1, 0, 0, 0, -1, 0],
             [0, 1, 0, 0, -1, 0],
             [0, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 1, 0],
             [-1, 0, 0, -1, 0, 0]]


    boardTwo = [[0, 0, 0, 1, 0, 0],
             [0, 1, 1, 0, -1, 0],
             [0, 1, 0, 0, -1, 0],
             [0, 0, 0, 0, 0, -1],
             [0, 0, 0, 1, 0, 0],
             [0, 0, -1, 0, 0, -1]]


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

    boardSolved = solve(board, False)
    boardTwoSolved = solve(boardTwo, False)
    boardThreeSolved = solve(boardThree, False)

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

def solve(board, Print):
    CSP = converter.toCSP(board)
    prop = propagators.prop_GAC
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