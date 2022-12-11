with open('input/day11-input.txt', 'r') as f:
    monkey_behaviour = [x.strip() for x in f.readlines()]

items=[[int(x) for x in l.split(':')[1].split(',')] for l in monkey_behaviour[1::7]]
div_tests = [int(x.split(' ')[-1]) for x in monkey_behaviour[3::7]]
destinations=[
    [int(x.split(' ')[-1]) for x in monkey_behaviour[5::7]],
    [int(x.split(' ')[-1]) for x in monkey_behaviour[4::7]]
]
munctions=[lambda x: x*17, lambda x: x+1, lambda x: x+3, lambda x: x+5, lambda x: x*x, lambda x: x+2, lambda x: x+4, lambda x: x*19]
inspect_counts=[0]*8

for rnd in range(20):
    for mnk in range(8):
        for itm in items[mnk]:
            inspect_counts[mnk]+=1
            itm = munctions[mnk](itm)
            itm = int(itm/3)
            items[destinations[itm % div_tests[mnk]==0][mnk]].append(itm)
        items[mnk]=[]

print(sorted(inspect_counts)[-1]*sorted(inspect_counts)[-2])

prod=1
for d in div_tests:
    prod = prod*d

items=[[int(x) for x in l.split(':')[1].split(',')] for l in monkey_behaviour[1::7]]
inspect_counts=[0]*8

for rnd in range(10000):
    for mnk in range(8):
        for itm in items[mnk]:
            inspect_counts[mnk]+=1
            itm = munctions[mnk](itm) % prod
            items[destinations[itm % div_tests[mnk]==0][mnk]].append(itm)
        items[mnk]=[]

print(sorted(inspect_counts)[-1]*sorted(inspect_counts)[-2])


