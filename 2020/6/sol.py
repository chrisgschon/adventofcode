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