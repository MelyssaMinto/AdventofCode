# --- Day 6: Tuning Trouble ---

import os
import sys
import string
# reading in input

with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]

scan = scan[0]

# scan = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# dictionary to hold letters
def find_distinct(num):
    watch = dict(zip(string.ascii_lowercase, [0] * 26))
    for i in range(0, len(scan)-num):
        sub = scan[i:i+num]
        for char in sub:
            watch[char] = watch[char] + 1
    
        if(all(x < 2 for x in watch.values())):
            print("unique substring")
            print(sub)
            print(i+num)
            break
        else:
            watch = dict.fromkeys(watch, 0)

# part 1
find_distinct(4)

# part 2
find_distinct(14)