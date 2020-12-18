import re

with open('c:/Users/paula/PycharmProjects/advent-of-code/day18-input.txt', 'r') as f:
    sums = [x.strip() for x in  f.readlines()]

operators = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

def parse_sum(sum_str,main_op):
    parenth = re.compile('\\([0-9\\s\\+\\*]*\\)')
    plus_re = re.compile('[0-9]+\\s\\+\\s[0-9]+')
    times_re = re.compile('[0-9]+\\s\\*\\s[0-9]+')
    sum_parenths = parenth.findall(sum_str)
    if all(x in '1234567890' for x in sum_str):
        return sum_str
    elif len(sum_parenths)>0:
        return parse_sum(sum_str.replace(sum_parenths[0],parse_sum(sum_parenths[0][1:-1],main_op)),main_op)
    else:
        if main_op == '+':
            ops = plus_re.findall(sum_str) + times_re.findall(sum_str)
        else:
            ops = [' '.join(sum_str.split(' ')[0:3])]
        op_split=ops[0].split(' ')
        op_res = str(operators[op_split[1]](int(op_split[0]),int(op_split[2])))
        return parse_sum(sum_str.replace(ops[0],op_res,1),main_op)

print(sum([int(parse_sum(sum,'')) for sum in sums]))
print(sum([int(parse_sum(sum,'+')) for sum in sums]))