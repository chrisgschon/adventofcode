from one import elf_calories_dict

key_max_calories_elfs = sorted(elf_calories_dict, key=elf_calories_dict.get)[-3:]
answer = sum([elf_calories_dict[key] for key in key_max_calories_elfs])
print(f'Day two answer: {answer}')