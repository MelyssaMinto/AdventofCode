# Day 1 Sonar Sweep
import os
import sys

# test input
# scan = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [int(line.rstrip('\n')) for line in scan]


# part 1: count the number of times a depth measurement increases
Sum = 0
for i in range(0, len(scan)-1):
    if scan[i + 1] > scan[i]:
        Sum+=1

print("the number of increases: " , Sum)

# part 2: count the number of times the sum of measurements in this sliding window increases 

window_sum = 0
for i in range(0, len(scan)-2):

    if sum(scan[i+1:i+4]) > sum(scan[i:i+3]):
        window_sum+=1

print("the number of increases in window is : " , window_sum)
