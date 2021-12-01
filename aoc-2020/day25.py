card_public_key = 13135480
door_public_key = 8821721

def find_loop_size(public_key,subj_num=7,modulus = 20201227):
    loop_size=0
    n = 1
    while n!= public_key:
        n *= subj_num
        n %= modulus
        loop_size += 1
    return loop_size

def transform(subj_num, loop_size, modulus = 20201227):
    n = 1
    for i in range(loop_size):
        n *= subj_num
        n %= modulus
    return n

print(transform(door_public_key,find_loop_size(card_public_key)))
print(transform(card_public_key,find_loop_size(door_public_key)))