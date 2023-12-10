with open('input/day10-input.txt', 'r') as f:
    PIPE_MAP = [x.strip() for x in f.readlines()]

MOVES_MAP = {
    (1,0,'L'): (0,1),
    (1,0,'J'): (0,-1),
    (-1,0,'F'): (0,1),
    (-1,0,'7'): (0,-1),
    (1,0,'|'): (1,0),
    (-1,0,'|'): (-1,0),
    (0,1,'7'): (1,0),
    (0,1,'J'): (-1,0),
    (0,-1,'F'): (1,0),
    (0,-1,'L'): (-1,0),
    (0,1,'-'): (0,1),
    (0,-1,'-'): (0,-1)
}

def get_next_coord(coords):
    last_move=(coords[-1][0]-coords[-2][0], coords[-1][1]-coords[-2][1])
    next_move = MOVES_MAP[(last_move[0],last_move[1],PIPE_MAP[coords[-1][0]][coords[-1][1]])]
    coords.append( tuple(coords[-1][i]+next_move[i] for i in range(2) ) )
    return coords

S_row = max(i for i in range(len(PIPE_MAP)) if 'S' in PIPE_MAP[i])
S_col = max(i for i in range(len(PIPE_MAP[S_row])) if PIPE_MAP[S_row][i]=='S')

coords=[(S_row,S_col),(S_row,S_col+1)]

while coords[-1]!=coords[0]:
    coords=get_next_coord(coords)
pipe_coords=set(coords)

print((len(coords)-1)//2)

def flood_fill(fill_coords):
    while True:
        new_coords=set([])
        for c in fill_coords:
            for dif in [(1,0),(-1,0),(0,1),(0,-1)]:
                nbr = (c[0] + dif[0], c[1] + dif[1])
                if nbr[0]>=0 and nbr[0]<len(PIPE_MAP) and nbr[1]>=0 and nbr[1]<len(PIPE_MAP[0]):
                    if nbr not in fill_coords and nbr not in pipe_coords:
                        new_coords.add(nbr)
        if len(new_coords)==0:
            return fill_coords
        else:
            fill_coords = fill_coords.union(new_coords)
            #print(len(fill_coords))

inside_coords=set([])
for i in range(1,len(coords)):
    cur_dir=( coords[i][0]-coords[i-1][0], coords[i][1]-coords[i-1][1] )
    cur_symb = PIPE_MAP[coords[i][0]][coords[i][1]]
    turn_right={(1,0):(0,1), (-1,0):(0,-1), (0,1):(-1,0), (0,-1):(1,0)}
    right_dir=turn_right[cur_dir]
    right_coord=( coords[i][0]+right_dir[0], coords[i][1]+right_dir[1] )
    if right_coord not in pipe_coords:
        inside_coords.add(right_coord)

coords=coords[::-1]
for i in range(1,len(coords)):
    cur_dir=( coords[i][0]-coords[i-1][0], coords[i][1]-coords[i-1][1] )
    cur_symb = PIPE_MAP[coords[i][0]][coords[i][1]]
    turn_right={(1,0):(0,-1), (-1,0):(0,1), (0,1):(1,0), (0,-1):(-1,0)}
    right_dir=turn_right[cur_dir]
    right_coord=( coords[i][0]+right_dir[0], coords[i][1]+right_dir[1] )
    if right_coord not in pipe_coords:
        inside_coords.add(right_coord)

print(len(inside_coords))
inside_coords = flood_fill(inside_coords)
print(len(inside_coords))
for row in range(140):
    row_str=''
    for col in range(140):
        if (row,col) in pipe_coords:
            row_str=row_str+'X'
        elif (row,col) in inside_coords:
            row_str=row_str+'O'
        else:
            row_str=row_str+'.'
    print(row_str)