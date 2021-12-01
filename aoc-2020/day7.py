with open('/aoc-2020/day7-input.txt', 'r') as f:
    bag_rules = f.readlines()

bag_rules = [x.strip() for x in bag_rules]
bag_rules = [x.split(' contain ') for x in bag_rules]


def parse_rule(rule):
    outer_bag = rule[0].replace(' bags', '')
    if rule[1] == 'no other bags.':
        inner_bags = []
    else:
        inner_bags = rule[1][:-1].replace(' bags', '').replace(' bag', '').split(', ')
        inner_bags = [[int(x.split(' ')[0]), x[2:]] for x in inner_bags]
    return (outer_bag, inner_bags)


bag_rules_dict = dict([parse_rule(x) for x in bag_rules])


def find_valid_outer_bags(bag_type, bag_rules_dict):
    current_outer_bags = set([bag_type])
    new_bags_found = True
    while new_bags_found:
        new_bags_found = False
        for bag in current_outer_bags:
            valid_containers = [x for x in bag_rules_dict.keys() if
                                any(content[1] == bag for content in bag_rules_dict[x])]
            if any(x not in current_outer_bags for x in valid_containers):
                new_bags_found = True
                current_outer_bags = current_outer_bags.union(set(valid_containers))
    return current_outer_bags


def count_inner_bags(outer_bag, bag_rules_dict):
    total_bags = 0
    current_bag_layer = [outer_bag]
    while len(current_bag_layer) > 0:
        contained_bag_layer = []
        for bag in current_bag_layer:
            for content_item in bag_rules_dict[bag]:
                contained_bag_layer.extend([content_item[1]] * content_item[0])
                total_bags += content_item[0]
        current_bag_layer = contained_bag_layer
    return total_bags


# Part 1
print(len(find_valid_outer_bags('shiny gold', bag_rules_dict)) - 1)

# Part 2
print(count_inner_bags('shiny gold', bag_rules_dict))


# Part 2 WITH RECURSION
def get_full_contents(bag, brd):
    immediate_contents = []
    for content in brd[bag]:
        immediate_contents.extend([content[1]] * content[0])
    return [get_full_contents(x, brd) for x in immediate_contents]


print(str(get_full_contents('shiny gold', bag_rules_dict)).count('[') - 1)


# Part 1 with recursion copied off Ben
def get_containing_colours(bag):
    containing_colours = set([x for x in bag_rules_dict.keys() if any([y[1] == bag for y in bag_rules_dict[x]])])
    return containing_colours.union(*[get_containing_colours(cc) for cc in containing_colours])

print(len(get_containing_colours('shiny gold')))
