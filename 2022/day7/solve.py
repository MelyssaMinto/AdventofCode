# --- Day 7: No Space Left On Device ---
import os
import sys
import string
# reading in input

with open(os.path.join(sys.path[0],"test.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]

# print(scan)
dirs = [cmd for cmd in scan if "$ cd" in cmd or "dir" in cmd]
print(dirs)

ind_cd =  [index for index, elem in enumerate(scan) if "$ cd" in elem]
ind_dir =  [index for index, elem in enumerate(scan) if "dir " in elem]
print(ind_cd)
paths = []
for i in ind_cd:
    parent = scan[i].replace("$ cd ", "")
    print(parent)
    for j in ind_dir:
        if( j < ind_cd[i+1]):
            child = scan[j].replace("dir ", "")
            print(child)
            paths.append(''.join( [parent, child]))
        else:
            break


print(paths)

def get_files_in_dir(input):
    # get the indices of ls commands in order to extract the contents of each dir
    ls_start =  [index for index, elem in enumerate(input) if elem == "$ ls"]
    ls_end = ls_start + [len(input)+1]
    ls_end = ls_end[1:]

    dirs = []
    contains = []
    # loop through ls indices to extract contents 
    for (start,end) in zip(ls_start,ls_end):
        s = start+1
        e = end-1
        # extract the dir ls is being ran on
        dir = input[start -1]
        dir = dir.replace("$ cd ", "")
        # get the files listed before the next ls commnand
        files = input[s:e]
        # > extract dir name
        files = [f.replace("dir ", "") for f in files]
        # > extract file size 
        files = [f.split(' ')[0] for f in files]
        # > remove the cd command before the next ls that is captured
        files = [f for f in files if f != "$"]

        # add dir to a running list of dirs
        dirs = dirs + [dir]
        # and list of contents to a running list of contents
        contains= contains + [files]
    # return the list of dirs and the list of contents per dir
    return(dirs, contains)

def get_sums(dirs, contains):
    # figure out which dirs can be summed up (i.e. does not have subdirs )
    can_sum = [[x.isdigit() for x in l] for l in contains]
    can_sum = [all(x) for x in can_sum]
    # create a dict to hold the total for each dir 
    dir_sums = dict()

    # loop through and calculate sums until all are calculated
    all_summable = False
    while all_summable == False:
        #loop throguh all the dirs 
        for i in range(len(can_sum)):
            # for the ones that can be summed, sum them
            if(can_sum[i]):
                sizes = [int(x) for x in contains[i]]
                # add totals to sub dirs
                dir_sums[dirs[i]] = str(sum(sizes))
        # update list of contents for newly summed dirs by replacing the dir with the sum of its contents
        contains = [[dir_sums[item] if str(item).isdigit() == False and item in dir_sums.keys() else item for item in l] for l in contains]
        # figure out conents are still dirs (i.e. ones that did not get summed yet)
        is_dir = [[str(x).isdigit() for x in l] for l in contains]
        # determine which dirs are summable
        all_summable = all([all(x) for x in is_dir])
        # determine if all dirs are summable, if so then we can end the loop
        can_sum = [all(x) for x in is_dir]
    # return the dictionary of sums and the lists of sums for contents
    return(dir_sums, contains)

def sum_atmost(s, limit):
    # sum the dirs whose sums are less than the limit
    print(sum([int(x) for x in s.values()  if int(x) <= limit]))
    



# d,c = get_files_in_dir(scan)
# dict_tree = dict(zip(d,c))
# print("tree: ")
# [print(key,':',value) for key, value in dict_tree.items()]


# sums, c_update = get_sums(d,c)
# dict_tree_sums = dict(zip(d,c_update))
# print("tree sums: ")
# # [print(key,':',value) for key, value in dict_tree_sums.items()]

# print("dir sums: ")
# # [print(key,':',value) for key, value in sums.items()]

# print("Part 1:")
# sum_atmost(sums, 100000)

# # print("tree: ")
# # print(dict_tree['rzb'])
# # print("sums: ")
# # print(dict_tree_sums['rzb'])


# # print([len(x) for x in dict_tree_sums.values()] == [len(x) for x in dict_tree.values()])
# print(len(dict_tree.keys()))