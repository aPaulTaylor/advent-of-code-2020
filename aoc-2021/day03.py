with open('input/day03-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

## Part 1
onemajorities = [ sum(num[i]=='1' for num in input)*2>len(input) for i in range(12) ]
gamma = sum(2**(11-i) for i in range(12) if onemajorities[i])
print(gamma*(2**12 - gamma - 1))

## Part 2
def reduce_diagnostic(diag,d,criteria):
    num_ones = sum(x[d]=='1' for x in diag)
    majority = '1' if num_ones*2 >= len(diag) else '0'
    return [x for x in diag if (x[d]==majority)^(criteria=='CO2') ]

prod=1
for criteria in ['oxygen','CO2']:
    diag = [x for x in input]
    d=0
    while len(diag)>1:
        diag=reduce_diagnostic(diag,d,criteria)
        d+=1
    prod *= sum(int(diag[0][i])*(2**(11-i)) for i in range(12))
print(prod)