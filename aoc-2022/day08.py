with open('input/day08-input.txt', 'r') as f:
    forest = [[int(t) for t in x.strip()] for x in f.readlines()]

visibilities=[[False for t in forest[0]] for row in forest]

for row_num in range(len(forest)):
    row=forest[row_num]
    for i in range(len(row)):
        if row[i] > min(max([-1]+row[:i]),max([-1]+row[(i+1):])):
            visibilities[row_num][i]=True

for col_num in range(len(forest[0])):
    col=[r[col_num] for r in forest]
    for i in range(len(col)):
        if col[i] > min(max([-1]+col[:i]),max([-1]+col[(i+1):])):
            visibilities[i][col_num]=True

print(sum(sum(v for v in vrow) for vrow in visibilities))

def get_scenic_score(forest, row_num, col_num):
    col=[r[col_num] for r in forest]
    tree=forest[row_num][col_num]
    sightlines=[
        forest[row_num][:col_num][::-1],
        forest[row_num][(col_num+1):],
        col[:row_num][::-1],
        col[(row_num + 1):]
    ]
    score=1
    for sl in sightlines:
        trees_seen=0
        for t in sl:
            trees_seen+=1
            if t>=tree:
                break
        score*=trees_seen
    return score

print(max(max(get_scenic_score(forest,rn,cn) for rn in range(len(forest))) for cn in range(len(forest[0]))))

