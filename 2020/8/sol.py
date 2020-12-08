def day8_part1(inp):
    visited_index_before = False
    index = 0
    visited_index_set = set([])
    accumulator = 0
    while not visited_index_before:
        visited_index_set.add(index)
        item = inp[index].split(' ')
        operation, value = item[0], int(item[1])
        if operation == 'nop':
            index += 1
        elif operation == 'acc':
            accumulator += value
            index += 1
        elif operation == 'jmp':
            index += value
        if index in visited_index_set:
            visited_index_before = True
              
    return accumulator

def day8_part2_program_runner(inp):
    visited_index_before = False
    index = 0
    visited_index_set = set([])
    accumulator = 0
    max_index = len(inp)-1
    index_reached_end = False
    while not visited_index_before and not index_reached_end:
        visited_index_set.add(index)
        item = inp[index].split(' ')
        operation, value = item[0], int(item[1])
        if operation == 'nop':
            index += 1
        elif operation == 'acc':
            accumulator += value
            index += 1
        elif operation == 'jmp':
            index += value
        
        if index in visited_index_set:
            visited_index_before = True
            termination_type = 'infinite'
            #print('Terminated from infinite loop')
        if index > max_index:
            index_reached_end = True
            termination_type = 'normal'
            #print('Terminated normally')
              
    return termination_type, accumulator

def day8_part2(inp):
    for idx, i in enumerate(inp):
        input_copy = inp.copy()
        if (i.split(' ')[0] == 'jmp'):
            input_copy[idx] = i.replace('jmp', 'nop')
            termination_type, accumulator = day8_part2_program_runner(input_copy)
        elif (i.split(' ')[0] == 'nop'):
            input_copy[idx] = i.replace('nop', 'jmp')
            termination_type, accumulator = day8_part2_program_runner(input_copy)
        else:
            continue
        if termination_type == 'normal':
            return(idx, i, termination_type, accumulator)
            
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import utils

inp = utils.load_input_as_list(8)
part1_acc = day8_part1(inp)
print(f'Part 1 answer: {part1_acc}')
part2_ans = day8_part2(inp)
print(f'Part 2 answer: {part2_ans}')