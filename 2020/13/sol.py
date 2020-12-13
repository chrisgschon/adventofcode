from functools import reduce

def day13_part1(inp):
    now = int(inp[0])
    ids = [int(i) for i in inp[1].split(',') if i != 'x']
    wait_times = dict([(i, i - (now % i)) for i in ids])
    min_wait_id = min(wait_times, key=wait_times.get)
    min_wait_time = wait_times[min_wait_id]
    return min_wait_id*min_wait_time


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def day13_part2(inp):
    ids = [int(i)if i != 'x' else i for i in inp[1].split(',') ]
    remainders = [(int(j),(int(j)-i) % j) for i, j in enumerate(ids) if j != 'x']
    val = chinese_remainder([r[0] for r in remainders], [r[1] for r in remainders])
    return(val)
        
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from utils import load_input_as_list 

inp = load_input_as_list('input_day13.txt')

print(f'Part one solution: {day13_part1(inp)}')
print(f'Part two solution: {day13_part2(inp)}')