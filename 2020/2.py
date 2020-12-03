'''
@author: Melyssa Minto
@date: Dec 2 2020

advent of code day2 : https://adventofcode.com/2020/day/2
'''

# importing libraries
import pandas as pd 

# inputs 
input = pd.read_csv('2_input.txt', sep=" ", header=None)

# parsing input
lett = [l.replace(':', '') for l in input[1].astype(str).values.tolist()]
pw = input[2].astype(str).values.tolist()

upper = []
lower =[] 
for x in  input[0].astype(str).values.tolist():
    upper.append( [int(s) for s in x.split('-')][1] )
    lower.append( [int(s) for s in x.split('-')][0] )


# checking password 

# upper = ['3', '3', '9' ]
# lower = ['1', '1', '2']
# lett = ['a', 'b', 'c']
# pw = ['abcde', 'cdefg', 'ccccccccc']

# part 1
chk = []
for i in range(0,len(pw)):
    r = pw[i].count(lett[i]) <= int(upper[i]) and pw[i].count(lett[i]) >= int(lower[i])
    chk.append(r)
print( "valid: " + str(chk.count(True)) + " \ninvalid: " + str(chk.count(False)) )



# Part 2
chk = []
for i in range(0, len(pw)):
    #print(pw[i] + " at " + lower[i] + " : " + pw[i][int(lower[i])-1] )
    c = (pw[i][int(lower[i])-1] == lett[i]) ^ (pw[i][int(upper[i])-1] ==lett[i])
    chk.append(c)
print( "valid: " + str(chk.count(True)) + " \ninvalid: " + str(chk.count(False)) )




