from functools import reduce

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
    instance_range_lower, instance_range_upper = [int(i) for i in                                                                   instance_range.split('-')]
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