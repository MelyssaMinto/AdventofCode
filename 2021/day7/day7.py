
#  Day 7: The Treachery of Whales

import os
import sys


positions = [16,1,2,0,4,2,7,1,2,14]


# # actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    ipt = file.readlines()
    ipt = ipt[0].split(',')
    ipt = [int(elem) for elem in ipt]


def minFeul(p, part1=False):
    if(part1):
        # get all the residual sums
        f = [sum([ abs(x - i) for x in p]) for i in range(max(p))]
    else:
        # get all the sums of the sequence 1:resudial
        f = [sum([ sum(range(abs(x - i)+1)) for x in p]) for i in range(max(p))]
      
    # sort sums to find minimum
    # -- using enumerate
    f = [(val, i) for i,val in enumerate(f)]
    f.sort(key=lambda x:x[0])
    # -- using zip
    # f = zip(f, range(len(f))) 
    # f = sorted(f, key = lambda x:x[0])

    # show solution
    print("(fuel, postion):", f[0])

    


# part 1
minFeul(positions, part1=True)
minFeul(ipt, part1=True)

#part 2
minFeul(positions)
minFeul(ipt)

