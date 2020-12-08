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