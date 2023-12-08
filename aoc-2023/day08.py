from math import gcd

with open('input/day08-input.txt', 'r') as f:
    network_raw = [x.strip() for x in f.readlines()]

directions=network_raw[0]

nodes={}
for node in network_raw[2:]:
    source=node.split('=')[0].strip()
    dests=[x.strip() for x in node.split('=')[1][2:-1].split(',')]
    nodes[source]=dests

def get_num_steps(pos,st,criteria):
    i = 0
    while not pos[st:]==criteria:
        if directions[i % len(directions)]=='L':
            pos=nodes[pos][0]
        else:
            pos=nodes[pos][1]
        i+=1
    return i

print(get_num_steps('AAA',0,'ZZZ'))

poses=[x for x in nodes.keys() if x[-1]=='A']
nums_steps=[get_num_steps(pos,2,'Z') for pos in poses]

lcm = 1
for i in nums_steps:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)