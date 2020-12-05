with open('c:/Users/paula/PycharmProjects/advent-of-code/day5-input.txt', 'r') as f:
    puzzle_input = f.readlines()


def bsp_to_id(bsp):
    bsp_rev = bsp[::-1]
    seat_id = 0
    for i in range(10):
        seat_id += (2 ** i) * (bsp_rev[i] in 'BR')
    return seat_id


all_seat_ids = [bsp_to_id(bsp.strip()) for bsp in puzzle_input]

print(max(all_seat_ids))
print([i for i in range(min(all_seat_ids), max(all_seat_ids)) if i not in all_seat_ids])
