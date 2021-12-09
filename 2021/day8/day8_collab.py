# day 8
# Collabed with MikeAA97 on this 
import os
import sys

'''
this functions gets the unique string 
when 'adding' or 'overlaying' two digits
-- getting the things that overlapped
'''
def add(x, y):
    l = x+y
    l = [char for char in l]
    l = ''.join(set(l))
    return(''.join(sorted(l)))
'''
set difference between two digits
'''
def diff(x, y):
    x = [ char for char in x]
    y = [ char for char in y]
    return(list(set(x) - set(y)) + list(set(y) - set(x)))


with open(os.path.join(sys.path[0],"input.txt"), "r")  as content:
    #For each line of the text file, strip the newline character, convert to integer, save to a list array
    lines =  content.readlines()
    ans = 0
    for line in lines:
        #Split into two sections, characters before | and after |
        splitLine = line.rstrip('\n').split(' | ')
        first = splitLine[0].split(' ')
        first = [''.join(sorted(x)) for x in first]
        second = splitLine[1].split(' ')
        second = [''.join(sorted(x)) for x in second]

        # determine the unique digis
        for elements in first:
            if len(elements) == 2: #1
                one = ''.join(sorted(elements))
            if len(elements) == 3: #7
                seven = ''.join(sorted(elements))
            if len(elements) == 4: #4
                four = ''.join(sorted(elements))
            if len(elements) == 7: #8
                eight = ''.join(sorted(elements))
        # detemine length 6 digis
        almost_nine = add(seven, four)
        for elements in first:
            if(len(elements) == 6):
                if(len(diff(seven, elements)) == 5):
                    six = ''.join(sorted(elements))
                if(len(diff(seven, elements)) == 3):
                    if(len(diff(almost_nine, elements)) == 1):
                        nine = ''.join(sorted(elements))
                    else:
                        zero = ''.join(sorted(elements))
        # determine the length 5 digits
        for elements in first:
            if(len(elements) == 5):
                if(len(diff(nine, elements)) > 1):
                    two = ''.join(sorted(elements))
                elif(len(diff(one, elements)) == 3):
                    three = ''.join(sorted(elements))
                elif(len(diff(one, elements)) == 5):
                    five = ''.join(sorted(elements))

        # create dictionary with decodings
        decode = { zero : 0,
                one : 1,
                two : 2,
                three : 3,
                four : 4,
                five : 5,
                six : 6,
                seven : 7,
                eight : 8,
                nine : 9}
        
        # decode second half of input
        nums = [str(decode[x]) for x in second]
        nums = int(''.join(nums))

        # add it to running sum
        ans += nums
    print(ans)