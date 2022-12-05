# --- Day 5: Supply Stacks ---
import os
import sys
import pandas as pd



# print(reader)

def read_stacks(NAME, NROWS, NCOLS):
    # read in as data frome
    data = pd.read_csv(os.path.join(sys.path[0],NAME), nrows =NROWS, header=None, sep= " ")
    data = data.iloc[:, 0:NCOLS]

    # convert to stack
    stack = data.transpose().values.tolist()
    stack = [list(filter(lambda x: x == x, inner_list)) for inner_list in stack]

    return(stack)


def read_operations(NAME, LINE):
    operations = pd.read_csv(os.path.join(sys.path[0],NAME), header=None, sep= " ", skiprows=LINE)
    operations = operations.iloc[:, [1,3,5]]
    operations.columns = ["n", "from", "to"]

    return(operations)


def solve(filename, NR, NC, startLine):
    # read in stacks 
    stack = read_stacks(filename, NR,NC )

    # read in operations
    operations = read_operations(filename, startLine)
    # perform operations
    for index, row in operations.iterrows():
        m = row['n']
        fr = row['from'] -1
        to = row['to'] -1

        for moves in range(m):
            if(len(stack[fr]) > 0):
                stack[to] =  [stack[fr][0]] + stack[to]
                stack[fr].pop(0)

    # get the top of each stack

    t = ''.join([x[0].strip("[").strip("]") for x in stack])

    print(t)

def solve_order(filename, NR, NC, startLine):
    # read in stacks 
    stack = read_stacks(filename, NR,NC )
    operations = read_operations(filename, startLine)
    # perform operations
    for index, row in operations.iterrows():
        m = row['n']
        fr = row['from'] -1
        to = row['to'] -1

        if(len(stack[fr]) < m ):
            moves = len(stack[fr])
        else:
            moves = m

        stack[to] =  stack[fr][0:moves] + stack[to]
        del stack[fr][0:moves]

    # get the top of each stack
    print(stack)

    t = ''.join([x[0].strip("[").strip("]") for x in stack])

    print(t)


solve("test.txt", 3, 3, 5)
solve("input.txt", 8,9,10)
solve_order("test.txt", 3, 3, 5)
solve_order("input.txt", 8,9,10)
