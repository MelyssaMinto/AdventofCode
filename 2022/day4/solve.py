# --- Day 4: Camp Cleanup ---
import os
import sys
import csv

# reading in input
with open(os.path.join(sys.path[0],"input.txt"), "r") as inf:
    reader = csv.reader(inf, delimiter=",")
    data = list(zip(*reader))


# part 1
# parsing input into a lists of ranges 
p1 = data[0]
p2 = data[1]

p1 = [x.split("-") for x in p1]
ranges1 = [range(int(x[0]), int(x[1])+1) for x in p1]
p2 = [x.split("-") for x in p2]
ranges2 = [range(int(x[0]), int(x[1])+1) for x in p2]
r = zip(ranges1, ranges2)

# find the sets of ranges contained in each other
overlap1 = [set(x).issubset(y) for (x,y) in zip(ranges1, ranges2)]
overlap2 = [set(x).issubset(y) for (x,y) in zip(ranges2, ranges1)]
overlap = [ o1 or o2 for (o1, o2) in zip(overlap1, overlap2)]
# print(overlap)
print(sum(overlap))


### part 2
l1 = [set(x).intersection(set(y)) for (x,y) in zip(ranges1, ranges2)]
overlaps = [len(s) > 0 for s in l1]
print(sum(overlaps))