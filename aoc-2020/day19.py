import itertools

with open('/aoc-2020/day19-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

rules = input[:139]
words = input[140:]
ab_rules = [r for r in rules if '"' in r]
num_rules = [r for r in rules if '"' not in r]


def parse_num_rule(nr):
    rule_num = nr.split(': ')[0]
    subrules = nr.split(': ')[1].split(' | ')
    return [rule_num, [sr.split(' ') for sr in subrules]]


resolved_rules = {r.split(': ')[0]: [r.split(': ')[1].replace('"', '')] for r in ab_rules}
unresolved_rules = dict([parse_num_rule(nr) for nr in num_rules])


def resolve_rule(rule):
    resolved_rule = []
    for rule_option in rule:
        option_resolutions = ['']
        for term in rule_option:
            term_words = resolved_rules[term]
            option_resolutions = [''.join(p) for p in itertools.product(option_resolutions, term_words)]
        resolved_rule.extend(option_resolutions)
    return resolved_rule


def is_resolvable(rule):
    return all(all(n in resolved_rules.keys() for n in rule_opt) for rule_opt in rule)


rule_resolved = True
while rule_resolved:
    to_resolve = [n for n, r in unresolved_rules.items() if is_resolvable(r)]
    if len(to_resolve) == 0:
        rule_resolved = False
    for n in to_resolve:
        resolved_rules[n] = resolve_rule(unresolved_rules[n])
        del unresolved_rules[n]

print(sum(w in resolved_rules['0'] for w in words))


def matches_new_rule0(word):
    matching_rule42 = True
    sub_42_uses = 0
    sub_31_uses = 0
    for i in range(0, len(word), 8):
        if word[i:i + 8] in resolved_rules['42'] and matching_rule42:
            sub_42_uses += 1
        elif word[i:i + 8] in resolved_rules['31']:
            matching_rule42 = False
            sub_31_uses += 1
        else:
            return False
    if sub_31_uses >= sub_42_uses or sub_31_uses == 0:
        return False
    return True


print(sum(matches_new_rule0(w) for w in words))
