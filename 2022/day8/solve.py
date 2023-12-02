# --- Day 8: Treetop Tree House ---

import numpy as np
import os
import sys

with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]

trees = [list(x) for x in scan]
trees = np.array(trees)
dim = np.shape(trees)
visibility = np.zeros(dim)




# find visibilities of inner tree
def find_visibility(arr, dims):

    # set visibility of edge
    visibility[0] = np.full(dims[0], 1)
    visibility[dims[0]-1] = np.full(dims[0], 1)
    visibility[:, dims[0]-1] = np.full(dims[0], 1)
    visibility[:, 0] = np.full(dims[0], 1)

    scores_list = []
    for idx, x in np.ndenumerate(arr):
        if(0 not in idx and dims[0]-1 not in idx):
            # check to see if it is visible
            #left
            left  = arr[idx[0],0:idx[1] ]
            left_max = max(left)
            if( x > left_max):
                left_score = len(left)
            else:
                ll = left.tolist()
                if(len(left) > 1):
                    ll.reverse()
                 
                left_score = [n >= x for n in ll]
                left_score = left_score.index(True) + 1
            
        

            #right
            right = arr[idx[0],idx[1]+1: ]
            right_max = max(right)
            if( right_max < x ):
                right_score = len(right)
            else:
                rr = right.tolist()
                right_score =[n >= x for n in rr]
                right_score = right_score.index(True) +1

            #top
            top = arr[0:idx[0],idx[1] ]
            top_max = max(top)
            if( x > top_max):
                top_score = len(top)
            else:
                tt = top.tolist()
                if(len(top) > 1):
                    tt.reverse()
                top_score = [n >= x for n in tt]
                top_score = top_score.index(True) +1
            
            #bottom
            bottom = arr[idx[0]+1:,idx[1] ]
            bottom_max = max(bottom)
            if(x > bottom_max):
                bottom_score = len(bottom)
            else:
                bb = bottom.tolist()
                bottom_score =[n >= x for n in bb]
                bottom_score = bottom_score.index(True) +1

            maxes = [left_max,right_max,top_max,bottom_max]
            scores = [left_score, right_score,top_score, bottom_score]
            scores = [ s for s in scores if s > 0]
            is_visible = any([ x > m for m in maxes])

            if(is_visible):
                visibility[idx] = 1

            scores_list.append(np.prod(scores))


  
    print("viz")
    print(np.sum(visibility))
    print("score")
    print(max(scores_list))




find_visibility(trees, dim)