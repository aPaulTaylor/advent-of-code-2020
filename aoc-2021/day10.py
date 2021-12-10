with open('input/day10-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

def reduce_brackets(brackets):
    atoms = ['()','[]','{}','<>']
    has_atoms = any(x in brackets for x in atoms)
    while has_atoms:
        for atom in atoms:
            brackets = brackets.replace(atom,'')
        has_atoms = any(x in brackets for x in atoms)
    return brackets

total_score=0
values={')':3, ']':57, '}':1197, '>':25137}
for br in input:
    br = reduce_brackets(br)
    for ob in ['(','[','{','<']:
        br = br.replace(ob,'')
    if len(br)>0:
        total_score += values[br[0]]

print(total_score)

def get_score(brackets):
    scores = {'(':1, '[':2, '{':3, '<':4}
    brackets=reduce_brackets(brackets)
    if any(x in brackets for x in [')', ']', '}', '>']):
        return 0
    else:
        total_score = 0
        br_scores = [scores[x] for x in brackets[::-1]]
        for sc in br_scores:
            total_score = (total_score * 5) + sc
        return total_score

scores=[get_score(br) for br in input]
scores=[x for x in scores if x>0]
print(sorted(scores)[len(scores)//2])
