with open('c:/Users/paula/PycharmProjects/advent-of-code/day13-input.txt', 'r') as f:
    busnotes = f.readlines()

start_time = int(busnotes[0].strip())
buses = [int(x) for x in busnotes[1].split(',') if not x=='x']
rel_times = [i for i,x in enumerate(busnotes[1].split(',')) if not x=='x']

# Part 1
timefound=False
dep_time=start_time-1
while not timefound:
    dep_time+=1
    if any(dep_time % bus_no == 0 for bus_no in buses):
        timefound=True
        print((dep_time - start_time)*[bus for bus in buses if dep_time % bus == 0][0])

# Part 2
def find_earliest_time(buses, rel_times):
    if len(buses) == 1:
        return rel_times[0]
    time=rel_times[0] - buses[0]
    while True:
        time += buses[0]
        if time % buses[1] == rel_times[1]:
            return find_earliest_time([buses[0]*buses[1]]+buses[2:], [time]+rel_times[2:])

print(find_earliest_time(buses, [-rel_times[i] % buses[i] for i in range(len(buses))]))
