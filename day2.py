with open('c:/Users/paula/PycharmProjects/advent-of-code/day2-input.txt', 'r') as f:
    puzzle_input = f.readlines()


def parse_input(input_line):
    iline_split = input_line.split(':')
    policy = iline_split[0].split(' ')
    return iline_split[1].strip(), policy[1], [int(x) for x in policy[0].split('-')]


def test_passwd(passwd, char, freq_range):
    return freq_range[0] <= sum(x == char for x in passwd) <= freq_range[1]


def test_passwd_pt2(passwd, char, indices):
    return (passwd[indices[0] - 1] == char) ^ (passwd[indices[1] - 1] == char)


print(sum(test_passwd(*parse_input(x)) for x in puzzle_input))

print(sum(test_passwd_pt2(*parse_input(x)) for x in puzzle_input))
