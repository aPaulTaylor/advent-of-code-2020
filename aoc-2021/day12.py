with open('input/day12-input.txt', 'r') as f:
    caves = [tuple(x.strip().split('-')) for x in f.readlines()]

caves.extend([x[::-1] for x in caves])
caves = [x for x in caves if x[1]!='start']

def extend_path(path, caves, allow_small_twice):
    small_caves_visited = [x for x in path if x==str.lower(x)]
    if allow_small_twice:
        visited_small_twice = len(small_caves_visited)>len(set(small_caves_visited))
    else:
        visited_small_twice = True
    valid_steps = [x for x in caves if x[0]==path[-1]]
    valid_steps = [x for x in valid_steps if x[1]==str.upper(x[1]) or x[1]=='end' or x[1] not in path or not visited_small_twice]
    return [path[:]+[x[1]] for x in valid_steps]

def make_all_paths(caves, allow_small_twice):
    all_paths = [['start']]
    completed_paths=[]
    while len(all_paths)>0:
        new_paths=[]
        for path in all_paths:
            new_paths.extend(extend_path(path, caves, allow_small_twice))
        completed_paths.extend([x for x in new_paths if x[-1]=='end'])
        all_paths = [x for x in new_paths if x[-1]!='end']
    return len(completed_paths)

print(make_all_paths(caves, False))
print(make_all_paths(caves, True))