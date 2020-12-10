import itertools

with open('c:/Users/paula/PycharmProjects/advent-of-code/day10-input.txt', 'r') as f:
    joltages = [int(x) for x in f.readlines()]

joltages.sort()

diffs = [joltages[i]-joltages[i-1] for i in range(1,len(joltages))]

# Part 1
print((1+sum(j==1 for j in diffs))*(1+sum(j==3 for j in diffs)))

# Part 2
def runs_of_1s(diffs):
    runlens=[]
    cur_run_len=0
    for i in range(len(diffs)):
        if diffs[i]==1:
            cur_run_len+=1
        else:
            runlens.append(cur_run_len)
            cur_run_len=0
    runlens.append(cur_run_len)
    return runlens

rl=runs_of_1s(diffs)

print(2**sum(r==2 for r in rl) * 4**sum(r==3 for r in rl) * 7**sum(r==4 for r in rl) * 2)



