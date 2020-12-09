from itertools import combinations 

def day9_part1(inp, preamble_length):
    l = [int(i) for i in inp]
    check_l = l.copy()
    for idx, i in enumerate(l):
        if idx < preamble_length:
            continue
        numbers_to_sum_from = check_l[(idx-preamble_length):idx]
        c = combinations(numbers_to_sum_from, 2)
        okay = True if i in [a[0] + a[1] for a in c] else False
        if not okay:
            return i
        
        
def day9_part2(inp, preamble_length):
    l = [int(i) for i in inp]
    check_l = l.copy()
    for idx, i in enumerate(l):
        if idx < preamble_length:
            continue
        numbers_to_sum_from = check_l[(idx-preamble_length):idx]
        c = combinations(numbers_to_sum_from, 2)
        okay = True if i in [a[0] + a[1] for a in c] else False
        if not okay:
            not_okay_idx = idx
            not_okay_value = l[idx]
            break
    
    continguous_list_range = [0,not_okay_idx-1]
    check_l = l[0:not_okay_idx-1].copy()
    for i in range(not_okay_idx):
        for d in range(2, not_okay_idx):
            continguous_sum = sum(check_l[i:d])
            if continguous_sum == not_okay_value:
                print(f'Start: {i}, End: {d},\n\nContinguous list: {check_l[i:d]}\n\n')
                min_c_l = min(check_l[i:d])
                max_c_l = max(check_l[i:d])
                print(f'Answer is: {min_c_l} + {max_c_l} = {min_c_l + max_c_l}')

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from utils import load_input_as_list

inp = load_input_as_list('9/input_day9.txt')

day9_part1(inp, 25)

day9_part2(inp, 25)
