import copy

with open('/aoc-2020/day8-input.txt', 'r') as f:
    program = f.readlines()

program = [[x.split(' ')[0], int(x.split(' ')[1])] for x in program]


def run_prog(prog):
    times_run = [0 for i in range(len(prog))]
    cur_step = 0
    acc = 0
    while 0 <= cur_step < len(times_run) and times_run[cur_step] == 0:
        times_run[cur_step] += 1
        if prog[cur_step][0] == 'acc':
            acc += prog[cur_step][1]
            next_step = cur_step + 1
        if prog[cur_step][0] == 'jmp':
            next_step = cur_step + prog[cur_step][1]
        if prog[cur_step][0] == 'nop':
            next_step = cur_step + 1
        cur_step = next_step
    if cur_step == len(times_run):
        success = True
    else:
        success = False
    return [acc, success]

#Part 1
print(run_prog(program))

#Part 2
for i in range(len(program)):
    if program[i][0] in ['nop', 'jmp']:
        new_prog = copy.deepcopy(program)
        if program[i][0] == 'nop':
            new_prog[i][0] = 'jmp'
        else:
            new_prog[i][0] = 'nop'
        prog_res = run_prog(new_prog)
        if prog_res[1]:
            print(f'Success changing line {i}; value of accumulator: {prog_res[0]}')
