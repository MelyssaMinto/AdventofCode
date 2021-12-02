
# day 2: Dive!

import os
import sys

# test input
# input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    input = file.readlines()
    input = [line.rstrip('\n') for line in input]

input = [x.split(' ') for x in input]

# Part 1
horiz = 0
depth = 0

for x,y in input:
    if(x == "forward"):
        horiz+=int(y)
    elif(x=="down"):
        depth=depth+int(y)
    else:
        depth=depth-int(y)

print(horiz*depth)

# part 2
aim = 0
horiz = 0
depth = 0

for x,y in input:
    if(x == "forward"):
        horiz+=int(y)
        depth=depth + aim*int(y)
    elif(x=="down"):
        aim=aim+int(y)
    else:
        aim=aim-int(y)

print(horiz*depth)
