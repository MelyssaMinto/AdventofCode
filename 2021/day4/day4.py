# day4 Giant Squid
# day 3: Binary Diagnostic
import os
import sys
import numpy as np 


# test input 
# input = [ 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
# b1 = [[22, 13 ,17 ,11 , 0], 
#           [8 , 2 ,23 , 4 ,24  ], 
#           [21 , 9 ,14 ,16 , 7 ], 
#           [6 ,10 , 3, 18,  5 ], 
#           [1 ,12 ,20 ,15, 19  ] ]
# b2 = [ [3, 15,  0,  2 ,22 ],
#       [9, 18, 13, 17 , 5  ],
#       [19,  8,  7, 25, 23],
#       [20, 11, 10, 24 , 4 ],
#       [14 ,21 ,16, 12 , 6]]
# b3 = [ [14, 21, 17, 24,  4],
#       [10 ,16 ,15,  9, 19],
#       [18 , 8, 23, 26, 20],
#       [22, 11 ,13 , 6 , 5],
#       [2 , 0 ,12,  3 , 7]]



# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    input = file.readlines()
    input = input[0].split(',')
    input = [int(elem) for elem in input]


with open(os.path.join(sys.path[0],"boards.txt"), "r") as file:
    boards = file.readlines()
    boards = [line.strip('\n').strip(' ') for line in boards]
    # Removing erroneous values
    boards = [elem for elem in boards if elem != '']
    # split each line by space and convert tp int
    boards = [elem.replace('  ', ' ').split(' ') for elem in boards]
    boards = [[int(x) for x in l ] for l in boards]
    # group/slice every five lists in nested list to create a board
    boards = [list(boards[i:i+5]) for i in range(0, len(boards), 5)]


# define functions
'''
function to cross numbers off of bingo board once called
the marker is a None variable so that it can be easily 
filtered when the board is summed. 

returns marked bingo card
'''
def crossNum(value, m):
    for row, x in enumerate(m):
        for col, num in enumerate(x):
            if num  == value:
                m[row][col] = None
                #print(num, " is at ", row, ",",  col)
    return(m)

'''
checks for BINGO - if all elements in row or column 
are None. 

Prints the challenge solution of the sum of 
the winning card * the last number called
'''
def checkBingo(card, winningNum):
    # track winning boards
    # check rows
    for row in card:
        if ( all(val == None for val in row)):
            print("Bingo!")
            print(sumCard(card)*winningNum)
            return('break')
            break
    
    # check cols
    card_transpose = [[card[j][i] for j in range(len(card))] for i in range(len(card[0]))]
    for row in card_transpose:
        if ( all(val == None for val in row)):
            print("Bingo!")
            print(sumCard(card)*winningNum)
            return('break')
            break

'''
returns the sum off all ints in bingo card. 
'''
def sumCard(card):
    Sum = 0 
    for row in card:
        rowSum = sum([i for i in row  if type(i)== int])
        Sum = Sum + rowSum
    return(Sum)


'''
play bingo given the numbers called (valiue), the bingo cards
at play (cards), and the game mode (regular or Last Win)
'''
def play(values, cards, lasWin=False):
    # track winning cards
    winningCards = set()
    # loop through all  numbers called
    for val in values:
        # loop through each card to mark number called if 
        # present and check if any cards have bingo
        for i, card in enumerate(cards):
            # marking cards
            card = crossNum(val, card)
            # checking bingo
            result = checkBingo(card, val)
            # if the last board that wins is wanted 
            # play bingo until the number of winning 
            # cards are equal to all cards
            if(lasWin):
                if(result == "break"):
                    winningCards.add(i)
                    if(len(winningCards) == len(cards)):
                        print("LAST")
                        return
            # otherwise, stop at first win
            elif(result == "break"):
                print("woohoo")
                return
            



#part 1
# play(input, [b1, b2, b3])
# play(input, boards)

# part 2
#play(input, [b1, b2, b3], True)
play(input, boards, True)

