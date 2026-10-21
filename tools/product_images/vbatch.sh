#!/bin/bash
# usage: vbatch.sh dir age
S=/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad
d=$1;a=$2;cd $S/$d
cp $S/make_age_v5.py make_age.py; cp $S/flat_v4.py flat.py; cp $S/h38/square.py $S/h38/place.py . 2>/dev/null
[ -f src_1293.png ] || cp $S/h38/src_1293.png $S/h38/fmask_*.png $S/h38/geo5.json .
# sage-safe skin mask (warm skin only)
python3 - <<'P'
import json,cv2,numpy as np
G=json.load(open('geo.json'))
for c,g in G.items():
    a=cv2.imread(g['file']).astype(int)
    sk=((a[...,2]-a[...,0])>30)&((a[...,1]-a[...,0])>5)&(a[...,2]>110)
    lab=cv2.cvtColor(cv2.GaussianBlur(cv2.imread(g['file']),(0,0),2),cv2.COLOR_BGR2LAB).astype(np.float32)
    y=g['ny']+int(0.6*(g['hem']-g['ny']));x=int(g['cx'])
    ref=np.median(lab[y-30:y+30,x-40:x+40].reshape(-1,3),0)
    shirtlike=np.sqrt((((lab-ref)*[0.25,1.5,1.5])**2).sum(-1))<16
    sk&=~shirtlike
    sk=cv2.dilate(sk.astype(np.uint8),np.ones((7,7),np.uint8))>0
    m=np.zeros(a.shape[:2],np.uint8);m[g['ny']-5:g['hem']-8,int(g['L'])-25:int(g['R'])+25]=1;m[sk]=0;cv2.imwrite(g['mask'],m*255)
P
python3 make_age.py vintage_e $a vint$a | tr '\n' ' '
python3 flat.py vintage_e $a vint$a 165 >/dev/null
python3 square.py vint$a >/dev/null 2>&1
echo
