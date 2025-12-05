with open('c:/GitHub/advent-of-code-2020/aoc-2025/input/day05-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

ranges=[l for l in input if '-' in l]
nums=[int(l) for l in input if '-' not in l and l!='']

ranges_rng = [range(int(r.split('-')[0]),int(r.split('-')[1])+1) for r in ranges]

print(sum(1 for n in nums if any(n in r for r in ranges_rng)))

ranges_nums = [(int(r.split('-')[0]),int(r.split('-')[1])) for r in ranges]
final_ranges= []

while len(ranges_nums)>0:
    new_ranges=[]
    found_overlap=False
    for i in range(1,len(ranges_nums)):
        if not found_overlap:
            if min(ranges_nums[0][1],ranges_nums[i][1])>=max(ranges_nums[0][0],ranges_nums[i][0]):
                found_overlap=True
                new_ranges.append((min(ranges_nums[0][0],ranges_nums[i][0]),max(ranges_nums[0][1],ranges_nums[i][1])))
            else:
                new_ranges.append(ranges_nums[i])
        else:
            new_ranges.append(ranges_nums[i])
    if not found_overlap:
        final_ranges.append(ranges_nums[0])
    ranges_nums=new_ranges


total_size=0
for r in final_ranges:
    total_size += r[1]-r[0]+1

print(total_size)