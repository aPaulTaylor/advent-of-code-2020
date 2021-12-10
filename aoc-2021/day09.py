with open('input/day09-input.txt', 'r') as f:
    hmap = [[int(n) for n in x[:-1]] for x in f.readlines()]

hmap_padded = [[9] * 102]
for l in hmap:
    hmap_padded.append([9] + l + [9])
hmap_padded.append([9] * 102)

total_risk_level = 0
low_points = []
for i in range(1, 101):
    for j in range(1, 101):
        if min(hmap_padded[i - 1][j], hmap_padded[i + 1][j], hmap_padded[i][j - 1], hmap_padded[i][j + 1]) > \
                hmap_padded[i][j]:
            total_risk_level += hmap_padded[i][j] + 1
            low_points.append([i, j])
print(total_risk_level)

def get_basin_size(hmap_padded, lp):
    basin = {(lp[0], lp[1])}
    point_added = True
    while point_added:
        new_points = set()
        for pt in basin:
            for nb in [[1,0], [-1,0],[0, 1], [0, -1]]:
                if hmap_padded[pt[0] + nb[0]][pt[1] + nb[1]] < 9 and hmap_padded[pt[0] + nb[0]][pt[1] + nb[1]] >= hmap_padded[pt[0]][pt[1]]:
                    new_points.add((pt[0] + nb[0], pt[1] + nb[1]))
        old_len = len(basin)
        basin = basin.union(new_points)
        point_added = len(basin) > old_len
    return len(basin)

basin_sizes = [get_basin_size(hmap_padded, lp) for lp in low_points]
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
