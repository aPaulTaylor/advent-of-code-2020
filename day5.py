with open('c:/Users/paula/PycharmProjects/advent-of-code/day5-input.txt', 'r') as f:
    puzzle_input = f.readlines()

puzzle_input = [x.strip() for x in puzzle_input]


def bsp_to_id(bsp):
    bsp_rev = bsp[::-1]
    seat_id = 0
    for i in range(10):
        if bsp_rev[i] in 'BR':
            seat_id += 2 ** i
    return seat_id


all_seat_ids = [bsp_to_id(bsp) for bsp in puzzle_input]

print(max(all_seat_ids))
print([i for i in range(min(all_seat_ids), max(all_seat_ids)) if i not in all_seat_ids])
