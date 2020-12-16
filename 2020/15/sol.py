def parse(inp):
    return [int(i) for i in inp[0].split(',')]

def play_game(l, length):
    lastnum = l[-1]
    seen = [0] * length
    i = 0
    while i < len(l):
        seen[l[i-1]] = i
        i+=1
    while i < length:
        said = seen[lastnum]
        seen[lastnum] = i
        lastnum = 0 if said == 0 else i-said
        i+=1
    return(lastnum)

def day15_part1(inp):
    l = parse(inp)
    return play_game(l, 2020)


def day15_part2(inp):
    l = parse(inp)
    return play_game(l, 30000000)

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from utils import load_input_as_list 

inp = load_input_as_list('input_day15.txt')

print(f'Part one solution: {day15_part1(inp)}')
print(f'Part two solution: {day15_part2(inp)}')