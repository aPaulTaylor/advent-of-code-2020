import re

with open('c:/Users/paula/PycharmProjects/advent-of-code/day19-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

rules = input[:139]
words = input[140:]

ab_rules = [r for r in rules if '"' in r]
num_rules = [r for r in rules if '"' not in r]

def parse_num_rule(nr):
    rule_num = nr.split(': ')[0]
    subrules = nr.split(': ')[1].split(' | ')
    return [rule_num,[sr.split(' ') for sr in subrules]]

resolved_rules = { r.split(': ')[0]:[r.split(': ')[1].replace('"','')] for r in ab_rules}
unresolved_rules = dict([parse_num_rule(nr) for nr in num_rules])

def resolve_rule(rule): #4:[[1,55,6],[22,3]]   1=[abbbab,bbbab]
    resolved_rule=[]
    for rule_option in rule:
        option_resolutions=['']
        for term in rule_option:
            term_words = resolved_rules[term]
            new_option_resolutions=[]
            for opt in option_resolutions:
                for tw in term_words:
                    new_option_resolutions.append(opt+tw)
            option_resolutions = new_option_resolutions
        resolved_rule.extend(option_resolutions)
    return resolved_rule

def is_resolvable(rule):
    return all( all(n in resolved_rules.keys() for n in rule_opt) for rule_opt in rule )

rule_resolved=True
while rule_resolved:
    to_resolve = [n for n,r in unresolved_rules.items() if is_resolvable(r)]
    print(f'resolving {len(to_resolve)} rules...')
    if len(to_resolve)==0:
        rule_resolved=False
    for n in to_resolve:
        resolved_rules[n] = resolve_rule(unresolved_rules[n])
        del unresolved_rules[n]



