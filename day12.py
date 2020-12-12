with open('c:/Users/paula/PycharmProjects/advent-of-code/day12-input.txt', 'r') as f:
    dirs = [[x.strip()[0],int(x.strip()[1:])] for x in f.readlines()]

ship_pos = {'E':0, 'N':0, 'dir':90}

def update_ship_pos(ship_pos,dir):
    if dir[0]=='L':
        ship_pos['dir'] = (ship_pos['dir']-dir[1]) % 360
    if dir[0]=='R':
        ship_pos['dir'] = (ship_pos['dir']+dir[1]) % 360
    bearings={0:'N', 90:'E', 180:'S', 270:'W'}
    if dir[0]=='F':
        dir[0]=bearings[ship_pos['dir']]
    if dir[0]=='N':
        ship_pos['N'] += dir[1]
    if dir[0]=='S':
        ship_pos['N'] -= dir[1]
    if dir[0]=='E':
        ship_pos['E'] += dir[1]
    if dir[0]=='W':
        ship_pos['E'] -= dir[1]

for d in dirs:
    update_ship_pos(ship_pos,d)

print(abs(ship_pos['E'])+abs(ship_pos['N']))

with open('c:/Users/paula/PycharmProjects/advent-of-code/day12-input.txt', 'r') as f:
    dirs = [[x.strip()[0],int(x.strip()[1:])] for x in f.readlines()]

ship_pos = {'E':0, 'N':0, 'dir':0}
waypoint= {'E':10, 'N':1}

def update_ship_and_waypoint(ship_pos, waypoint, dir):
    if dir[0]=='N':
        waypoint['N'] += dir[1]
    if dir[0]=='S':
        waypoint['N'] -= dir[1]
    if dir[0]=='E':
        waypoint['E'] += dir[1]
    if dir[0]=='W':
        waypoint['E'] -= dir[1]
    if dir[0] in 'LR' and dir[1]==180:
        waypoint['E'],waypoint['N'] = -waypoint['E'],-waypoint['N']
    if dir in [['L',90],['R',270]]:
        waypoint['E'],waypoint['N'] = -waypoint['N'],waypoint['E']
    if dir in [['L',270],['R',90]]:
        waypoint['E'],waypoint['N'] = waypoint['N'],-waypoint['E']
    if dir[0]=='F':
        ship_pos['N'] += waypoint['N']*dir[1]
        ship_pos['E'] += waypoint['E'] * dir[1]

for d in dirs:
    update_ship_and_waypoint(ship_pos,waypoint,d)

print(abs(ship_pos['E'])+abs(ship_pos['N']))