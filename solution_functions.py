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