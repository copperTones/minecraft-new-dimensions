from json import load, dump
from os import walk
from os.path import join

def addP(p, k, v):
    if k in p:
        p[k] |= {v}
    else:
        p[k] = {v}
                
bs = join('tmp', 'blockstates')
states = {}
for fn in next(walk(bs))[2]: # file names in folder
    print(fn, end=' ')
    with open(join(bs, fn), 'r') as f:
        d = load(f)
    p = {}
    if 'variants' in d:
        for s in d['variants']: # 'key1=val1,key2=val2': ...
            if s == '':
                continue
            s = s.split(',')
            for kv in s:
                addP(p, *kv.split('='))
    elif 'multipart' in d:
        for o in d['multipart']: # {'key1': 'val1', 'key2': 'val2' ...}
            if 'when' in o:
                o = o['when']
                if 'OR' in o:
                    for o2 in o['OR']:
                        for k, v in o2.items():
                            addP(p, k, v)
                else:
                    for k, v in o.items():
                        addP(p, k, v)
    else:
        print(d.keys())
        quit()
    states[fn[:-4]] = {k: list(v) for k,v in p.items()}
    print(p)

with open('tmp/raw_blockstates.json', 'w') as f:
    dump(states, f)
