import cv2,numpy as np,json,sys,shutil,os
from necc2 import skin_center
from necc import neck_center
for d in sys.argv[1:]:
    if not os.path.exists(f'{d}/geo_orig.json'): shutil.copy(f'{d}/geo.json',f'{d}/geo_orig.json')
    G=json.load(open(f'{d}/geo_orig.json'))
    for c,g in G.items():
        r=neck_center(d,c,g) if c=='pink' else skin_center(d,g)
        r=[a for a,w in r]
        if r:
            n=float(np.median(r));print(d,c,g['cx'],'->',round(n));g['cx']=n
        else: print(d,c,'NO NECK')
    json.dump(G,open(f'{d}/geo.json','w'))
