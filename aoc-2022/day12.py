with open('input/day12-input.txt', 'r') as f:
    heightmap = [x.strip() for x in f.readlines()]

S_row = min(i for i in range(len(heightmap)) if 'S' in heightmap[i])
S_col = heightmap[S_row].index('S')
E_row = min(i for i in range(len(heightmap)) if 'E' in heightmap[i])
E_col = heightmap[S_row].index('E')

heightmap[S_row] = heightmap[S_row].replace('S','a')
heightmap[E_row] = heightmap[E_row].replace('E','z')

heightmap = [[ord(x)-96 for x in hm_row] for hm_row in heightmap]
map_size=len(heightmap)*len(heightmap[0])

S_dists={(S_row,S_col):0}
while (E_row,E_col) not in S_dists:
    new_S_dists = {}
    for pt in S_dists.keys():
        pt_ht = heightmap[pt[0]][pt[1]]
        for adj in [(-1,0),(1,0),(0,1),(0,-1)]:
            pt_new = (pt[0]+adj[0],pt[1]+adj[1])
            if pt_new[0] in range(len(heightmap)) and pt_new[1] in range(len(heightmap[0])):
                if pt_new not in S_dists:
                    if heightmap[pt_new[0]][pt_new[1]]-pt_ht < 2:
                        new_S_dists[pt_new]=S_dists[pt]+1
    S_dists.update(new_S_dists)

print(S_dists[(E_row,E_col)])

S_dists={}
for r in range(len(heightmap)):
    for c in range(len(heightmap[0])):
        if heightmap[r][c]==1:
            S_dists[(r,c)]=0

while (E_row,E_col) not in S_dists:
    new_S_dists = {}
    for pt in S_dists.keys():
        pt_ht = heightmap[pt[0]][pt[1]]
        for adj in [(-1,0),(1,0),(0,1),(0,-1)]:
            pt_new = (pt[0]+adj[0],pt[1]+adj[1])
            if pt_new[0] in range(len(heightmap)) and pt_new[1] in range(len(heightmap[0])):
                if pt_new not in S_dists:
                    if heightmap[pt_new[0]][pt_new[1]]-pt_ht < 2:
                        new_S_dists[pt_new]=S_dists[pt]+1
    S_dists.update(new_S_dists)

print(S_dists[(E_row,E_col)])