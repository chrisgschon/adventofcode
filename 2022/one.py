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
print(f'Day one answer: {elf_calories_dict[key_max_calories_elf]}')
    