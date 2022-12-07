from utils import load_input_as_list
input = load_input_as_list("inputs/three.txt")

from string import ascii_lowercase, ascii_uppercase
priority_score_map = {i: n+1 for n, i in enumerate(ascii_lowercase + ascii_uppercase)}

# Part one
rucksacks_split = [(i[:(len(i)//2)], i[(len(i)//2):]) for i in input]
rucksacks_dupe_items = []
for r in rucksacks_split:
    continue_search = True
    for char in r[0]:
        if continue_search:
            if char in r[1]:
                rucksacks_dupe_items.append(char)
                continue_search = False
                break
rucksack_scores = [priority_score_map[i] for i in rucksacks_dupe_items]
print(f'Day 3 part 1 answer: {sum(rucksack_scores)}')

# Part two
rucksacks = input
group_shared_items = [list(set(a).intersection(set(b)).intersection(set(c)))[0] for (a,b,c) in [tuple(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)]]
sum_of_shared_items = [priority_score_map[i] for i in group_shared_items]
print(f'Day 3 part 2 answer: {sum(sum_of_shared_items)}')




                

            
            
            
            

# rucksacks_dupe_items = [j for i in rucksacks for j in i[0] if j in i[1]]

# print(set(rucksacks_dupe_items))



