import re

with open('c:/Users/paula/PycharmProjects/advent-of-code/day18-input.txt', 'r') as f:
    sums = [x.strip() for x in  f.readlines()]

operators = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

def parse_sum(sum_str):
    parenth = re.compile('\\([0-9\\s\\+\\*]*\\)')
    sum_parenths = parenth.findall(sum_str)
    if all(x in '1234567890' for x in sum_str):
        return sum_str
    elif len(sum_parenths)>0:
        return parse_sum(sum_str.replace(sum_parenths[0],parse_sum(sum_parenths[0][1:-1])))
    else:
        sum_seq = sum_str.split(' ')
        first_op_res = str(operators[sum_seq[1]](int(sum_seq[0]),int(sum_seq[2])))
        return parse_sum(' '.join([first_op_res] + sum_seq[3:]))

print(sum([int(parse_sum(sum)) for sum in sums]))

def parse_sum2(sum_str):
    parenth = re.compile('\\([0-9\\s\\+\\*]*\\)')
    addition = re.compile('[0-9]*\\s\+\\s[0-9]*')
    sum_parenths = parenth.findall(sum_str)
    sum_adds = addition.findall(sum_str)
    if all(x in '1234567890' for x in sum_str):
        return sum_str
    elif len(sum_parenths)>0:
        return parse_sum2(sum_str.replace(sum_parenths[0],parse_sum2(sum_parenths[0][1:-1])))
    elif len(sum_adds)>0:
        add_split = sum_adds[0].split(' ')
        subtotal = str(int(add_split[0])+int(add_split[2]))
        return parse_sum2(sum_str.replace(sum_adds[0], subtotal, 1))
    else:
        sum_seq = sum_str.split(' ')
        first_op_res = str(int(sum_seq[0])*int(sum_seq[2]))
        return parse_sum2(' '.join([first_op_res] + sum_seq[3:]))

print(sum([int(parse_sum2(sum)) for sum in sums]))