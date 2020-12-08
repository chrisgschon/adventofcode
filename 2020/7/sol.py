def day7_part1_dict_build(inp):
    bags_dict = {}
    for i in inp:
        key = i.split('bag')[0].strip()
        bags_dict[key] = {}
        contains = i.replace(key + ' bags contain', '')
        matches = re.findall('([\w\s]*?) bag', contains)
        for m in matches:
            ms = m.strip()
            if ms!= 'no other':
                bag = ms[2:]
                val = int(ms[0])
            else:
                continue
            bags_dict[key][bag] = val
    return(bags_dict)

def day7_bag_recurser(bags_dict, bag_colour):
    searched_dict = bags_dict[bag_colour]
    if searched_dict!={}:
        yield searched_dict
        for k, v in searched_dict.items():
            searched_dict = bags_dict[k]
            yield from day7_bag_recurser(bags_dict, k)
    

def day7_nested_bag_build(bags_dict):
    nested_bags_dict = {}
    for k, v in bags_dict.items():
        g = list(day7_bag_recurser(bags_dict, k))
        bag_nested = {}
        for i in g:
            for o, w in i.items():
                if o not in bag_nested.keys():
                    bag_nested[o] = w
                else:
                    bag_nested[o] += w
        nested_bags_dict[k] = bag_nested
    return(nested_bags_dict)

            

def day7_part1(inp):
    bags_dict = day7_part1_dict_build(inp)
    nested_bags_dict = day7_nested_bag_build(bags_dict)
    shiny_gold_count = 0
    for k, v in nested_bags_dict.items():
        if 'shiny gold' in v.keys():
            shiny_gold_count += 1
    return(shiny_gold_count)

def day7_part2_recurser(bags_dict, bag_colour, n=1):
    searched_dict = bags_dict[bag_colour]
    if searched_dict!={}:
        for k, v in searched_dict.items():
            yield n*v
            yield from day7_part2_recurser(bags_dict, k, n*v)

def day7_part2(inp):
    bags_dict = day7_part1_dict_build(inp)
    shiny_gold_recursive_dicts = list(day7_part2_recurser(bags_dict, 'shiny gold'))
    return(sum(shiny_gold_recursive_dicts))