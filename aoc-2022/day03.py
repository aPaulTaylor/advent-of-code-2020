import string
with open('input/day03-input.txt', 'r') as f:
    rucksacks = [x.strip() for x in f.readlines()]

def duplicate_item_priority(rsck):
    dupl=set(rsck[:int(len(rsck)/2)]).intersection(set(rsck[int(len(rsck)/2):])).pop()
    return string.ascii_letters.find(dupl) + 1

print(sum(duplicate_item_priority(rsck) for rsck in rucksacks))

p_sum=0
for i in range(0,len(rucksacks),3):
    badge=set(string.ascii_letters)
    badge.intersection_update(*[set(rsck) for rsck in rucksacks[i:i+3]])
    p_sum+=string.ascii_letters.find(badge.pop())+1
print(p_sum)
