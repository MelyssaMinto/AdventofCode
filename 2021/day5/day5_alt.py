from posixpath import split
import numpy as np
import os
import sys



with open(os.path.join(sys.path[0],"input.txt"), "r") as content:
    #For each line of the text file, strip the newline character, convert to integer, save to a list array
    lines = [line.rstrip('\n') for line in content.readlines()]

    splitLine = []
    for line in lines:
        splitLine.append(line.split(" -> ")) 
    # list comprehension version
    # [ (your desired result) for interator in list]
    # [line.split(" -> ") for line in lines] might be better 

    for elements in splitLine:
        for count, pairs in enumerate(elements):
            elements[count] = pairs.split(",")
    # list comprehenson version - nested
    # splitLine = [[pairs.split(",") for pairs in elements] for elements in splitLine]

#print(splitLine)


mi = 0
ma = 0
keeper = []
for test_line in splitLine:
    if test_line[0][0] == test_line[1][0]:
        #print("Case 1")
        static_number = test_line[0][0]
        if test_line[0][1] > test_line[1][1]:
            mi = int(test_line[1][1])
            ma = int(test_line[0][1])
        else:
            mi = int(test_line[0][1])
            ma = int(test_line[1][1])
        k = []
        for adds in range(mi+1, ma):
            k = k  + [[static_number, str(adds)]]
        k = test_line + k
        keeper.append(k)
        # print(test_line)
    elif test_line[0][1] == test_line [1][1]:
        #print("Case 2")
        static_number = test_line[0][1]
        if test_line[0][0] > test_line[1][0]:
            mi = int(test_line[1][0])
            ma = int(test_line[0][0])
        else:
            mi = int(test_line[0][0])
            ma = int(test_line[1][0])
        k = []
        for adds in range(mi+1, ma):
            k = k  + [[str(adds),static_number]] 
        k = test_line + k 
        keeper.append(k)
        # print(test_line)
    


# print('list:', keeper)
splitLine = keeper
diags = []
for elements in splitLine:
    if (elements[0][0] != elements[1][0]) & (elements[0][1] != elements[1][1]):
        diags.append(elements)
# print('diags:',  diags)

# print('splitLine:' , splitLine)
# [ (your desired result) for interator in list given a condition]
splitLine = [item for item in splitLine if item not in diags]
# print('splitLine:' , splitLine)


flat_list = [item for sublist in splitLine for item in sublist]
# print("flatlist:", flat_list)

# coord_list =  [tuple(x) for x in flat_list ]
# print('coord_list:', coord_list)

# # parsing list to get max value
# x = [[i for i in t] for t in flat_list]
# x = sum(x, [])
# x = [ int(elem) for elem in x]
# arr_size = max(x)+1

# diagram = np.zeros([arr_size, arr_size])
# for coord in coord_list:
#     y = int(coord[0])
#     x = int(coord[1])

#     diagram[x,y] = diagram[x,y] + 1


# print(diagram)
# print(np.count_nonzero(diagram > 1))


main_list = []
for elements in flat_list:
    main_list.append(("~").join(elements))
# print("main list:", main_list)

number_list = np.array(main_list)
# print('number list:', number_list)

(unique, counts) = np.unique(number_list, return_counts=True)

# print(np.asarray((unique,counts)).T)
frequencies = np.asarray((counts)).T
# print(frequencies)

ans = frequencies[frequencies >= 2]
print(len(ans))