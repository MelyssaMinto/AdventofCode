# Day 1 Calorie Counting
import os
import sys

## PART 1
# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]

# split array by spaces 
split_ind = [idx for idx, value in enumerate(scan) if value == '']

# get ind to split array
start = [0] + [num +1 for num in split_ind]
end = [num for num in split_ind] + [len(scan)]

# find the summary of cals
sums = []
for i in range(len(start)):
    # split array by indeces for each deer
    s = int(start[i])
    e = int(end[i])

    # sum calories
    cal = [int(n) for n in scan[s:e]]
    tot = sum(cal)

    # add it to an array
    sums = sums + [tot]
    end

# output max
print("Part 1: " +  str(max(sums)))

## PART 2

# sort list of sums 
sums.sort(reverse=True)
print("Part 2: " + str(sum(sums[0:3])))

