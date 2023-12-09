with open('input/day09-input.txt', 'r') as f:
    readings=[ [int(x) for x in rd.strip().split(' ')] for rd in f.readlines() ]

def predict(reading,next):
    diffs=[reading]
    while not all(x==0 for x in diffs[-1]):
        diffs.append([ diffs[-1][i+1] - diffs[-1][i] for i in range(len(diffs[-1])-1)])
    return sum(d[-1 if next else 0]*(1 if next else (-1)**n) for n,d in enumerate(diffs))

print([sum(predict(rd,nx) for rd in readings) for nx in [True,False]])

def pred_rec(reading,pred_next):
    if all(x==0 for x in reading):
        return 0
    else:
        diffs=[reading[i+1]-reading[i] for i in range(len(reading)-1)]
        return reading[-1 if pred_next else 0]+(pred_rec(diffs,pred_next) * (1 if pred_next else -1))

print( [sum(pred_rec(r,nx) for r in readings ) for nx in [True,False]] )