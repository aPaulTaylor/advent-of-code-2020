import copy

with open('/aoc-2020/day17-input.txt', 'r') as f:
    input = f.readlines()

layers = []
for i in range(6):
    layers.append([[0] * 20] * 20)

central_layer = [[0] * 20] * 6
for input_line in input:
    central_layer.append([0] * 6 + [int(input_line[i] == '#') for i in range(8)] + [0] * 6)
central_layer.extend([[0] * 20] * 6)
layers.append(central_layer)

for i in range(6):
    layers.append([[0] * 20] * 20)


# Part 1
def iterate_volume(vol):
    newvol = []
    for i in range(len(vol)):
        inbs = [inb for inb in [i - 1, i, i + 1] if 0 <= inb < len(vol)]
        newlayer = []
        for j in range(len(vol[0])):
            jnbs = [jnb for jnb in [j - 1, j, j + 1] if 0 <= jnb < len(vol[0])]
            newrow = []
            for k in range(len(vol[0][0])):
                knbs = [knb for knb in [k - 1, k, k + 1] if 0 <= knb < len(vol[0][0])]
                nbs_sum = sum(sum(sum(vol[x][y][z] for z in knbs) for y in jnbs) for x in inbs)
                if (vol[i][j][k] == 0 and nbs_sum == 3) or (vol[i][j][k] == 1 and 3 <= nbs_sum <= 4):
                    newrow.append(1)
                else:
                    newrow.append(0)
            newlayer.append(newrow)
        newvol.append(newlayer)
    return newvol


def sum_vol(vol):
    return sum(sum(vol[x][y]) for y in range(len(vol[0])) for x in range(len(vol)))


iter_vol = copy.deepcopy(layers)
for i in range(6):
    iter_vol = iterate_volume(iter_vol)
print(sum_vol(iter_vol))

# Part 2
hypervol = [[[[0] * 20] * 20] * 13] * 6 + [layers] + [[[[0] * 20] * 20] * 13] * 6


def iterate_hypervolume(vol):
    newhvol = []
    for i in range(len(vol)):
        inbs = [inb for inb in [i - 1, i, i + 1] if 0 <= inb < len(vol)]
        newvol = []
        for j in range(len(vol[0])):
            jnbs = [jnb for jnb in [j - 1, j, j + 1] if 0 <= jnb < len(vol[0])]
            newlayer = []
            for k in range(len(vol[0][0])):
                knbs = [knb for knb in [k - 1, k, k + 1] if 0 <= knb < len(vol[0][0])]
                newrow = []
                for h in range(len(vol[0][0][0])):
                    hnbs = [hnb for hnb in [h - 1, h, h + 1] if 0 <= hnb < len(vol[0][0][0])]
                    nbs_sum = sum(
                        sum(sum(sum(vol[x][y][z][w] for w in hnbs) for z in knbs) for y in jnbs) for x in inbs)
                    if (vol[i][j][k][h] == 0 and nbs_sum == 3) or (vol[i][j][k][h] == 1 and 3 <= nbs_sum <= 4):
                        newrow.append(1)
                    else:
                        newrow.append(0)
                newlayer.append(newrow)
            newvol.append(newlayer)
        newhvol.append(newvol)
    return newhvol


def sum_hypervol(hvol):
    total = 0
    for cube in hvol:
        for lr in cube:
            for row in lr:
                total += sum(row)
    return total


iter_hvol = copy.deepcopy(hypervol)
for i in range(6):
    iter_hvol = iterate_hypervolume(iter_hvol)
print(sum_hypervol(iter_hvol))
