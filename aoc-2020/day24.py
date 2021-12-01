import copy

with open('/aoc-2020/day24-input.txt', 'r') as f:
    paths = [x.strip() for x in f.readlines()]

dir_coord_changes = {
    'e':[0,2],
    'w':[0,-2],
    'ne':[1,1],
    'nw':[1,-1],
    'se':[-1,1],
    'sw':[-1,-1]
}

def path_to_coords(path):
    direction= ''
    coords=[0,0]
    for letter in path:
        direction += letter
        if direction[-1] in 'ew':
            # update coords according to dir
            coords = [x + y for x, y in zip(coords, dir_coord_changes[direction])]
            direction= ''
    return coords

black_coords=[]
for p in paths:
    c = path_to_coords(p)
    if c in black_coords:
        black_coords.remove(c)
    else:
        black_coords.append(c)

# Part 1
print(len(black_coords))
bc_nums = [x[0]*1000000 + x[1] for x in black_coords]
neighbour_diffs = [x[0]*1000000 + x[1] for x in dir_coord_changes.values()]

for i in range(100):
    print(f'After day {i}:')
    print(len(bc_nums))
    black_neighbour_coords = {}
    for c in bc_nums:
        for nd in neighbour_diffs:
            nb_c = c+nd
            if nb_c in black_neighbour_coords:
                black_neighbour_coords[nb_c] +=1
            else:
                black_neighbour_coords[nb_c]=1
    new_black_coords = [ c for c in bc_nums if c in black_neighbour_coords.keys() and black_neighbour_coords[c] < 3]
    for c in black_neighbour_coords.keys():
        if (c not in bc_nums) and black_neighbour_coords[c] == 2:
            new_black_coords.append(c)
    bc_nums = new_black_coords[:]

print(len(bc_nums))