import math

with open('c:/GitHub/advent-of-code-2020/aoc-2025/input/day06-input.txt', 'r') as f:
    hwk_in = [x[:-1] for x in f.readlines()]

hwk = [h.split() for h in hwk_in]
hwk_total=0
for i in range(len(hwk[0])):
    if hwk[-1][i] == '+':
        sol=0
        for j in range(len(hwk)-1):
            sol+=int(hwk[j][i])
    else:
        sol=1
        for j in range(len(hwk)-1):
            sol*=int(hwk[j][i])
    hwk_total += sol

print(hwk_total)

hwk_total=0

curr_col = len(hwk_in[0])-1
curr_prob_nums=[]
while curr_col >= 0:
    col_num = int(''.join(
        [x[curr_col] for x in hwk_in if x[curr_col] not in '*+ ']
        ))
    curr_prob_nums.append(col_num)
    if hwk_in[-1][curr_col] == '+':
        hwk_total += sum(curr_prob_nums)
        curr_prob_nums=[]
        curr_col += -1
    elif hwk_in[-1][curr_col] == '*':
        hwk_total += math.prod(curr_prob_nums)
        curr_prob_nums=[]
        curr_col += -1
    curr_col += -1

print(hwk_total)