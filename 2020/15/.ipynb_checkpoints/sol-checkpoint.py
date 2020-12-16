def parse(inp):
    mask_idxs = [i for i, val in enumerate(inp) if 'mask' in val]
    mask_idxs.append(len(inp))
    init_prog_list = []
    for i in range(0, len(mask_idxs)-1):
        mask_str = inp[mask_idxs[i]]
        mem_allocations = inp[mask_idxs[i]+1:mask_idxs[i+1]]
        mem_allocations_list = []
        for m in mem_allocations:
            alloc = m.replace('mem[', '').replace(']', '').split(' = ')
            mem_allocations_list.append((int(alloc[0]), int(alloc[1])))
        init_prog = {'mask': mask_str.split(' = ')[1], 'alloc': mem_allocations_list}
        init_prog_list.append(init_prog)
    return(init_prog_list)

def int_to_bit36(i):
    return("{0:b}".format(i).zfill(36))

def bit36_to_int(i):
    return(int(i, 2))

def program_resolver(value, mask):
    """pass bit value and mask, 
    return value"""
    out = value
    subs = [(i, int(x)) for i, x in enumerate(mask) if x!= 'X']
    for sub in subs:
        out = out[:sub[0]] + str(sub[1]) + out[(sub[0]+1):]
    return out

def day14_part1(inp):
    init_prog = parse(inp)
    mem_address_dict = {}
    for i in init_prog:
        mask = i['mask']
        for a in i['alloc']:
            value = int_to_bit36(a[1])
            new_value = program_resolver(value, mask)
            mem_address_dict[a[0]] = new_value
    mem_sum = sum([bit36_to_int(v) for _, v in mem_address_dict.items()])
    return mem_sum


def floating_value_generator(v):
    new_v=[]
    for s in v:
        x= s.find('X')
        if x==-1:
            pass
        s1 = s[:x] + '1' + s[x + 1:]
        s2 = s[:x] + '0' + s[x + 1:]
        new_v.append(s1)
        new_v.append(s2)
    #any left?
    lft=new_v[0].find('X')
    if lft!=-1:
        new_v=floating_value_generator(new_v)
    return new_v

def floating_program_resolver(value, mask):
    """pass bit value and mask, 
    return value"""
    s = ''
    for i in range(len(value)):
        if mask[i] == '0':
            s+=value[i]
        elif mask[i] == 'X':
            s+='X'
        elif mask[i] == '1':
            s+='1'
    
    multi_s=floating_value_generator([s])
    f=[]
    for x in multi_s:
        f.append([x, bit36_to_int(x)])
    return f


def day14_part2(inp):
    init_prog = parse(inp)
    mem_address_dict = {}
    for i in init_prog:
        mask = i['mask']
        for a in i['alloc']:
            value = int_to_bit36(a[0])
            new_values = floating_program_resolver(value, mask)
            for v in new_values:
                mem_address_dict[v[1]] = a[1]
    return(sum(mem_address_dict.values()))
            

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from utils import load_input_as_list 

inp = load_input_as_list('input_day14.txt')

print(f'Part one solution: {day14_part1(inp)}')
print(f'Part two solution: {day14_part2(inp)}')