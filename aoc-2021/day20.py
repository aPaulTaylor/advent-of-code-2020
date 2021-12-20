with open('input/day20-input.txt', 'r') as f:
    trenchmap = [x.strip() for x in f.readlines()]

algo = trenchmap[0]
map_hashes=set()
for i in range(2,len(trenchmap)):
    for j in range(len(trenchmap[i])):
        if trenchmap[i][j]=='#':
            map_hashes.add((i,j))

def iterate_map(map_hashes,bg_is_hashes):
    min_x = min([t[0] for t in map_hashes])
    max_x = max([t[0] for t in map_hashes])
    min_y = min([t[1] for t in map_hashes])
    max_y = max([t[1] for t in map_hashes])
    new_map_hashes=set()
    for i in range(min_x-1,max_x+2):
        for j in range(min_y-1,max_y+2):
            n=256
            algo_index=0
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if min_x<=i+di<=max_x and min_y<=j+dj<=max_y:
                        if (i+di,j+dj) in map_hashes:
                            algo_index+=n
                    else:
                        if bg_is_hashes:
                            algo_index+=n
                    n=n//2
            if algo[algo_index]=='#':
                new_map_hashes.add((i,j))
    return new_map_hashes

for it in range(50):
    map_hashes=iterate_map(map_hashes,it%2)
    if it in [1,49]:
        print(f'{len(map_hashes)} lit pixels after {it+1} iterations')
