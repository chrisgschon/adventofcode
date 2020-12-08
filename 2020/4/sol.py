
def day4_preprocess(inp):
    l = [i+' ' if i!='' else '|' for i in inp]
    m = ''.join(l).split('|')
    return(m)

def day4_part1(inp):
    """check field existence for passport data
    example data:
    
    eyr:2029 iyr:2013
    hcl:#ceb3a1 byr:1939 ecl:blu
    hgt:163cm
    pid:660456119
    """
    
    m = day4_preprocess(inp)
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    valid_count = 0
    for details in m:
        detail_fields = set([i.split(':')[0] for i in details.split(' ')])
        if req_fields.issubset(detail_fields):
            valid_count+=1    
    return(valid_count)


def day4_part2(inp):
    """add data validation checks 
    to passport field checks"""
    
    m = day4_preprocess(inp)
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    valid_count = 0
    for details in m:
        details_dict = dict([(i.split(':')[0], i.split(':')[1]) for i in details.split(' ') if i != ''])
        detail_fields = set(details_dict.keys())
        #skip if passport doesnt have the right fields
        if not req_fields.issubset(detail_fields):
            continue
        #else check details
        else:
            test_byr = re.match('^(19[2-8][0-9]|199[0-9]|200[0-2])$', details_dict['byr']) is not None
            test_iyr = re.match('^(201[0-9]|2020)$', details_dict['iyr']) is not None
            test_eyr = re.match('^(202[0-9]|2030)$', details_dict['eyr']) is not None
            hgt_unit = 'in' if 'in' in details_dict['hgt'] else 'cm' if 'cm' in details_dict['hgt'] else False
            test_hgt = False
            if hgt_unit:
                if hgt_unit == 'in':
                    hgt_min = 59
                    hgt_max = 76
                elif hgt_unit == 'cm':
                    hgt_min = 150
                    hgt_max = 193
                test_hgt = int(details_dict['hgt'].replace(hgt_unit, '')) \
                >= hgt_min and int(details_dict['hgt'].replace(hgt_unit, '')) <= hgt_max
            test_hcl = re.match('^#([a-f]|[0-9]){6}$', details_dict['hcl']) is not None
            test_ecl = details_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            test_pid = re.match('^[0-9]{9}$', details_dict['pid']) is not None
        
        if test_byr and test_iyr and test_eyr and test_hgt and test_hcl and test_ecl and test_pid:
            valid_count+=1
            
    return(valid_count)