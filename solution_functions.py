"""Each main sovler function loads puzzle day (inp)
using load_input_as_list(inp), simply reading the txt
file line by line and loading into a list"""

from functools import reduce
import re
from collections import Counter

def load_input_as_list(day):
    with open(f"input_data/input_day{day}.txt", "r") as f:
        raw = f.readlines()
    inp = [i.replace('\n', '') for i in raw]
    return inp

def day1_part1(inp):
    """Given a list of expense items, return 
    the multiple of the two items that sum
    to 2020"""
    
    upper_triangle_sum = [((i,j), inp[i] + inp[j]) 
                          for i in range(len(inp)) 
                          for j in range(i, 200)]
    i, j = [i[0] for i in 
                             upper_triangle_sum 
                             if i[1] == 2020][0]
    multiple = inp[i]*inp[j]
    return multiple


def day1_part2(inp):
    """Given a list of expense items, return 
    the multiple of 3 items that sum
    to 2020"""
    
    upper_triangle_sum = [((i,j,k), inp[i] + inp[j] + inp[k]) 
                          for i in range(len(inp)) 
                          for j in range(i, 200)
                          for k in range(j, 200)]
    i, j, k = [i[0] for i in 
                             upper_triangle_sum 
                             if i[1] == 2020][0]
    multiple = inp[i]*inp[j]*inp[k]
    return multiple


def day2_part1_test_single(i):
    instance_range, letter, password = i.replace(':', '').split(' ')
    instance_range_lower, instance_range_upper = [int(i) for i in instance_range.split('-')]
    letter_instance_in_password = len([i for i in password if i == letter])
    passed = 1 if (letter_instance_in_password <= instance_range_upper
                  and letter_instance_in_password >= instance_range_lower) \
             else 0
    return passed


def day2_part1(input_day2):
    """Given a list of policies and
    passwords, return the number of valid
    passwords
    Example:
     '4-5 m: mmpth'
    means the password must have 4-5 'm's in,
    but it has 2, so it is not valid"""
    
    passed_list = [day2_part1_test_single(i) for i in input_day2]
    num_passed = sum(passed_list)
    return num_passed

def day2_part2_test_single(i):
    instance_indices, letter, password = i.replace(':', '').split(' ')
    instance_first, instance_second = [int(i) for i in instance_indices.split('-')]
    instance_first_pass = 1*(password[instance_first-1] == letter)
    instance_second_pass = 1*(password[instance_second-1] == letter)
    passed = 1*(instance_first_pass+instance_second_pass == 1)
    return passed

def day2_part2(input_day2):
    """Given a list of policies and
    passwords, return the number of valid
    passwords
    Example:
     '4-5 m: mmpth'
    means the password must have one m in either
    index 4 or 5 of the password. So it fails."""
    passed_list = [day2_part2_test_single(i) for i in input_day2]
    num_passed = sum(passed_list)
    return num_passed

def day3_part1(inp):
    """Given a list representing trees
    on a taboggan slope:
    ['....#...............##...#...#.'
    '#...#..#.....##.##.#.##....#...',
    '...#.....#...#.................'
    '#..#..#.......#...#.#..........']
    calculate the number of trees you
    would hit as you traverse 3 across
    and 1 down."""
    tree_count = 0
    width = len(inp[0])
    j = 0
    for i in range(len(inp)):
        if inp[i][j] == '#':
            tree_count += 1
        j+=3
        j = j % width
    return tree_count


def day3_part2_solver(inp, right, down):
    """generalise day3 part 1 for
    user defined traversal strategy
    down (steps down) and right (steps right)"""
    
    tree_count = 0
    width = len(inp[0])
    j = 0
    for i in range(0, len(inp), down):
        if inp[i][j] == '#':
            tree_count += 1
        j+=right
        j = j % width
    return tree_count


def day3_part2(inp):
    """main solver function for day 3 part,
    returning the product of tree counts
    of different traversal strategies"""
    
    tree_counts = []
    strats = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    for s in strats:
        tree_counts.append(day3_part2_solver(inp, s[0], s[1]))
    tree_counts_multiple = reduce((lambda x, y: x*y), tree_counts)
    return tree_counts_multiple


def day4_preprocess(inp):
    l = [i+' ' if i!='' else '|' for i in inp]
    m = ''.join(l).split('|')
    return(m)

def day4_part1(inp):
    """check field existence for passport data
    example data:
    
    eyr:2029 iyr:2013
    hcl:#ceb3a1 byr:1939 ecl:blu
    hgt:163cm
    pid:660456119
    """
    
    m = day4_preprocess(inp)
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    valid_count = 0
    for details in m:
        detail_fields = set([i.split(':')[0] for i in details.split(' ')])
        if req_fields.issubset(detail_fields):
            valid_count+=1    
    return(valid_count)


