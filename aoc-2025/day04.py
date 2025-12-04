with open('c:/GitHub/advent-of-code-2020/aoc-2025/input/day04-input.txt', 'r') as f:
    map = [x.strip() for x in f.readlines()]

roll_locs_list=[]
roll_locs_set=set()

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]=='@':
            roll_locs_list.append((i,j))
            roll_locs_set.add((i,j))


rolls_removed=True
num_rolls=len(roll_locs_list)

while rolls_removed:
    accessible_rolls=[]
    rolls_removed=False
    for r in roll_locs_list:
        adj_rolls=0
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if (r[0]+dx,r[1]+dy) in roll_locs_set:
                    adj_rolls+=1
        if adj_rolls<5:
            accessible_rolls.append(r)
            rolls_removed=True
    print(len(accessible_rolls))
    for rr in accessible_rolls:
        roll_locs_list.remove(rr)
        roll_locs_set.discard(rr)

print(num_rolls-len(roll_locs_list))