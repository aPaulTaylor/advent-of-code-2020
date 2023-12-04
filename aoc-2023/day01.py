with open('input/day01-input.txt', 'r') as f:
    tb = [x.strip() for x in f.readlines()]

tb_digits = [[int(d) for d in x if d in '0123456789'] for x in tb]
print(sum([10 * t[0] + t[-1] for t in tb_digits]))

digit_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def line_to_digits(ln):
    line_digits = []
    for i in range(len(ln)):
        if ln[i] in '1234567890':
            line_digits.append(int(ln[i]))
        for j in range(len(digit_words)):
            if ln[i:i + len(digit_words[j])] == digit_words[j]:
                line_digits.append(j)
    return line_digits


tb_digits = [line_to_digits(x) for x in tb]
print(sum([10 * t[0] + t[-1] for t in tb_digits]))
