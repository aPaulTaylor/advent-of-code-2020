with open('input/day14-input.txt', 'r') as f:
    rocklines=[ [tuple(map(int,y.split(','))) for y in x.split(' -> ')] for x in f.readlines()]

def incl_range(a,b):
    return list(range(a,b+1)) if a<=b else range(b,a+1)

rock_coords=set()
for rl in rocklines:
    for i in range(len(rl)-1):
        for x in incl_range(rl[i][0],rl[i+1][0]):
            for y in incl_range(rl[i][1],rl[i+1][1]):
                rock_coords.add((x,y))

max_rock_y = max(r[1] for r in rock_coords)
sand_coords=set()

def drop_sand(sand_coords,rock_coords):
    sand_pos=(500,0)
    while not done:
        moved=False
        down=(sand_pos[0],sand_pos[1]+1)
        if down not in rock_coords and down not in sand_coords:
            sand_pos=down
            moved=True
        else:
            downleft=(sand_pos[0]-1,sand_pos[1]+1)
            if downleft not in rock_coords and downleft not in sand_coords:
                sand_pos=downleft
                moved=True
            else:
                downright=(sand_pos[0]+1,sand_pos[1]+1)
                if downright not in rock_coords and downright not in sand_coords:
                    sand_pos=downright
                    moved=True
        if not moved:
            return sand_pos, 'rest'
        else:
            if sand_pos[1]>max_rock_y:
                return sand_pos, 'abyss'

done=False
while not done:
    new_sand_pos, status = drop_sand(sand_coords,rock_coords)
    if status=='abyss':
        print(len(sand_coords))
        done=True
    else:
        sand_coords.add(new_sand_pos)
