# --- Day 2: Cube Conundrum ---
import os
import sys
import re

# actual input
with open(os.path.join(sys.path[0],"input.txt"), "r") as file:
    scan = file.readlines()
    scan = [line.rstrip('\n') for line in scan]
    scan = [line.split(': ')[1] for line in scan]
    scan = [line.split('; ') for line in scan]


def parse_games(s):
    sums = []
    maxes = []
    for line in s:
        # wrangle and flaten list
        p = [x.split(' ') for x in line]
        p = [x.split(', ') for x in line]
        flat_p = [item for sublist in p for item in sublist]

        # get the maxes
        rgb = dict.fromkeys(['red', 'green', 'blue'])
        for key in rgb.keys():
            pattern ='\d+ ' + key
            res = [re.findall('\d+', x) for x in flat_p if re.findall(pattern, x)]
            res = [int(item) for sublist in res for item in sublist]
            rgb[key] = max(res)
        maxes.append(rgb)
    return(maxes)

def find_games(d, r,g,b):
    game_ids = []
    ids = [*range(1,len(d)+1)]
    for game, id in zip(d, ids):
        
        # print(game)
        if(game['red'] <= r and game['green'] <= g and game['blue'] <= b):
            game_ids.append(id)
            #print("game in! ==>" + str(id))

    return(game_ids)
        

def find_power(d):
    prods = []
    for game in d:
        prod = 1
        for vals in game.values():
            prod = vals*prod
        prods.append(prod)
    # print(prods)
    print(sum(prods))


print("part 1")
rgb_dict = parse_games(scan)
possibles = find_games(rgb_dict, 12, 13, 14)
print(sum(possibles))

print("part 2")
find_power(rgb_dict)

