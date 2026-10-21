#!/bin/bash
d=$1;cd $d;[ -f geo_old.json ] || cp geo.json geo_old.json
arg=$(python3 -c "
import json;G=json.load(open('geo_old.json'));print(json.dumps([[g['file'],c,g['neck']] for c,g in G.items()]))")
python3 ../geo2.py "$arg" >/dev/null 2>&1
python3 - <<'P'
import json,numpy as np
G=json.load(open('geo.json'))
hs=[g['hem'] for c,g in G.items() if g['hem']<1300]
for c,g in G.items():
    if g['hem']>=1300 or g['hem']-g['ny']<350:
        g['hem']=int(np.median(hs)) if hs else 1060;g['maxbottom']=g['hem']-35
json.dump(G,open('geo.json','w'))
print({c:(g['ny'],g['L'],g['R'],g['cx'],g['hem']) for c,g in G.items()})
P
