def update_seating(inp):
    seat_array = np.array([[char for char in i] for i in inp])
    num_rows, num_cols = seat_array.shape
    out = inp.copy()
    for i, row in enumerate(seat_array):
        for j, seat in enumerate(row):
            adrows = [max(0, i-1), min(num_rows-1, i+1)]
            adcols = [max(0, j-1), min(num_cols-1, j+1)]
            ad_occupied = [seat_array[i,j] == '#' for i in range(adrows[0], adrows[1]+1) for j in range(adcols[0], adcols[1]+1)]
            if seat == 'L':
                if not any(ad_occupied):
                    out[i] = out[i][:j] + '#' + out[i][j+1:]
            elif seat == '#':
                if sum(ad_occupied) >= 5:
                    out[i] = out[i][:j] + 'L' + out[i][j+1:]
    return(out)

def day11_part1(inp):
    previous_arrangement = inp.copy()
    arrangement = update_seating(inp)
    while arrangement != previous_arrangement:
        previous_arrangement = arrangement.copy()
        arrangement = update_seating(arrangement)
    num_occupied = sum([i.count('#') for i in arrangement])
    return arrangement, num_occupied


import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from utils import load_input_as_list


