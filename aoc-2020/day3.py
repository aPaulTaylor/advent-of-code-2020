with open('/aoc-2020/day3-input.txt', 'r') as f:
    puzzle_input = f.readlines()

puzzle_input = [x.strip() for x in puzzle_input]
trees = [[int(x == '#') for x in input_line] for input_line in puzzle_input]


def traverse_trees(trees, ac, dn):
    x_pos = 0
    num_trees = 0
    num_cols = len(trees[0])
    for y_pos in range(0, len(trees), dn):
        num_trees += trees[y_pos][x_pos]
        x_pos = (x_pos + ac) % num_cols
    return num_trees


tree_nums = []
prod = 1
for slope in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    tree_nums.append(traverse_trees(trees, *slope))
    prod *= tree_nums[-1]

print(tree_nums)
print(prod)
