# day3
import os
import sys
import string

# reading in input

with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]


# create priority dict
letts = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority = dict(zip(letts, range(1, 53)))

# part 1
def findCommon(input):
    p = []
    for s in input:
        l = int(len(s)/2)
        one = s[0:l]
        two = s[l:]

        common = ''.join(set(one).intersection(two))
        p.append(priority[common[0]])

    print("Part 1: " + str(sum(p)))

findCommon(scan)
    

# part 2
def findCommon3(input):
    p = []
    for i in range(0, len(input), 3):
        one = input[i]
        two = input[i+1]
        three = input[i+2]

        common = ''.join(set(one).intersection(two).intersection(three))
        p.append(priority[common[0]])

    print("Part 2: " + str(sum(p)))

findCommon3(scan)
