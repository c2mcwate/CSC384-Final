import converter
import cspbase
import propagators

def main():
    board = [[0, 0,0,0,0,0],
             [-1,0,0,0,-1,0],
             [0,1,0,0,-1,0],
             [0,0,0,0,0,-1],
             [-1,0,0,0,1,0],
             [-1,0,0,-1,0,0]]

    print(board)

    CSP = converter.toCSP(board)
    # prop = propagators.prop_GAC
    # backtracker = cspbase.BT(CSP)
    # backtracker.bt.search(prop)
    # backtracker.trace_on()
    #
    # for var in CSP.get_all_vars():
    #     print(var.name)
    #     print("Value = {}".format(var.assignedValue))

if __name__ == "__main__":
    main()