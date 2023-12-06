# Time:        62     64     91     90
# Distance:   553   1010   1473   1074

times=[62, 64, 91, 90]
dists=[553, 1010, 1473, 1074]

ways=[]
for i in range(4):
    num_ways=0
    for j in range(1,times[i]+1):
        if j*(times[i]-j) > dists[i]:
            num_ways += 1
    ways.append(num_ways)

tot = 1
for n in ways:
    tot *= n
print(ways)
print(tot)

time = 62649190
dist = 553101014731074

i = 0
while i*(time-i)<dist:
    i += 10000

i = i-10000
while i*(time-i) < dist:
    i += 1

print(time+1-(2*i))
