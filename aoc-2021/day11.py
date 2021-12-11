with open('input/day11-input.txt', 'r') as f:
    octomap = [[int(n) for n in x[:-1]] for x in f.readlines()]

total_flashes=0
for step_num in range(250):
    new_flashes=True
    flash_coords=set()
    octomap = [[n + 1 for n in ol] for ol in octomap]
    while new_flashes:
        new_flashes=False
        for i in range(10):
            for j in range(10):
                if octomap[i][j]>9 and (i,j) not in flash_coords:
                    total_flashes+=1
                    flash_coords.add((i,j))
                    new_flashes=True
                    for di in [-1,0,1]:
                        for dj in [-1,0,1]:
                            if (not (di==0 and dj==0)) and i+di in range(10) and j+dj in range(10):
                                octomap[i+di][j+dj]+=1
    if step_num == 100:
        print(f'{total_flashes} flashes after 100 steps')
    if len(flash_coords)==100:
        print(f'all flash in step {step_num+1}')
        break
    for fc in flash_coords:
        octomap[fc[0]][fc[1]]=0
