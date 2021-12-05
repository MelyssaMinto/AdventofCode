# day 3: Binary Diagnostic
import os
import sys


# test input 
# input = [ "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    input = file.readlines()
    input = [line.rstrip('\n') for line in input]

def findmode(l, reg=True):
    # find mode of binary input
    # when reg = true, the mode is found, and if thereus a tiem 1 is returned
    # when reg = FALSE, the anti mode is found and if there is a tie, 0 is returned
    ones = l.count('1')
    zeros = l.count('0')
    if(reg):
        if(ones >= zeros):
            return('1')
        else:
            return('0')
    else:
        if(zeros <= ones):
            return('0')
        else:
            return('1')


def findRates(l):
    gamma = ''
    epsillon = ''
    for index, x  in enumerate(l[0]):
        # get ith character for each string in list
        c = [x[index][:] for x in l]
        # find the mode or antu mode of c
        mode = findmode(c)
        anti_mode =  findmode(c, reg=False)
        # append mode and antimode to gamma and epsillon respectively
        gamma += mode
        epsillon += anti_mode

    #print("g, e: ", [gamma, epsillon])
    return([gamma, epsillon])


# part 2
def findO_CO(l):
    # start off with full input and gamma and epsilon rates
    o = co2 = l
    g ,e = findRates(l)

    # iterate through oxygen list until one element is left
    for index in range(len(l[0])):
        if(len(o)==1):
            break
        else:
            # keep element if ith char is the mode of list
            keepBool = [x[index] == g[index] for x in o]
            o = [x for x, y in zip(o, keepBool) if y]
            # recalculate mode and antimode of filtered list 
            g ,e = findRates(o)
            # return last element
            ogr = o[0]
    
    # start off with famma and epsolon rates for full input
    g ,e = findRates(l)
    # iterate through oxygen list until one element is left
    for index in range(len(l[0])):
        if(len(co2) == 1):
            break
        else:
            # keep element if the ith char is the antimode of list
            keepBool = [x[index] == e[index] for x in co2]
            co2 = [x for x, y in zip(co2, keepBool) if y]
            # recalculate mode and antimode of filtered list
            g ,e =  findRates(co2)
            # return last element
            co2r = co2[0]

    # print("OGR, CO2GR: ", [ogr, co2r])
    # print("OGR, CO2GR: ", [int(ogr, 2), int(co2r, 2)])
    # print(int(ogr, 2) * int(co2r,2))
    return(ogr, co2r)


gamma, epsillon = findRates(input)
print("part1 = ", int(gamma, 2) * int(epsillon,2))

ogr, co2r = findO_CO(input)
print("part2 = ", int(ogr, 2) * int(co2r,2))




