with open('c:/Users/paula/PycharmProjects/advent-of-code/day11-input.txt', 'r') as f:
    seatmap = [x.strip() for x in f.readlines()]


def count_neighbours(seatmap, x, y):
    rows = seatmap[max(0, y - 1):min(len(seatmap), y + 2)]
    nbhd = [r[max(0, x - 1):min(len(seatmap[0]), x + 2)] for r in rows]
    empty = sum(sum(s == 'L' for s in nbd_row) for nbd_row in nbhd) - (seatmap[y][x] == 'L')
    occupied = sum(sum(s == '#' for s in nbd_row) for nbd_row in nbhd) - (seatmap[y][x] == '#')
    return [empty, occupied]


def iterate_seatmap(seatmap, cnfunc, vacate_limit):
    newmap = []
    for y, row in enumerate(seatmap):
        newrow = ''
        for x, s in enumerate(row):
            cn = cnfunc(seatmap, x, y)
            if s == 'L':
                if cn[1] == 0:
                    newrow += '#'
                else:
                    newrow += 'L'
            elif s == '#':
                if cn[1] >= vacate_limit:
                    newrow += 'L'
                else:
                    newrow += '#'
            else:
                newrow += '.'
        newmap.append(newrow)
    return newmap


def compare_maps(map1, map2):
    return all(map1[i] == map2[i] for i in range(len(map1)))


newmap= iterate_seatmap(seatmap,count_neighbours,4)
while not compare_maps(seatmap,newmap):
    newnewmap = iterate_seatmap(newmap,count_neighbours,4)
    seatmap = newmap
    newmap = newnewmap
print(sum(sum(s=='#' for s in row) for row in newmap))

def count_visible(seatmap, x, y):
    visible_occupied = 0
    for ac_inc in [0,-1,1]:
        for dn_inc in [0,-1,1]:
            if not(ac_inc==0 and dn_inc==0):
                i = x + ac_inc
                j = y + dn_inc
                seat_seen = False
                while (0<=i<len(seatmap[0]) and 0<=j<len(seatmap) and not seat_seen):
                    if seatmap[j][i] == '#':
                        visible_occupied += 1
                        seat_seen = True
                    if seatmap[j][i] == 'L':
                        seat_seen = True
                    i += ac_inc
                    j += dn_inc
    return [0, visible_occupied]


with open('c:/Users/paula/PycharmProjects/advent-of-code/day11-input.txt', 'r') as f:
    seatmap = [x.strip() for x in f.readlines()]

newmap = iterate_seatmap(seatmap, count_visible, 5)
while not compare_maps(seatmap, newmap):
    newnewmap = iterate_seatmap(newmap, count_visible, 5)
    seatmap = newmap
    newmap = newnewmap

print(sum(sum(s == '#' for s in row) for row in newmap))
