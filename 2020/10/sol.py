from collections import Counter

def day10_part1(inp):
    l = [int(i) for i in inp]
    max_joltage = max(l) + 3
    sl = l.copy()
    sl.sort()
    sl.insert(len(sl), max_joltage)
    sl.insert(0, 0)
    cum_diff = [sl[i+1] - sl[i] for i in range(0,len(sl)-1)]
    diff_counters = Counter(cum_diff)
    ans = diff_counters[1]*diff_counters[3]
    return diff_counters, ans

def day10_part2(inp):
    l = [int(i) for i in inp]
    max_joltage = max(l) + 3
    sl = l.copy()
    sl.sort()
    sl.insert(len(sl), max_joltage)
    sl.insert(0, 0)
    cum_diff = [sl[i+1] - sl[i] for i in range(0,len(sl)-1)]
    consecs = ''.join([str(a) for a in cum_diff]).split('3')
    consecs_counts = Counter(consecs)
    ans = pow(7, consecs_counts['1111'])*pow(4, consecs_counts['111'])*pow(2, consecs_counts['11'])
    return consecs_counts, ans

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from utils import load_input_as_list



inp = load_input_as_list('10/input_day10.txt')

day10_part1(inp)

day10_part2(inp)