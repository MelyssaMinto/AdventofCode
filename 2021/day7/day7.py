
#  Day 7: The Treachery of Whales

import os
import sys


positions = [16,1,2,0,4,2,7,1,2,14]



# # actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    ipt = file.readlines()
    ipt = ipt[0].split(',')
    ipt = [int(elem) for elem in ipt]



def minFeul1(p):
    f = 100000000000000
    pos = None
    step = 1
    for i in range(max(p)):
        new_f = sum([abs(x - i) for x in p])
        # print("pos", i, "sum", new_f)
        if(new_f < f):
            f = new_f
            pos = i 
        step+=1
    print("positon", pos, "feul", f)



def minFeul2(p):
    f = 100000000000000
    pos = None
    step = 1
    for i in range(max(p)):
        new_f = sum([ sum(range(abs(x - i)+1)) for x in p])
        # print("pos", i, "sum", new_f)
        if(new_f < f):
            f = new_f
            pos = i 
        step+=1
    print("positon", pos, "feul", f)

# part 1
minFeul1(positions)
minFeul1(ipt)

#part 2
minFeul2(positions)
minFeul2(ipt)