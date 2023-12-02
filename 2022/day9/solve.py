# --- Day 9: Rope Bridge ---
import os
import sys

with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]

positions_H = [[('0', '0')]]
positions_T = [[('0', '0')]]

# make dict for the operation to move a postion (row, col)
# the left will subtract from the column, while the right 
# movement will add to the column. Moving up and down is 
# reversed for indexing purposes. so moving up will add to 
# the row while moving down subtracts from the row. 
operation = {"L": "-", "R":"+", "U":"+", "D":"-"}
tup_ind = {"L": 1, "R":1, "U":0, "D":0}

# start position
position = ["0","0"]

# for each move, calculate the new position
for move in scan:
    move = move.split(" ")
    dir = move[0]
    n = move[1]

    p = []
    for i in range(int(n)):
        # the postion + operation + how many moves
        statement =  position[tup_ind[dir]] + operation[dir] + "1"
        position[tup_ind[dir]]  = str(eval(position[tup_ind[dir]] + operation[dir] + "1"))
    
        # add to list of positions
        p.append(tuple(position))
    
    positions_H.append(p)
    if(len(p) > 1):
        positions_T.append(p[:-1])

    #print move
    # print(move)
    # print(p)

# get all positions visited
# T moves every move that H does except for the last one
positions_flat_H = [item for sublist in positions_H for item in sublist]
positions_flat_T = [item for sublist in positions_T for item in sublist]
# print(positions_T)
# print(positions_H)
# get number of unique elements (except for start)
print(len(set(positions_flat_T))-1)

# visualize

max_row = int(max([item[0] for item in positions_flat_T]))+1
max_col = int(max([item[1] for item in positions_flat_T]))+1



arr  = [['.']*max_col for i in range(max_row)]

for ind in positions_flat_T:
    print(ind)
    ro = int(ind[0])
    co = int(ind[1])
    # print( arr[ro][co])
    arr[ro][co]="#"




arr[0][0] = 's'
for r in arr[::-1]:
         print(''.join(r))