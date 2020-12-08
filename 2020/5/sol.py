
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