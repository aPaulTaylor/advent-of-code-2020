import re

with open('input/day15-input.txt', 'r') as f:
    sensor_beacon_info = [ list(map(int,re.findall(r'[\-\d]+', x))) for x in f.readlines()]

sensors_dists = set()
for sb in sensor_beacon_info:
    sensor=(sb[0],sb[1])
    dist=abs(sb[0]-sb[2])+abs(sb[1]-sb[3])
    sensors_dists.add((sensor,dist))

Y_CONST=2000000
#Y_CONST=10

no_beacon_xs=set()
for sd in sensors_dists:
    x_dist=sd[1] - abs(sd[0][1]-Y_CONST)
    if x_dist>0:
        for x in range(0,x_dist+1):
            no_beacon_xs.add(sd[0][0]-x)
            no_beacon_xs.add(sd[0][0]+x)
print(len(no_beacon_xs))

