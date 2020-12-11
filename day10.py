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
    for d in diffs:
        if d==1:
            cur_run_len+=1
        else:
            runlens.append(cur_run_len)
            cur_run_len=0
    runlens.append(cur_run_len)
    return runlens

rl=runs_of_1s(diffs)

# there are only joltage differences of 1 and 3 in the sequence.
# a 3-jolt difference means both adapters must be used.
# so the number of combinations depends on the lengths of runs of 1-jolt differences:
# run of one 1-jolt diff: 1 combination (eg 2,5,6,9 -- all must be used)
# run of two 1-jolt diffs: 2 combinations (eg 2,5,6,7,10 -- 6 can be used or not) - none of these in sequence so omitted
# run of three 1-jolt diffs: 4 combinations (eg 2,5,6,7,8,11 -- 6 and 7 can each be used or not)
# run of four 1-jolt diffs: 7 combinations (eg 2,5,6,7,8,9,12 -- any combination of at least one of 6,7,8)
# extra *2 for the choice of either of the first two adapters (joltages 1,2) not covered by the above
print(2**sum(r==2 for r in rl) * 4**sum(r==3 for r in rl) * 7**sum(r==4 for r in rl) * 2)



