with open('c:/Users/paula/PycharmProjects/advent-of-code/day13-input.txt', 'r') as f:
    busnotes = f.readlines()

start_time = int(busnotes[0].strip())
buses = [int(x) for x in busnotes[1].split(',') if not x=='x']

# Part 1
timefound=False
dep_time=start_time-1
while not timefound:
    dep_time+=1
    if any(dep_time % bus_no == 0 for bus_no in buses):
        timefound=True
        print(dep_time - start_time)
        print([bus for bus in buses if dep_time % bus == 0])

# Part 2
rel_times = []
for i,b in enumerate(busnotes[1].split(',')):
    if not b == 'x':
        rel_times.append(i % int(b))


def find_earliest_time(buses, rel_times):
    print(buses,rel_times)
    if len(buses) == 1:
        return rel_times[0]
    time=rel_times[0] - buses[0]
    sol_found=False
    while not sol_found:
        time += buses[0]
        if time % buses[1] == rel_times[1]:
            sol_found=True
            print(time)
            return find_earliest_time([buses[0]*buses[1]]+buses[2:], [time]+rel_times[2:])


test_buses = [7,13,59,31,19]
test_times = [0,1,4,6,7]
print(find_earliest_time(test_buses, [test_buses[i]-test_times[i] for i in range(len(test_buses))]))

print(find_earliest_time(buses, [buses[i]-rel_times[i] for i in range(len(buses))]))
