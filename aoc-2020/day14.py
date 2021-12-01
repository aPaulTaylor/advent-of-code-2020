with open('/aoc-2020/day14-input.txt', 'r') as f:
    program = [ x[:-1].split(' = ') for x in f.readlines()]

## Part 1
def apply_mask(bin_num,mask):
    masked_num = list(mask)
    for i in range(1,len(bin_num)+1):
        if masked_num[-i] == 'X':
            masked_num[-i] = bin_num[-i]
    masked_num = ''.join(masked_num).replace('X','0')
    return masked_num

mem = {}
for instr in program:
    if instr[0] == 'mask':
        mask = instr[1]
    else:
        masked_bin = apply_mask(bin(int(instr[1]))[2:],mask)
        mem[instr[0]] = int(masked_bin,2)

print(sum(mem.values()))

## Part 2
def apply_mask_to_address(address, mask):
    address = '0'*(len(mask)-len(address)) + address
    masked_address=''
    for i in range(len(mask)):
        if mask[i]=='0':
            masked_address += address[i]
        if mask[i]=='1':
            masked_address += '1'
        if mask[i]=='X':
            masked_address += 'X'
    num_Xs = masked_address.count('X')
    X_replacements = [bin(i)[2:] for i in range(2**num_Xs)]
    X_replacements = ['0'*(num_Xs - len(rep)) + rep for rep in X_replacements]
    addresses=[]
    for repl in X_replacements:
        new_address = ''
        repl_ind=0
        for c in masked_address:
            if c=='X':
                new_address += repl[repl_ind]
                repl_ind+=1
            else:
                new_address += c
        addresses.append(int(new_address,2))
    return addresses

mem={}
for instr in program:
    if instr[0] == 'mask':
        mask = instr[1]
    else:
        addresses = apply_mask_to_address(bin(int(instr[0].split('[')[1][:-1]))[2:],mask)
        for add in addresses:
            mem[add] = int(instr[1])

print(sum(mem.values()))