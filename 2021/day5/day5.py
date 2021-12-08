# Day 5: Hydrothermal Venture
import os
import sys
import numpy as np 

# test input
# ipt = [
# '0,9 -> 5,9',
# '8,0 -> 0,8',
# '9,4 -> 3,4',
# '2,2 -> 2,1',
# '7,0 -> 7,4',
# '6,4 -> 2,0',
# '0,9 -> 2,9',
# '3,4 -> 1,4',
# '0,0 -> 8,8',
# '5,5 -> 8,2']

# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    ipt = file.readlines()
    ipt = [line.rstrip('\n') for line in ipt]

# format input
input = [elem.split( ' -> ') for elem in ipt]
input = [[tuple(map(int, x.split(','))) for x in p ] for p in input]

# get the max number for array contruction
x = [elem.replace(' -> ', ',').split(',') for elem in ipt]
x = sum(x, [])
x = [ int(elem) for elem in x]
arr_size = max(x)+1


def checkOverlap(l, arr_size):
    diagram = np.zeros((arr_size, arr_size))
     # loop through esach coordiante and add markers accordingly
    for pair in l:
        # extract coordinates 
        x1 = pair[0][0]
        y1 = pair[0][1]
        x2 = pair[1][0]
        y2 = pair[1][1]

        # calculate max and min for appropriate slicing
        # I think there is a way to get arround this
        maxx = max(x1, x2)
        minx = min(x1, x2)
        maxy = max(y1, y2)
        miny = min(y1, y2)

        # calculate slope
        # if the line is diagnal slope = 1 or -1
        if(y2 - y1 != 0):
            slope = (x2 - x1)/ (y2-y1)
        else:
            slope = None

        # vertical
        if(x1 == x2):
            diagram[miny:(maxy+1), x1 ] =  diagram[miny:(maxy+1), x1 ] + 1
        # horizontal
        elif(y1 == y2):
                diagram[y1, minx:(maxx+1)] = diagram[y1, minx:(maxx+1)] + 1 
        # # postive diagnal
        # elif(slope == 1):
        #     for k,j in zip(range(miny, maxy+1), range(minx, maxx+1)):
        #          diagram[k, j] = diagram[k, j] + 1
        # #negative diagnal
        # elif(slope == -1):
        #      for j,k  in zip(range(maxx, minx-1, -1), range(miny, maxy+1)):
        #          diagram[k, j] = diagram[k, j] + 1

    # how many cells 2 or more lines 
    print(np.count_nonzero( diagram > 1))




checkOverlap(input, arr_size)