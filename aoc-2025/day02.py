import math

input="18623-26004,226779-293422,65855-88510,868-1423,248115026-248337139,903911-926580,97-121,67636417-67796062,24-47,6968-10197,193-242,3769-5052,5140337-5233474,2894097247-2894150301,979582-1016336,502-646,9132195-9191022,266-378,58-91,736828-868857,622792-694076,6767592127-6767717303,2920-3656,8811329-8931031,107384-147042,941220-969217,3-17,360063-562672,7979763615-7979843972,1890-2660,23170346-23308802"

ranges=[[int(i) for i in x.split('-')] for x in input.split(',')]

invalid_id_sum=0

for r in ranges:
    for id in range(r[0],r[1]+1):
        id_str=str(id)
        if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
            invalid_id_sum += id

print(invalid_id_sum)

def check_rep(id,n):
    id_init = id[:n]
    num_reps = len(id)//n
    return id == id_init*num_reps

invalid_id_sum=0

for r in ranges:
    for id in range(r[0],r[1]+1):
        id_str=str(id)
        for n in range(1,len(id_str)):
            if check_rep(id_str,n):
                invalid_id_sum += id
                break

print(invalid_id_sum)

# non-string version

def check_rep_int(id,n):
    rep = id % (10**n)
    while True:
        id = id//(10**n)
        if id % (10**n) != rep:
            return False
        if id==rep:
            return True

invalid_id_sum=0

for r in ranges:
    for id in range(r[0],r[1]+1):
        num_len=2
        pow_ten=100
        while id>=pow_ten:
            num_len +=1
            pow_ten *=10
        if num_len % 2 == 0:
            if check_rep_int(id, num_len//2 ):
                invalid_id_sum += id


print(invalid_id_sum)

invalid_id_sum=0

for r in ranges:
    for id in range(r[0],r[1]+1):
        num_len=2
        pow_ten=100
        while id>=pow_ten:
            num_len +=1
            pow_ten *=10
        for rep_len in range(1,num_len):
            if num_len % rep_len==0:
                if check_rep_int(id, rep_len):
                    invalid_id_sum += id
                    break


print(invalid_id_sum)