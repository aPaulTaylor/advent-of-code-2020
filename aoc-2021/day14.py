with open('input/day14-input.txt', 'r') as f:
    polymer = [x.strip() for x in f.readlines()]

template=polymer[0]
rules = {x[:2]:x[-1] for x in polymer[2:]}
pairs={}
for i in range(len(template)-1):
    pair=template[i:i+2]
    if pair in pairs:
        pairs[pair] +=1
    else:
        pairs[pair] = 1

for i in range(40):
    newpairs = {}
    for pair in pairs.keys():
        if pair in rules:
            newpair_l=pair[0]+rules[pair]
            newpair_r=rules[pair]+pair[1]
            newpairs[newpair_l] = (pairs[pair] if newpair_l not in newpairs else newpairs[newpair_l]+pairs[pair])
            newpairs[newpair_r] = (pairs[pair] if newpair_r not in newpairs else newpairs[newpair_r]+pairs[pair])
        else:
            newpairs[pair] = pairs[pair]
    pairs=newpairs

letter_freqs={}
for x in pairs.keys():
    letter_freqs[x[0]] = (pairs[x] if x[0] not in letter_freqs else letter_freqs[x[0]]+pairs[x])
    letter_freqs[x[1]] = (pairs[x] if x[1] not in letter_freqs else letter_freqs[x[1]] + pairs[x])
letter_freqs['C']+=1
letter_freqs['B']+=1
print((max(letter_freqs.values())-min(letter_freqs.values()))//2)


