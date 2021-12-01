with open('/aoc-2020/day16-input.txt', 'r') as f:
    tickets = [l.strip() for l in f.readlines()]

rules = tickets[:20]
my_ticket = tickets[22]
nearby_tickets = tickets[25:]


def rule_to_values(rule):
    range1 = rule.split(': ')[1].split(' or ')[0].split('-')
    range2 = rule.split(': ')[1].split(' or ')[1].split('-')
    return list(range(int(range1[0]), int(range1[1]) + 1)) + list(range(int(range2[0]), int(range2[1]) + 1))


all_allowed_vals = set()
for rule in rules:
    all_allowed_vals = all_allowed_vals.union(set(rule_to_values(rule)))

# Part 1
total_invalid = 0
for ticket in nearby_tickets:
    for n in [int(x) for x in ticket.split(',')]:
        if n not in all_allowed_vals:
            total_invalid += n
print(total_invalid)

# Part 2
valid_nearby_tickets = []
for ticket in nearby_tickets:
    ticket_vals = [int(x) for x in ticket.split(',')]
    if all(n in all_allowed_vals for n in ticket_vals):
        valid_nearby_tickets.append(ticket)

rules_dict = {rule.split(':')[0]: rule_to_values(rule) for rule in rules}

valid_ticket_lists = [[int(n) for n in tick.split(',')] for tick in [my_ticket] + valid_nearby_tickets]
vals_per_position = [[t[i] for t in valid_ticket_lists] for i in range(20)]


def determine_fields(rules_dict, vals_per_position):
    position_viable_rules = []
    for i in range(20):
        viable_rules = []
        for rule in rules_dict.keys():
            if all(n in rules_dict[rule] for n in vals_per_position[i]):
                viable_rules.append(rule)
        position_viable_rules.append(viable_rules)

    fixed_rules = []
    while max(len(x) for x in position_viable_rules) > 1:
        onerule_ind = [i for i in range(20) if len(position_viable_rules[i]) == 1 and i not in fixed_rules][0]
        onerule_rule = position_viable_rules[onerule_ind][0]
        fixed_rules.append(onerule_ind)
        for j in range(20):
            if j not in fixed_rules:
                if onerule_rule in position_viable_rules[j]:
                    position_viable_rules[j].remove(onerule_rule)
    return [x[0] for x in position_viable_rules]


fieldslist = determine_fields(rules_dict, vals_per_position)
myticketnums = [int(n) for n in my_ticket.split(',')]
prod = 1
for i in range(20):
    if 'departure' in fieldslist[i]:
        prod *= myticketnums[i]
print(prod)
