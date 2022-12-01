#day 6: laternfirsh

import os
import sys


# test input:
test = [3,4,3,1,2]

# # actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    ipt = file.readlines()
    ipt = ipt[0].split(',')
    ipt = [int(elem) for elem in ipt]




def lanternfish(days, initialPop, p=False):
    timer = initialPop
    reset_cond = -1
    reset_val = 6
    spawn = 8 

    for i in range(days):
        # decrease timer by one 
        timer = [(x-1) for x in timer]

        # if timer is 0 - SPAWN * Reset
        num_spawns = len([ x for x in timer if x == reset_cond])
        if(num_spawns > 0):
            # create new spawns
            new_spawns = [y for x in range(num_spawns) for y in [spawn]]
            # add mew spawns to list
            timer = timer + new_spawns
            #reset internal clocks
            timer = [reset_val if x == -1 else x for x in timer]
        # print list as it grows
        if(p):
            print(i+1, timer)

    print(len(timer))




lanternfish(18, test, True)
lanternfish(30, test, True)
laternfish(256, ipt) naive approach is too memory intensive