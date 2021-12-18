with open('input/day18-input.txt', 'r') as f:
    s_sums = [x.strip() for x in f.readlines()]

s_sums = [[n for n in ss if not n==','] for ss in s_sums]

def reduce_ssum(s_sum):
    reduced=True
    while reduced:
         reduced=False
         nest_level = 0
         for i in range(len(s_sum)):
             if s_sum[i] == '[':
                 nest_level += 1
             if s_sum[i] == ']':
                 nest_level -= 1
             if nest_level == 5:
                 reduced=True
                 for j in range(i - 1, -1, -1):
                     if s_sum[j] not in '[]':
                         s_sum[j] = str(int(s_sum[j]) + int(s_sum[i + 1]))
                         break
                 for j in range(i + 3, len(s_sum)):
                     if s_sum[j] not in '[]':
                         s_sum[j] = str(int(s_sum[j]) + int(s_sum[i + 2]))
                         break
                 s_sum = s_sum[:i] +['0']+ s_sum[i + 4:]
                 break
         if nest_level < 5:
             for i in range(len(s_sum)):
                  if s_sum[i] not in '[]':
                       if int(s_sum[i])>9:
                         reduced=True
                         s_sum = s_sum[:i]+['[',str(int(s_sum[i])//2),str(int(s_sum[i])//2 + int(s_sum[i])%2),']']+s_sum[i+1:]
                         break
    return s_sum

def get_mag(s_sum):
     while '[' in s_sum:
          for i in range(len(s_sum)):
               if s_sum[i] not in '[]' and s_sum[i+1] not in '[]':
                    s_sum = s_sum[:i-1] + [str(3*int(s_sum[i]) + 2*int(s_sum[i+1]))] + s_sum[i+3:]
                    break
     return int(s_sum[0])

s_sum = reduce_ssum(['['] + s_sums[0] + s_sums[1] + [']'])
for nss in s_sums[2:]:
     s_sum = reduce_ssum(['['] + s_sum + nss + [']'])

print(get_mag(s_sum))

max_mag=0
for i in range(len(s_sums)):
     for j in range(len(s_sums)):
          if not i==j:
               max_mag=max(max_mag,get_mag(reduce_ssum(['[']+s_sums[i]+s_sums[j]+[']'])))
print(max_mag)