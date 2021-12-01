with open('/aoc-2020/day4-input.txt', 'r') as f:
    puzzle_input = f.readlines()

puzzle_input.append('\n')

passports=[]
cur_passport=""
for input_line in puzzle_input:
    if input_line == '\n':
        passports.append(cur_passport)
        cur_passport=''
    else:
        cur_passport = cur_passport + ' ' + input_line

passports = [x.split() for x in passports]
passport_dicts = [dict([x.split(':') for x in pp]) for pp in passports]

necessary_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #not 'cid'

def is_valid_passport(pp, nk=necessary_keys):
    return all([k in pp.keys() for k in nk])

print('{} valid passports'.format(sum(is_valid_passport(pp) for pp in passport_dicts)))

valid_pps = [x for x in passport_dicts if is_valid_passport(x)]

valid_values = {
    'byr':[str(n) for n in range(1920,2003)],
    'iyr':[str(n) for n in range(2010,2021)],
    'eyr':[str(n) for n in range(2020,2031)],
    'hgt':[str(n)+'cm' for n in range(150,194)]+[str(n)+'in' for n in range(59,77)],
    'ecl':['amb','blu','brn','gry','grn','hzl','oth']
}

def has_valid_values(pp,vv=valid_values):
    main_valid = all(pp[i] in vv[i] for i in vv.keys())
    # manual checks for pid and hcl
    pid_valid = len(pp['pid']) == 9 and all(n in ['0','1','2','3','4','5','6','7','8','9'] for n in pp['pid'])
    hcl_valid = len(pp['hcl']) == 7 and pp['hcl'][0]=='#' and all(n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a','b','c','d','e','f'] for n in pp['hcl'][1:])
    return main_valid and pid_valid and hcl_valid

print("{} valid passports with valid values".format(sum(has_valid_values(pp) for pp in valid_pps)))

