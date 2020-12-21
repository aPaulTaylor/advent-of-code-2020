with open('c:/Users/paula/PycharmProjects/advent-of-code/day20-input.txt', 'r') as f:
    input = f.read()

tilesraw = [x.split('\n') for x in input.split('\n\n')][:-1]
tilesraw = [{'id': int(t[0][5:9]), 'tile': t[1:]} for t in tilesraw]
for t in tilesraw:
    t['edges'] = [t['tile'][0],
                  t['tile'][9],
                  ''.join([row[0] for row in t['tile']]),
                  ''.join([row[9] for row in t['tile']])
                  ]
tiles = []
for t in tilesraw:
    perimeter = t['edges'][0] + t['edges'][3] + t['edges'][1][::-1] + t['edges'][2][::-1]
    perim_rev = perimeter[::-1]
    orient_edges = [
        [perimeter[0:10], perimeter[10:20], perimeter[20:30][::-1], perimeter[30:40][::-1]],
        [perimeter[10:20], perimeter[20:30], perimeter[30:40][::-1], perimeter[0:10][::-1]],
        [perimeter[20:30], perimeter[30:40], perimeter[0:10][::-1], perimeter[10:20][::-1]],
        [perimeter[30:40], perimeter[0:10], perimeter[10:20][::-1], perimeter[20:30][::-1]],
        [perim_rev[0:10], perim_rev[10:20], perim_rev[20:30][::-1], perim_rev[30:40][::-1]],
        [perim_rev[10:20], perim_rev[20:30], perim_rev[30:40][::-1], perim_rev[0:10][::-1]],
        [perim_rev[20:30], perim_rev[30:40], perim_rev[0:10][::-1], perim_rev[10:20][::-1]],
        [perim_rev[30:40], perim_rev[0:10], perim_rev[10:20][::-1], perim_rev[20:30][::-1]]
    ]
    tiles.append(orient_edges)

grid_tiles = []
grid_tile_orients = []


def does_tile_fit(tile, orient, pos, grid_tiles, grid_tile_orients):
    if pos > 11:
        if tile[orient][0] != tiles[grid_tiles[pos - 12]][grid_tile_orients[pos - 12]][2]:
            return False
    if not pos % 12 == 0:
        if tile[orient][3] != tiles[grid_tiles[pos - 1]][grid_tile_orients[pos - 1]][1]:
            return False
    return True


next_tile = 55 # set to 0 to run from start; use 55 as a shortcut
next_tile_orient = -1
max_found=0
while len(grid_tiles) < 144:
    # get next tile
    if next_tile_orient == 7:
        next_tile_orient = 0
        next_tile += 1
    else:
        next_tile_orient += 1
    while next_tile in grid_tiles:
        next_tile_orient = 0
        next_tile += 1
    if next_tile == 144:
        next_tile = grid_tiles.pop()
        next_tile_orient = grid_tile_orients.pop()
    else:
        print([tilesraw[i]['id'] for i in grid_tiles])
        print(grid_tile_orients)
        print(max_found)
        next_tile_fits = does_tile_fit(tiles[next_tile], next_tile_orient, len(grid_tiles), grid_tiles, grid_tile_orients)
        if next_tile_fits:
            grid_tiles.append(next_tile)
            grid_tile_orients.append(next_tile_orient)
            if len(grid_tiles)> max_found:
                max_found = len(grid_tiles)
            next_tile = 0
            next_tile_orient = -1

print(tilesraw[grid_tiles[0]]['id']*tilesraw[grid_tiles[11]]['id']*tilesraw[grid_tiles[132]]['id']*tilesraw[grid_tiles[143]]['id'])