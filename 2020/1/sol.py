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