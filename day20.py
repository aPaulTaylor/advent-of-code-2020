import copy

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

def does_tile_fit(tile, orient, pos, grid_tiles, grid_tile_orients):
    if pos > 11:
        if tile[orient][0] != tiles[grid_tiles[pos - 12]][grid_tile_orients[pos - 12]][2]:
            return False
    if not pos % 12 == 0:
        if tile[orient][3] != tiles[grid_tiles[pos - 1]][grid_tile_orients[pos - 1]][1]:
            return False
    return True

grid_tiles = []
grid_tile_orients = []
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
        next_tile_fits = does_tile_fit(tiles[next_tile], next_tile_orient, len(grid_tiles), grid_tiles, grid_tile_orients)
        if next_tile_fits:
            grid_tiles.append(next_tile)
            grid_tile_orients.append(next_tile_orient)
            if len(grid_tiles)> max_found:
                max_found = len(grid_tiles)
            next_tile = 0
            next_tile_orient = -1

# Part 1
print(tilesraw[grid_tiles[0]]['id']*tilesraw[grid_tiles[11]]['id']*tilesraw[grid_tiles[132]]['id']*tilesraw[grid_tiles[143]]['id'])

# Tile transform function courtesy of Katie
def tile_transform(tile_grid,orientation): # should be a 10 by 10 grid, fed in as a list of 10 strings of length 10
    transformed_grid = copy.deepcopy(tile_grid)
    rows = len(transformed_grid)
    cols = len(transformed_grid[0]) # these should both be 10
    if orientation == 1: # first row l-r becomes last column t-b
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[cols-1-j][i]
            transformed_grid[i] = row_i
    elif orientation == 2: # first row l-r becomes bottom row r-l
        for i in range(rows): # goes through the rows
            transformed_grid[rows-1-i] = tile_grid[i][::-1]
    elif orientation == 3: # first row l-r becomes first column b-t
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[j][cols - 1 - i]
            transformed_grid[i] = row_i
    elif orientation == 4:
        transformed_grid = [row[::-1] for row in tile_grid]
    elif orientation == 5:
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[rows-1-j][cols-1-i]
            transformed_grid[i] = row_i
    elif orientation == 6: # first row l-r becomes bottom row l-r
        for i in range(rows): # goes through the rows
            transformed_grid[i] = tile_grid[rows-1-i]
    elif orientation == 7:
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[j][i]
            transformed_grid[i] = row_i
    #print_grids(tile_grid, transformed_grid)
    return transformed_grid


om = [0,3,2,1,7,6,5,4] # map from orientations used for edges to ones used in tile_transform
bigpictiles = [ tile_transform(tilesraw[grid_tiles[i]]['tile'],om[grid_tile_orients[i]]) for i in range(144)]

bigpic=[]
for row in range(12):
    for i in range(1,9):
        bigpicrow = ''.join([ bigpictiles[n][i][1:-1] for n in range(12*row, 12*row + 12) ])
        bigpic.append(bigpicrow)

'''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
monster_coords=[[0,18],[1,0],[1,5],[1,6],[1,11],[1,12],[1,17],[1,18],[1,19],[2,1],[2,4],[2,7],[2,10],[2,13],[2,16]]

def find_monsters(bigpic):
    found_monsters = []
    for row in range(96):
        for col in range(96):
            is_monster = True
            for mc in monster_coords:
                if row+mc[0] >=96 or col+mc[1] >= 96 or bigpic[row+mc[0]][col+mc[1]] == '.':
                    is_monster=False
            if is_monster:
                found_monsters.append([row,col])
    return found_monsters

# Part 2
for i in range(8):
    bigpic_transformed = tile_transform(bigpic,i)
    monster_locs = find_monsters(bigpic_transformed)
    if len(monster_locs)>0:
        print(sum(sum(x=='#' for x in bigpicrow) for bigpicrow in bigpic_transformed) - 15*len(monster_locs))


