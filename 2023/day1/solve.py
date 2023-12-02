# Day 1 --- Day 1: Trebuchet?! ---

import os
import sys
import re 

## PART 1
# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]


ints_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ints_2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# mapping = dict(map(lambda i,j : (i,j) , ints_2 + ints_1 ,ints_1 + ints_1))
mapping = dict(map(lambda i,j : (i,j) , ints_2  ,ints_1 ))


def check_int(l):
    calib_val = []
    first = ""
    for arr in l:
        # check for first int then break
        for elem in arr:
            if(elem in ints_1):
                first = elem
                break
        # check for last int then break
        for elem in arr[::-1]:
            if(elem in ints_1):
                last = elem
                break
        calib_val.append(int(first + last))
   # print("calibration values")
    # print(calib_val)       
    print("sum: ")
    print(sum(calib_val))  

def part2(l):
    calib_val = []
    for string in l:
        print(string)
        # track the index of each integer
        tracker = dict.fromkeys(ints_1)
        for ints in ints_2:
            print("int " + ints + ": ")
            if(ints in string and mapping[ints] in string):
                ind1 = string.index(ints)
                ind2 = string.index(mapping[ints])
                print(str(ind1) + " and " + str(ind2))
                if((ind1 == 0 and ind2+1 == len(string)) or (ind2 == 0 and ind1+1 == len(string))):
                    tracker[ints] = 0
                    print("first and last is " + mapping[ints])
                elif ind1 < ind2:
                    tracker[ints] = ind1
                    print("--> " + str(ind1))
                else:
                    tracker[ints] = ind2
                    print("--> " + str(ind2))
            elif(ints in string):
                 print(string.index(ints))
                 tracker[ints]  = string.index(ints)
            elif(mapping[ints] in string):
                 print(string.index(mapping[ints]))
                 tracker[ints]  = string.index(mapping[ints])
            else:
                 tracker[ints] = None

        # get the first and last 
        first_ind = min(x for x in tracker.values() if x is not None)
        last_ind = max(x for x in tracker.values() if x is not None)
        first = [key for key in tracker if tracker[key] == first_ind]
        last = [key for key in tracker if tracker[key] == last_ind]
        print(string + " ==> " + mapping[first[0]] + mapping[last[0]])
        calib_val.append(int(mapping[first[0]] + mapping[last[0]]))
    # print("calibration values")
    # print(calib_val)       
    print("sum: ")
    print(sum(calib_val))  

def CntSubstr(pattern, string):
    a = [m.start() for m in re.finditer(
        '(?={0})'.format(re.escape(pattern)), string)]
    return a

def solve_part2(s):
    calib_val = []
    mapping = dict(map(lambda i,j : (i,j) , ints_2+ints_1  ,ints_1+ints_1 ))
    for string in s:
        print(string)
        # res = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", string)
        pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
        res = [match.group(1) for match in pattern.finditer(string)]
        first = mapping[res[0]]
        last = mapping[res[len(res)-1]]
        val = first + last
        calib_val.append(int(val))
        print(res)
        print(val)
    print(sum(calib_val))





# part 1
part1 = [[x for x in y] for y in scan]
print("part1")
check_int(part1)


solve_part2(scan)