with open('input/day13-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

dots=[]
folds=[]
for l in input:
   if len(l)>0 and l[0]=='f':
      eq=l.split(' ')[-1].split('=')
      folds.append((eq[0],int(eq[1])))
   if ',' in l:
      dots.append(tuple([int(x) for x in l.split(',')]))

def do_fold(dot,fold):
   if fold[0]=='x':
      return (dot[0] if dot[0]<=fold[1] else 2*fold[1]-dot[0], dot[1])
   else:
      return (dot[0], dot[1] if dot[1]<=fold[1] else 2*fold[1]-dot[1])

print(len(set([do_fold(dot,folds[0]) for dot in dots])))

for fold in folds:
   dots=[do_fold(dot,fold) for dot in dots]

for i in range(6):
   pl=''
   for j in range(39):
      pl=pl+('#' if (j,i) in dots else '.')
   print(pl)