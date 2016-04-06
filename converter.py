from cspbase import *
from itertools import product

def toCSP(board):
    finalCsp = CSP("3-in-a-row")
    vars = []
    consSameList = []
    varsWithStructure = []

    domain = [-1, 1]
    count = 0
    for row in board:
        temp = []
        for i in range(len(row)):
            count += 1
            var = Variable("V{}".format(count))
            if row[i] != 0:
                var.add_domain_values([row[i]])
            else:
                var.add_domain_values(domain)
            temp.append(var)
            vars.append(var)
            finalCsp.add_var(var)
        varsWithStructure.append(temp)

    n = len(board)
    i=0


    sameAmountTuples = []
    domains = []
    for i in range(n):
        domains.append(domain)

    for combination in product(*domains):
        if sum(combination) == 0:
            sameAmountTuples.append(combination)

    for row in varsWithStructure:
        i=i+1
        c = Constraint("EqualColors-Row{}".format(i), row)
        c.add_satisfying_tuples(sameAmountTuples)
        finalCsp.add_constraint(c)

    t=()
    for element in varsWithStructure:
        t += (element,)
    transposed = [list(x) for x in zip(*t)]

    i=0
    for column in transposed:
        i=i+1
        c = Constraint("EqualColors-Column{}".format(i), column)
        c.add_satisfying_tuples(sameAmountTuples)
        finalCsp.add_constraint(c)






    print(1)
