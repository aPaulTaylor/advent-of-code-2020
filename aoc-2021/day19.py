with open('input/day19-input.txt', 'r') as f:
    scanners_text = [x.strip() for x in f.readlines()]

scanners = []
for sl in scanners_text:
    if '---' in sl:
        scanner={'beacons':[]}
    if ',' in sl:
        scanner['beacons'].append(tuple([int(n) for n in sl.split(',')]))
    if sl=='':
        scanners.append(scanner)

scanners[0]['pos']=(0,0,0)
scanners[0]['orient']=0
scanners[0]['beacons_reorient']=scanners[0]['beacons'][:]

transforms = [
    lambda x,y,z: (x,y,z),
    lambda x,y,z: (x,-z,y),
    lambda x, y, z: (x,-y,-z),
    lambda x, y, z: (x,z,-y),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (y,x,-z),
    lambda x, y, z: (-z,x,-y),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-y,-x,-z),
    lambda x, y, z: (-z,-x,y),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-y,-z,x),
    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (y, -z, -x),
]

def compare_scanners(si,sj):
    for o in range(24):
        for bi in si['beacons_reorient']:
            for bj in sj['beacons']:
                bj_reorient = transforms[o](*bj)
                j_to_i_shift = tuple([bi[n]-bj_reorient[n] for n in range(3)])
                sjb = [ tuple(transforms[o](*b)[n] + j_to_i_shift[n] for n in range(3))  for b in sj['beacons']]
                if len([s for s in si['beacons_reorient'] if s in sjb])>11:
                    return [o,j_to_i_shift]

for t in range(40):
    for si in [s for s in scanners if 'beacons_reorient' in s and 'checked' not in s]:
        for sj in [s for s in scanners if 'beacons_reorient' not in s]:
            compare = compare_scanners(si,sj)
            if compare:
                sj['beacons_reorient'] = [ tuple(transforms[compare[0]](*b)[n] + compare[1][n] for n in range(3))  for b in sj['beacons']]
                sj['pos']=compare[1]
        si['checked'] = True

all_beacons=[]
for s in scanners:
    all_beacons.extend(s['beacons_reorient'])
print(len(set(all_beacons)))

max_md=0
for si in scanners:
    for sj in scanners:
        mij = sum(abs(si['pos'][n]-sj['pos'][n]) for n in range(3))
        max_md = max(max_md,mij)
print(max_md)

