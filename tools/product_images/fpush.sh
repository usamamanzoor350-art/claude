#!/bin/bash
# usage: fpush.sh age -> copy finger images to repo, commit, push, print fileUpdate payload
S=/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad;F=/root/.claude/projects/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/tool-results/mcp-Shopify-graphql_query-1792605998136.txt
a=$1;cd /home/user/claude && mkdir -p product_images/finger$a && cp $S/f$a/sq/fing${a}_*_sq.jpg product_images/finger$a/ && git add product_images/finger$a previews/finger_$a.jpg && git commit -qm "Add Finger images for age $a from new blank photos

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01RFXLDoCFapJK3Pt9AUoro2" && git push -q origin claude/confident-newton-nzy6u0 && C=$(git rev-parse HEAD) && python3 - <<P
import json
a=$a;n=a-1
def o(k): return str(k)+('th' if 10<=k%100<=20 else {1:'st',2:'nd',3:'rd'}.get(k%10,'th'))
d=json.load(open('$F'))['data']['products']['nodes'];p=[p for p in d if p['title'].startswith(f'I Am {n} +')][0]
ms=[m['id'] for m in p['media']['nodes']];assert len(ms)==8
base=f"I Am {n} + Middle Finger - Funny {o(a)} Birthday T-Shirt for Women - "
L=[('black','Black Round Neck'),('white','White V-Neck'),('pink','Blush Pink V-Neck'),('sage','Sage Green Round Neck'),('burgundy','Burgundy Round Neck'),('navy','Navy Blue V-Neck'),('flatlay','Flat Lay')]
f=[{'id':ms[i],'alt':base+t,'originalSource':f'https://raw.githubusercontent.com/usamamanzoor350-art/claude/$C/product_images/finger{a}/fing{a}_{i+1}_{c}_sq.jpg'} for i,(c,t) in enumerate(L)]
print(json.dumps({'files':f},separators=(',',':')))
P
