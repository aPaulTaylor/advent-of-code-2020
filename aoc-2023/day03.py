with open('day03-input.txt', 'r') as f:
    eng = [x.strip() for x in f.readlines()]

nums=[]
symbols={}
ADJ_COORDS=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

curr_num = 0
curr_num_coords = set()

for i in range(len(eng)):
    for j in range(len(eng[0])):
        if eng[i][j] in '1234567890':
            curr_num = 10*curr_num + int(eng[i][j])
            curr_num_coords.add((i,j))
        else:
            if curr_num>0:
                num_dict={'num':curr_num, 'coords':curr_num_coords}
                nums.append(num_dict)
                curr_num=0
                curr_num_coords = set()
            if eng[i][j] != '.':
                symbols[(i,j)]=eng[i][j]

part_nums_sum=0

for num in nums:
    is_pt=False
    for cd in num['coords']:
        for adj in ADJ_COORDS:
            if (cd[0]+adj[0],cd[1]+adj[1]) in symbols:
                if not is_pt:
                    part_nums_sum+=num['num']
                    is_pt=True

print(part_nums_sum)

tot_ratio=0
for sym in symbols:
    if symbols[sym]=='*':
        sym_coord = symbols[sym]
        adj_nums=[]
        for num in nums:
            if any( (sym[0]-c[0],sym[1]-c[1]) in ADJ_COORDS for c in num['coords'] ):
                adj_nums.append(num['num'])
        if len(adj_nums)==2:
            gr=1
            for adj_num in adj_nums:
                gr *= adj_num
            tot_ratio+=gr

print(tot_ratio)