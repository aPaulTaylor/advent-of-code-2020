with open('input/day08-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

input = [x.split(' | ') for x in input]
input = [[x[0].split(' '),x[1].split(' ')] for x in input]

print( sum( sum(len(x) in [2,3,4,7] for x in l[1] ) for l in input) )

def num_common_segs(a,b):
    return sum(x in b for x in a)

def process_digits(digits):
    digits_sorted = sorted(digits,key=len)
    digits_sorted = [''.join(sorted(x)) for x in digits_sorted]
    digits_dict= {digits_sorted[0]: 1, digits_sorted[1]: 7, digits_sorted[2]: 4, digits_sorted[9]: 8}
    signature = [digits_sorted[i] for i in [0,2,1,9]]
    sigs = {(2,3,3,6):0, (1,2,2,5):2, (2,3,3,5):3, (1,3,2,5):5, (1,3,2,6):6, (2,4,3,6):9}
    for d in digits_sorted:
        if d not in digits_dict:
            digit_sig=tuple((num_common_segs(d,x) for x in signature))
            digits_dict[d]=sigs[digit_sig]
    return digits_dict

output_sum=0
tens=[1000,100,10,1]
for input_line in input:
    line_dict=process_digits(input_line[0])
    decoded_digits=[line_dict[''.join(sorted(i))] for i in input_line[1]]
    output_sum += sum(decoded_digits[i]*tens[i] for i in range(4))
print(output_sum)