with open('/aoc-2020/day21-input.txt', 'r') as f:
    input = f.readlines()

ingredients = [x.split('(')[0].strip().split(' ') for x in input]
allergens = [x.split('(contains ')[1].strip().replace(')','').split(', ') for x in input]

all_allergens=set().union(*allergens)
all_ingredients=set().union(*ingredients)
allergen_candidates={}
for a in all_allergens:
    foodstuffs_with_allergen = [ingredients[i] for i in range(len(ingredients)) if a in allergens[i]]
    poss_ingreds = all_ingredients.intersection(*foodstuffs_with_allergen)
    allergen_candidates[a] = poss_ingreds

allergen_containing_ingredients = set().union(*allergen_candidates.values())

# Part 1
total=0
for ing in all_ingredients:
    if ing not in allergen_containing_ingredients:
        total += sum(ing in x for x in ingredients)
print(total)

# Part 2 easily solved from this output
for a in all_allergens:
    print(a)
    print(allergen_candidates[a])
