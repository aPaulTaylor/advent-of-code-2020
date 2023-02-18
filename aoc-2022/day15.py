import re

with open('input/day15-input.txt', 'r') as f:
    sensor_beacon_info = [ list(map(int,re.findall(r'[\-\d]+', x))) for x in f.readlines()]

sensors_dists = set()
for sb in sensor_beacon_info:
    sensor=(sb[0],sb[1])
    dist=abs(sb[0]-sb[2])+abs(sb[1]-sb[3])
    sensors_dists.add((sensor,dist))

print(sum(sd[1] for sd in sensors_dists))

Y_CONST=2000000
#Y_CONST=10

no_beacon_xs=set()
for sd in sensors_dists:
    x_dist=sd[1] - abs(sd[0][1]-Y_CONST)
    if x_dist>0:
        no_beacon_xs.update(range(sd[0][0]-x_dist,sd[0][0]+x_dist+1))
print(len(no_beacon_xs))


def test_row(r):
    excl_ranges=set()
    for sd in sensors_dists:
        x_d = sd[1] - abs(sd[0][1] - r)
        excl_ranges.add((sd[0][0]-x_d, sd[0][0]+x_d))
    i=0
    while i<=4000000:
        adv=False
        for er in excl_ranges:
            if i>=er[0] and i<=er[1]:
                i=er[1]+1
                adv=True
                break
        if not adv:
            return i
    return -1

for r in range(4000001):
    c=test_row(r)
    if c>-1:
        print((r,c))
        print(c*4000000 + r)




