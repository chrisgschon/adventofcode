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
