with open('input/day06-input.txt', 'r') as f:
    buffer = f.readlines()[0].strip()

print([min(i for i in range(4, len(buffer)) if len(set(buffer[i - d:i])) == d) for d in [4, 14]])