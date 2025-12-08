with open('c:/GitHub/advent-of-code-2020/aoc-2025/input/day07-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

beam_poses = [i for i in range(len(input[0])) if input[0][i]=='S']
splits=0

for row in input[1:]:
    new_beam_poses=[]
    for bp in beam_poses:
        if row[bp]=='^':
            splits+=1
            for spl in [-1,1]:
                if bp+spl not in new_beam_poses:
                    new_beam_poses.append(bp+spl)
        else:
            if bp not in new_beam_poses:
                new_beam_poses.append(bp)
    beam_poses=new_beam_poses

print(splits)

beam_poses_counts = []
for x in input[0]:
    if x=='S':
        beam_poses_counts.append(1)
    else:
        beam_poses_counts.append(0)

for row in input[1:]:
    new_beam_poses_counts=[0 for i in range(len(row))]
    for i in range(len(row)):
        if row[i]=='^':
            new_beam_poses_counts[i-1]+=beam_poses_counts[i]
            new_beam_poses_counts[i+1]+=beam_poses_counts[i]
        else:
            new_beam_poses_counts[i]+=beam_poses_counts[i]
    beam_poses_counts=new_beam_poses_counts

print(sum(new_beam_poses_counts))