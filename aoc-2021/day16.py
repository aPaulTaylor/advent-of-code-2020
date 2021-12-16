from operator import mul
from functools import reduce

with open('input/day16-input.txt', 'r') as f:
    packet = f.readlines()[0].strip()

packet='0'+bin(int(packet,16))[2:]

def parse_packet_full(pkt):
    type_funcs={'000':sum, '001':(lambda x: reduce(mul, x, 1)),
                '010':min, '011':max,
                '101':(lambda x:x[0]>x[1]),
                '110':(lambda x:x[0]<x[1]),
                '111': (lambda x: x[0]==x[1])
                }
    version = pkt[:3]
    type = pkt[3:6]
    total_version = int(version,2)
    if type == '100':
        i=11
        lit_val=''
        while pkt[i-5]=='1':
            lit_val += pkt[i-4:i]
            i+=5
        lit_val += pkt[i-4:i]
        return total_version, i, int(lit_val,2)
    else:
        len_type=pkt[6]
        i=7
        sbpkt_lit_vals=[]
        if len_type=='1': # 11 bits are number of subpackets
            num_subpackets = int(pkt[7:18],2)
            i=18
            for sp in range(num_subpackets):
                sbpkt_total_version, sbpkt_len, sbpkt_lit_val = parse_packet_full(pkt[i:])
                sbpkt_lit_vals.append(sbpkt_lit_val)
                total_version += sbpkt_total_version
                i+= sbpkt_len
        else: # 15 bits are length of subpackets
            subpacket_len = int(pkt[7:22],2)
            i=22
            while i<subpacket_len+22:
                sbpkt_total_version, sbpkt_len, sbpkt_lit_val = parse_packet_full(pkt[i:])
                sbpkt_lit_vals.append(sbpkt_lit_val)
                total_version += sbpkt_total_version
                i+= sbpkt_len
        pkt_val = type_funcs[type](sbpkt_lit_vals)
        return total_version, i, pkt_val

print(parse_packet_full(packet))