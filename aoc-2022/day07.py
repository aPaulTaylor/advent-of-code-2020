with open('input/day07-input.txt', 'r') as f:
    terminal_log = [x.strip().split(' ') for x in f.readlines()]

filesystem={  }
dir_files={'/':0}
cur_path=[]

for ln in terminal_log:
    if ln[0]=='$':
        if ln[1]=='cd':
            if ln[2]=='/':
                cur_path=[]
            elif ln[2]=='..':
                cur_path.pop()
            else:
                cur_path.append(ln[2])
        elif ln[1]=='ls':
            pass
    else:
        if ln[0]=='dir':
            cur_dir = filesystem
            for pt in cur_path:
                cur_dir = cur_dir[pt]
            if ln[1] not in cur_dir.keys():
                cur_dir[ln[1]] = {}
                dir_files[''.join(['/'+x for x in cur_path])+'/'+ln[1]]=0
        else:
            size=int(ln[0])
            dir_files['/'] += size
            for i in range(1,len(cur_path)+1):
                dir_files[''.join(['/'+x for x in cur_path[:i]])]+=size

pt1_sum=0
space_target=30000000-(70000000-dir_files['/'])
best_folder_size=70000000
for dir in dir_files.keys():
    if dir_files[dir]<=100000:
        pt1_sum+=dir_files[dir]
    if dir_files[dir]>space_target and dir_files[dir]<best_folder_size:
        best_folder_size=dir_files[dir]
print(pt1_sum)
print(best_folder_size)