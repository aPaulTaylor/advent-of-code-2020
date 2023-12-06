with open('input/day05-input.txt', 'r') as f:
    almanac_raw = [x.strip() for x in f.readlines()]

almanac_raw_test='''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''.split('\n')

seeds=[int(x) for x in almanac_raw[0].split(' ')[1:]]

maps=[]
cur_map=[]
for l in almanac_raw[3:]:
    if l=='':
        maps.append(cur_map)
        cur_map=[]
    elif 'map' in l:
        pass
    else:
        cur_map.append(tuple(int(x) for x in l.split(' ')))
maps.append(cur_map)

def map_number(n,map):
    for rule in map:
        if n in range(rule[1],rule[1]+rule[2]):
            return n+rule[0]-rule[1]
    return n

def process_seed(s,maps):
    for map in maps:
        s=map_number(s,map)
    return s

print(min(process_seed(s,maps) for s in seeds))


def map_range(r_min, r_len, map_in):
    map = [x for x in map_in]
    map.sort(key=lambda r:r[1])
    rule_mins=[r[1] for r in map]
    rule_maxes=[r[1]+r[2] for r in map]
    null_rules=[]
    for i in range(len(map)-1):
        if rule_maxes[i]<rule_mins[i+1]+1:
            null_rules.append([rule_maxes[i]+1, rule_maxes[i]+1, rule_mins[i+1]-rule_maxes[i]-1])
    map.extend(null_rules)
    map.append([rule_maxes[-1]+1, rule_maxes[-1]+1, 999999999999])

    ranges_out=[]
    r_max=r_min+r_len-1
    for rule in map:
        rule_range = range(rule[1],rule[1]+rule[2]-1)
        rule_offset=rule[0]-rule[1]
        if r_min in rule_range:
            if r_max in rule_range:
                ranges_out.append( (r_min+rule_offset,r_len) )
            else:
                ranges_out.append( (r_min+rule_offset, rule[1]+rule[2]-r_min ))
        else:
            if r_max in rule_range:
                ranges_out.append((rule[0], r_max-rule[1]+1 ))
    return ranges_out

def process_seed_range(sr,maps):
    ranges = [sr]
    for map in maps:
        new_ranges=[]
        for rng in ranges:
            new_ranges.extend(map_range(rng[0],rng[1],map))
        ranges=new_ranges
    return ranges


min_locs=[]
for i in range(0,len(seeds),2):
    loc_ranges=process_seed_range((seeds[i],seeds[i+1]),maps)
    min_locs.append(min(x[0] for x in loc_ranges))
print(min(min_locs))