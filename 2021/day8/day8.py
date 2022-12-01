#  Day 8: Seven Segment Search 

import os
import sys





# test input:
ipt = ['acedgfb', 'cdfbe', 'gcdfa' ,'fbcad' ,'dab' ,'cefabd' ,'cdfgeb', 'eafb', 'cagedb', 'ab', "|",'cdfeb', 'fcadb', 'cdfeb' ,'cdbaf']

# create dictionary for each number 
number_dict = {'acedgfb': 8,
                'cdfbe': 5,
                'gcdfa': 2,
                'fbcad': 3,
                'dab': 7,
                'cefabd': 9,
                'cdfgeb': 6,
                'eafb': 4,
                'cagedb': 0,
                'ab': 1 }




def unique_segment(s):
    # breaking list into pattern and number output
    pattern = s[:-5]
    # print("pattern", pattern)
    output = s[-4:]
    # print("output", output)

    # getting the length of each string
    output_len = [len(x) for x in output]
    # print(output_len)

    ind_unique = [x for x,y in enumerate(output_len) if y == 2 or y == 4 or y == 3  or y == 7]
    print(ind_unique)

    # print(ind_unique)
    return(len(ind_unique))

def decode_segment(s):
     # breaking list into pattern and number output
    pattern = s[:-5]
    # print("pattern", pattern)
    output = s[-4:]
    output = ["".join(sorted(x)) for x in output]
    # print("output", output)

    decode = [ str(sorted_dict[x]) for x in output]
    print(''.join(decode))



def part1(text):
    with open(os.path.join(sys.path[0],text), "r") as file:
        lines = file.readlines()
        total_unique = 0
        for line in lines:
            ipt = line.strip('\n')
            ipt = ipt.split(' ')
            total_unique += unique_segment(ipt)

        print("TOTAL :", total_unique)

def part2(text):
    with open(os.path.join(sys.path[0],text), "r") as file:
        lines = file.readlines()
        total_unique = 0
        for line in lines:
            ipt = line.strip('\n')
            ipt = ipt.split(' ')
            total_unique += int(decode_segment(ipt))

        print("TOTAL :", total_unique)


unique_segment(ipt)
part1("test_input.txt")
# part1("input.txt")

# decode_segment(ipt)
# part2("test_input.txt")