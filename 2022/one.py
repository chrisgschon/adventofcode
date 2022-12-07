from utils import load_input_as_list

input = load_input_as_list("inputs/one.txt")

elf_calories_dict = {}
elf_number = 1

for item in input:
    if item != '':
        if elf_calories_dict.get(elf_number) is None:
            elf_calories_dict[elf_number] = 0
        elf_calories_dict[elf_number] += int(item)
    else:
        elf_number += 1
        
key_max_calories_elf = sorted(elf_calories_dict, key=elf_calories_dict.get)[-1]
print(f'Day 1 part 1 answer: {elf_calories_dict[key_max_calories_elf]}')

key_max_calories_elfs = sorted(elf_calories_dict, key=elf_calories_dict.get)[-3:]
answer = sum([elf_calories_dict[key] for key in key_max_calories_elfs])
print(f'Day 1 part 2 answer: {answer}')
    