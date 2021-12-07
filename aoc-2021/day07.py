with open('input/day07-input.txt', 'r') as f:
    input = [int(x) for x in f.read().split(',')]

def get_fuel(crabs,fuel_func):
    best_fuel = -1
    best_pos=0
    for pos in range(max(crabs)+1):
        fuel_req = sum(fuel_func(abs(pos-crab)) for crab in crabs)
        if best_fuel==-1 or best_fuel > fuel_req:
            best_fuel = fuel_req
            best_pos = pos
    return best_pos, best_fuel

print(get_fuel(input,lambda x: x))
print(get_fuel(input,lambda x: (x+1)*x//2))