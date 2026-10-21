import cv2,numpy as np,json,sys
from scipy import ndimage as nd
d=sys.argv[1];G=json.load(open(f'{d}/geo.json'))
def skinm(a):
    g=a.astype(int);return ((g[...,2]-g[...,0])>30)&((g[...,1]-g[...,0])>5)&(g[...,2]>110)
res={}
for c,g in G.items():
    a=cv2.imread(f'{d}/'+g['file']);H,W=a.shape[:2]
    lab=cv2.cvtColor(cv2.GaussianBlur(a,(0,0),2),cv2.COLOR_BGR2LAB).astype(np.float32)
    # shirt colour: mode inside a central lower-chest window (square image sits at rows 140..1262)
    win=lab[140+int(1122*.55):140+int(1122*.68),int(W*.40):int(W*.60)].reshape(-1,3)
    q=(win//5).astype(int);k=q[:,0]*10000+q[:,1]*100+q[:,2];v,cn=np.unique(k,return_counts=True)
    ref=win[k==v[np.argmax(cn)]].mean(0)
    wts=np.array([0.35,1.5,1.5]) if ref[0]<220 else np.array([0.8,1.3,1.3])
    dist=np.sqrt((((lab-ref)*wts)**2).sum(-1));thr=20 if ref[0]<220 else 12
    sh=(dist<thr)&~skinm(a)
    sh=nd.binary_opening(sh,iterations=2);l,n=nd.label(sh);sz=nd.sum(sh,l,range(1,n+1));sh=l==1+np.argmax(sz)
    shf=nd.binary_fill_holes(nd.binary_closing(sh,iterations=6))
    ys,xs=np.where(shf);top=ys.min();bot=ys.max()
    # centre column from mid-torso
    rows=range(top+int(0.30*(bot-top)),top+int(0.70*(bot-top)),4)
    Ls=[];Rs=[]
    for y in rows:
        xx=np.where(shf[y])[0]
        if len(xx)==0: continue
        runs=np.split(xx,np.where(np.diff(xx)>3)[0]+1);r=max(runs,key=len);Ls.append(r[0]);Rs.append(r[-1])
    Wd=np.array(Rs)-np.array(Ls);k=np.argsort(Wd)[:max(3,len(Wd)//3)]
    L=float(np.median(np.array(Ls)[k]));R=float(np.median(np.array(Rs)[k]));cx=(L+R)/2
    # neckline: first shirt row at centre column (bottom of collar opening)
    col=shf[:,int(cx)-4:int(cx)+5].all(1);cy=np.where(col)[0];ny=int(cy[0]) if len(cy) else top
    # hem: last row where shirt run is wide
    hem=bot
    for y in range(bot,ny,-1):
        xx=np.where(shf[y])[0]
        if len(xx)>0.6*(R-L): hem=y;break
    res[c]=dict(L=L,R=R,cx=cx,bw=R-L,ny=ny,hem=int(hem))
# same model + framing per age: use median width, but each photo's own centre/neck
bwm=float(np.median([r['bw'] for r in res.values()]))
for c,g in G.items():
    r=res[c]
    if abs(r['bw']-bwm)>0.12*bwm: r['bw']=bwm;r['L']=r['cx']-bwm/2;r['R']=r['cx']+bwm/2
    g.update(r);g['maxbottom']=r['hem']-35
    a=cv2.imread(f'{d}/'+g['file']);sk=cv2.dilate(skinm(a).astype(np.uint8),np.ones((7,7),np.uint8))>0
    m=np.zeros(a.shape[:2],np.uint8);m[g['ny']-5:g['hem']-8,int(g['L'])-25:int(g['R'])+25]=1;m[sk]=0;cv2.imwrite(f"{d}/{g['mask']}",m*255)
json.dump(G,open(f'{d}/geo.json','w'))
print(d,{c:(int(g['cx']),int(g['bw']),g['ny'],g['hem']) for c,g in G.items()})
