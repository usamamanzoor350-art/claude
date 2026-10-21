import json,sys,cv2,numpy as np
d=sys.argv[1];G=json.load(open(f'{d}/geo.json'))
ok=lambda g: 400<g['ny']<720 and 470<g['cx']<680 and g['hem']-g['ny']>320 and g['hem']<1240
good=[g for g in G.values() if ok(g)]
med={k:float(np.median([g[k] for g in good])) for k in ('cx','ny','hem','bw')}
def skinm(a):
    g=a.astype(int);return ((g[...,2]-g[...,0])>30)&((g[...,1]-g[...,0])>5)&(g[...,2]>110)
for c,g in G.items():
    fixed=[]
    if not (400<g['ny']<720): g['ny']=int(med['ny']);fixed.append('ny')
    if not (470<g['cx']<680): g['cx']=med['cx'];fixed.append('cx')
    if not (g['hem']-g['ny']>320 and g['hem']<1240): g['hem']=int(med['hem']);fixed.append('hem')
    if abs(g['bw']-med['bw'])>0.12*med['bw']: g['bw']=med['bw'];fixed.append('bw')
    g['L']=g['cx']-g['bw']/2;g['R']=g['cx']+g['bw']/2;g['maxbottom']=g['hem']-35
    a=cv2.imread(f'{d}/'+g['file']);sk=cv2.dilate(skinm(a).astype(np.uint8),np.ones((7,7),np.uint8))>0
    m=np.zeros(a.shape[:2],np.uint8);m[g['ny']-5:g['hem']-8,int(g['L'])-25:int(g['R'])+25]=1;m[sk]=0;cv2.imwrite(f"{d}/{g['mask']}",m*255)
    if fixed: print(d,c,fixed)
json.dump(G,open(f'{d}/geo.json','w'))
