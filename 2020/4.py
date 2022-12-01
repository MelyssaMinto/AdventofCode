'''
@author: Melyssa Minto
@date: Dec 2 2020

advent of code day4 : https://adventofcode.com/2020/day/4
'''

# reading in file and creating dictionary object to hold
# passport entries
feilds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',  'cid']
passport = {}

lines = [line for line in file.readlines() if line.strip()]

id = 0
count = 0 
file = open('4_input.txt', 'r') 
for line in file: 
    if  line.strip():
        id += 1
        next
    else:
        
        
        passport[id] = {}

    print("Line{}: {}".format(count, line.strip())) 

file.close()