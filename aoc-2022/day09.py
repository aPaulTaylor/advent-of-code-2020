with open('input/day09-input.txt', 'r') as f:
    rope_moves = [x.strip().split(' ') for x in f.readlines()]

moves_dict={'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

k_poses=[(0,0) for i in range(10)]
t1_poses_visited=set()
t1_poses_visited.add((0,0))
t9_poses_visited=set()
t9_poses_visited.add((0,0))

for mv in rope_moves:
    for j in range(int(mv[1])):
        k_poses[0]=tuple([k_poses[0][i]+moves_dict[mv[0]][i] for i in range(2)])
        for i in range(1,10):
            h_t = (k_poses[i-1][0]-k_poses[i][0],k_poses[i-1][1]-k_poses[i][1])
            if 2 in h_t or -2 in h_t:
                h_t_new = (int(h_t[0]/2),int(h_t[1]/2))
            else:
                h_t_new=h_t
            k_poses[i] = (k_poses[i-1][0]-h_t_new[0],k_poses[i-1][1]-h_t_new[1])
        t1_poses_visited.add(k_poses[1])
        t9_poses_visited.add(k_poses[-1])

print(len(t1_poses_visited))
print(len(t9_poses_visited))