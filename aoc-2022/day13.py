from functools import cmp_to_key

with open('input/day13-input.txt', 'r') as f:
    lines_in=f.readlines()
    packets = [
        [eval(x.strip()) for x in lines_in[0::3]],
        [eval(x.strip()) for x in lines_in[1::3]]
    ]

def compare_packets(pl,pr):
    for i in range(min(len(pl),len(pr))):
        if type(pl[i]) is int and type(pr[i]) is int:
            if pl[i]<pr[i]:
                return 1
            elif pl[i]>pr[i]:
                return -1
        elif type(pl[i]) is list and type(pr[i]) is list:
            subcomp = compare_packets(pl[i],pr[i])
            if subcomp is not None:
                return subcomp
        elif type(pl[i]) is list and type(pr[i]) is int:
            subcomp = compare_packets(pl[i],[pr[i]])
            if subcomp is not None:
                return subcomp
        elif type(pl[i]) is int and type(pr[i]) is list:
            subcomp = compare_packets([pl[i]],pr[i])
            if subcomp is not None:
                return subcomp
    if len(pl)==len(pr):
        return None
    else:
        return 1 if len(pl)<len(pr) else -1

print(sum(i+1 for i in range(len(packets[0])) if compare_packets(packets[0][i],packets[1][i])==1))

divider1=[[6]]
divider2=[[2]]
all_packets = packets[0]+packets[1]+[divider1]+[divider2]
all_packets.sort(reverse=True,key=cmp_to_key(compare_packets))
print((all_packets.index(divider1)+1)*(all_packets.index(divider2)+1))
