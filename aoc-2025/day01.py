with open('c:/GitHub/advent-of-code-2020/aoc-2025/input/day00-input.txt', 'r') as f:
    rotations = [x.strip() for x in f.readlines()]

pos=50
zero_count_end=0
zero_count_mid=0

for r in rotations:
    prev_pos=pos
    mult = -1 if r[0]=='L' else 1
    pos += mult*int(r[1:])
    if pos>=100:
        zero_count_mid += pos//100
    if pos<=0:
        zero_count_mid += (100-pos)//100
        if prev_pos==0:
            zero_count_mid -= 1
    pos = pos % 100
    if pos==0:
        zero_count_end+=1


print(zero_count_end, zero_count_mid)




