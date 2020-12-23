
'''
The cups will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were
32415, there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would
be labeled 3, 2, 4, 1, 5, and then back to 3 again.

Before the crab starts, it will designate the first cup in your list as the current cup.
The crab is then going to do 100 moves.

Each move, the crab does the following actions:

The crab picks up the three cups that are immediately clockwise of the current cup.
They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
If this would select one of the cups that was just picked up, the crab will keep subtracting one until it
finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value
on any cup's label, it wraps around to the highest value on any cup's label instead.
The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
They keep the same order as when they were picked up.
The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
'''

cups=[3,6,4,2,9,7,5,8,1] # actual input
#cups=[3,8,9,1,2,5,4,6,7] # example input
cur_cup_ind=0
num_cups=9
for i in range(100):
    cur_cup = cups[cur_cup_ind]
    inds_to_remove = [(cur_cup_ind + j) % num_cups for j in [1,2,3] ]
    picked_up_cups=[cups[j] for j in inds_to_remove]
    cups = [cups[j] for j in range(num_cups) if j not in inds_to_remove]
    dest_cup = cur_cup-1
    if dest_cup == 0:
        dest_cup = 9
    while dest_cup not in cups:
        dest_cup -= 1
        if dest_cup == 0:
            dest_cup = num_cups
    dest_cups_ind = cups.index(dest_cup)+1
    cups = cups[:dest_cups_ind]+picked_up_cups+cups[dest_cups_ind:]
    cur_cup_ind = cups.index(cur_cup) + 1
    if cur_cup_ind == 9:
        cur_cup_ind = 0

print(cups)


cups = [3,6,4,2,9,7,5,8,1] + list(range(10,1000001))
orig_cups = cups[:]
cur_cup_ind=0
num_cups=1000000
i=0
while cups!=orig_cups or i==0:
    if i%100==0:
        print(i)
    i+=1
    cur_cup = cups[cur_cup_ind]
    inds_to_remove = [(cur_cup_ind + j) % num_cups for j in [1,2,3] ]
    picked_up_cups=[cups[j] for j in inds_to_remove]
    cups = [cups[j] for j in range(num_cups) if j not in inds_to_remove]
    dest_cup = cur_cup-1
    if dest_cup == 0:
        dest_cup = num_cups
    while dest_cup not in cups:
        dest_cup -= 1
        if dest_cup == 0:
            dest_cup = num_cups
    dest_cups_ind = cups.index(dest_cup)+1
    cups = cups[:dest_cups_ind]+picked_up_cups+cups[dest_cups_ind:]
    cur_cup_ind = cups.index(cur_cup) + 1
    if cur_cup_ind == num_cups:
        cur_cup_ind = 0
    i+=1