def day4_part2(inp):
    """add data validation checks 
    to passport field checks"""
    
    m = day4_preprocess(inp)
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    valid_count = 0
    for details in m:
        details_dict = dict([(i.split(':')[0], i.split(':')[1]) for i in details.split(' ') if i != ''])
        detail_fields = set(details_dict.keys())
        #skip if passport doesnt have the right fields
        if not req_fields.issubset(detail_fields):
            continue
        #else check details
        else:
            test_byr = re.match('^(19[2-8][0-9]|199[0-9]|200[0-2])$', details_dict['byr']) is not None
            test_iyr = re.match('^(201[0-9]|2020)$', details_dict['iyr']) is not None
            test_eyr = re.match('^(202[0-9]|2030)$', details_dict['eyr']) is not None
            hgt_unit = 'in' if 'in' in details_dict['hgt'] else 'cm' if 'cm' in details_dict['hgt'] else False
            test_hgt = False
            if hgt_unit:
                if hgt_unit == 'in':
                    hgt_min = 59
                    hgt_max = 76
                elif hgt_unit == 'cm':
                    hgt_min = 150
                    hgt_max = 193
                test_hgt = int(details_dict['hgt'].replace(hgt_unit, '')) \
                >= hgt_min and int(details_dict['hgt'].replace(hgt_unit, '')) <= hgt_max
            test_hcl = re.match('^#([a-f]|[0-9]){6}$', details_dict['hcl']) is not None
            test_ecl = details_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            test_pid = re.match('^[0-9]{9}$', details_dict['pid']) is not None
        
        if test_byr and test_iyr and test_eyr and test_hgt and test_hcl and test_ecl and test_pid:
            valid_count+=1
            
    return(valid_count)


def day5_getid(code):
    """binary search based on F/B L/R input"""
    
    row = sum([pow(2,6-i) if code[i] == 'B' else 0 for i in range(7)])
    col = sum([pow(2,2-i) if code[i+7] == 'R' else 0 for i in range(3)])
    return(row,col, row*8+col)
    

def day5_part1(inp):
    """get highest seat ID 
    from input"""
    idmax = 0
    for i in inp:
        row, col, seatid = day5_getid(i)
        if seatid > idmax:
            idmax = seatid
    return idmax


def day5_part2(inp):
    """find your seatid based on
    missing value"""
    
    idmax = 0
    idmin = 100
    seatid_range = [i*8 + j for i in range(128) for j in range(8)]
    for i in inp:
        row, col, seatid = day5_getid(i)
        if seatid > idmax:
            idmax = seatid
        if seatid < idmin:
            idmin = seatid
        seatid_range.remove(seatid)
    no_neighbours = [i for i in seatid_range if i > idmin and i < idmax]
    return(no_neighbours)


def day6_part1(inp):
    """return unique counts of groups of
    strings"""
    
    l = ''.join([i if i!='' else '|' for i in inp]).split('|')
    counts = [len(Counter(i)) for i in l]
    return(sum(counts))

def day6_part2(inp):
    """return intersect counts of groups 
    of strings"""
    
    #make list of lists
    l = [a.strip().split(' ') for a in ' '.join([i if i!='' else '|' for i in inp]).split('|')]
    
    #intersect of values for each list
    intersect_counts = [len(set.intersection(*[set(i) for i in j])) for j in l]
    
    return(sum(intersect_counts))



def day7_part1_dict_build(inp):
    bags_dict = {}
    for i in inp:
        key = i.split('bag')[0].strip()
        bags_dict[key] = {}
        contains = i.replace(key + ' bags contain', '')
        matches = re.findall('([\w\s]*?) bag', contains)
        for m in matches:
            ms = m.strip()
            if ms!= 'no other':
                bag = ms[2:]
                val = int(ms[0])
            else:
                continue
            bags_dict[key][bag] = val
    return(bags_dict)

def day7_bag_recurser(bags_dict, bag_colour):
    searched_dict = bags_dict[bag_colour]
    if searched_dict!={}:
        yield searched_dict
        for k, v in searched_dict.items():
            searched_dict = bags_dict[k]
            yield from day7_bag_recurser(bags_dict, k)
    

def day7_nested_bag_build(bags_dict):
    nested_bags_dict = {}
    for k, v in bags_dict.items():
        g = list(day7_bag_recurser(bags_dict, k))
        bag_nested = {}
        for i in g:
            for o, w in i.items():
                if o not in bag_nested.keys():
                    bag_nested[o] = w
                else:
                    bag_nested[o] += w
        nested_bags_dict[k] = bag_nested
    return(nested_bags_dict)

            

def day7_part1(inp):
    bags_dict = day7_part1_dict_build(inp)
    nested_bags_dict = day7_nested_bag_build(bags_dict)
    shiny_gold_count = 0
    for k, v in nested_bags_dict.items():
        if 'shiny gold' in v.keys():
            shiny_gold_count += 1
    return(shiny_gold_count)

def day7_part2_recurser(bags_dict, bag_colour, n=1):
    searched_dict = bags_dict[bag_colour]
    if searched_dict!={}:
        for k, v in searched_dict.items():
            yield n*v
            yield from day7_part2_recurser(bags_dict, k, n*v)

def day7_part2(inp):
    bags_dict = day7_part1_dict_build(inp)
    shiny_gold_recursive_dicts = list(day7_part2_recurser(bags_dict, 'shiny gold'))
    return(sum(shiny_gold_recursive_dicts))
