from cspbase import *
from itertools import product

def toCSP(board):
    """
    A board input should look something like this:
        board = [[0, 0, 0, 0, 0, 0],
                [-1, 0, 0, 0, -1, 0],
                [0, 1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0, -1],
                [-1, 0, 0, 0, 1, 0],
                [-1, 0, 0, -1, 0, 0]]
    Where 0 means the square is colored grey, -1 means the square is colored white and 1 means the square is colored
    blue. The goal of the game is to output a coloring for each square such that no 3 squares in a row horizontally
    and vertically are colored the same and each row and column contain the same amount of blue and white colored
    squares.

    :param board: 3-in-a-Row board to be converted to CSP format
    :return: the board input converted to CSP object with appropriate constraints and variables

    """

    finalCsp = CSP("3-in-a-row")
    varsWithStructure = []
    domain = [-1, 1]
    count = 0

    #For square, we create a variable with an appropriate name, give it the appropriate domain, and add it to the CSP
    for row in board:
        #We will save the variables into rows and append them into varsWithStructure for looping over later
        tempVarRow = []
        for i in range(len(row)):
            count += 1
            var = Variable("V{}".format(count))
            if row[i] != 0:
                var.add_domain_values([row[i]])
            else:
                var.add_domain_values(domain)
            tempVarRow.append(var)
            finalCsp.add_var(var)
        varsWithStructure.append(tempVarRow)

    n = len(board)
    sameAmountTuples = []
    domains = []

    #Generate a list of lists containing n lists of domains
    for i in range(n):
        domains.append(domain)

    #Using previously made list of domains, generate every possible combination of the domains and only append
    #to our tuples list the appropriate combinations
    for combination in product(*domains):
        #The sum of the combination will be 0 iff there is an equal amount of white and blue colored squares
        if sum(combination) == 0:
            sameAmountTuples.append(combination)

    threeInARowTuples = []
    domains = []
    for i in range(3):
        domains.append(domain)

    #Same as before but now for the 3 in a row constraint tuples
    for combination in product(*domains):
        #If the sum of the combination is 3 or -3, all three squares are white or blue
        if sum(combination) != 3 and sum(combination) != -3:
            threeInARowTuples.append(combination)

    #Transpose the varsWithStructure to get a list of columns
    t=()
    for element in varsWithStructure:
        t += (element,)
    transposed = [list(x) for x in zip(*t)]

    #Loop over all the rows and add constraints with the tuple lists generated above
    i=0
    for row in varsWithStructure:
        i=i+1
        #Each row has to have the same amount of white and blue colored squares
        c = Constraint("EqualColors-Row{}".format(i), row)
        c.add_satisfying_tuples(sameAmountTuples)
        finalCsp.add_constraint(c)

        for j in range(1, len(row)-1):
            #Every three squares in a row must not be colored the same
            scope = [row[j-1], row[j], row[j+1]]
            c = Constraint("3InRow-{}".format(i), scope)
            c.add_satisfying_tuples(threeInARowTuples)
            finalCsp.add_constraint(c)

    #Loop over all the columns and add constraints with the tuple lists generated above
    i=0
    for column in transposed:
        i=i+1
        #Each column has to have the same amount of white and blue colored squares
        c = Constraint("EqualColors-Column{}".format(i), column)
        c.add_satisfying_tuples(sameAmountTuples)
        finalCsp.add_constraint(c)

        for j in range(1, len(column)-1):
            #Every three squares in a row must not be colored the same
            scope = [column[j-1], column[j], column[j+1]]
            c = Constraint("3InColumn-{}".format(i), scope)
            c.add_satisfying_tuples(threeInARowTuples)
            finalCsp.add_constraint(c)

    return finalCsp
