import cv2,numpy as np
S='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/'
def alpha(f):
    a=cv2.imread(f,cv2.IMREAD_UNCHANGED)[...,3];ys,xs=np.where(a>10)
    return a[max(0,ys.min()-20):ys.max()+21,max(0,xs.min()-20):xs.max()+21].copy()
def comps(a):
    n,lab,st,_=cv2.connectedComponentsWithStats((a>100).astype(np.uint8),8)
    return lab,[dict(i=i,x=st[i,0],y=st[i,1],w=st[i,2],h=st[i,3],area=st[i,4]) for i in range(1,n) if st[i,4]>30]
def classify(a):
    lab,C=comps(a);H=a.shape[0]
    # word letters: tallest group of components in the middle band
    cand=[c for c in C if c['y']>0.25*H]
    cap=np.median(sorted([c['h'] for c in cand],reverse=True)[:5])
    letters=[c for c in cand if abs(c['h']-cap)<0.2*cap]
    yW=int(np.median([c['y'] for c in letters]))
    word=[c for c in C if c['y']>=yW-0.15*cap and c['y']+c['h']<=yW+1.25*cap]
    est=[c for c in C if c['y']>yW+1.0*cap]
    hello=[c for c in C if c not in word and c not in est]
    return lab,sorted(letters,key=lambda c:c['x']),word,est,hello,cap,yW
def mask_of(lab,cs,shape):
    m=np.zeros(shape,bool)
    for c in cs: m|=lab==c['i']
    return m
# THIRTY strip from the Thirty design
T=alpha('/home/user/claude/hello_png/Hello Thirty Black Png.png')
labT,LT,_,_,_,capT,yT=classify(T)
assert len(LT)>=6,len(LT)
six=LT[:6];m6=mask_of(labT,six,T.shape)
x0=min(c['x'] for c in six);x1=max(c['x']+c['w'] for c in six);y0=min(c['y'] for c in six);y1=max(c['y']+c['h'] for c in six)
THIRTY=(T*m6)[y0:y1,x0:x1];THIRTY_cap=capT
# digit glyph library from 40-49 EST lines
DIG={}
for age in range(40,50):
    a=alpha(S+f'designs/hello_orig/{age}_black.png');lab,L,W,E,Hh,cap,yW=classify(a)
    E=sorted(E,key=lambda c:c['x']);yr=str(2026-age)
    for c,d in zip(E[-4:],yr):
        if d not in DIG: g=(a*(lab==c['i']))[c['y']:c['y']+c['h'],c['x']:c['x']+c['w']];DIG[d]=g
def build(n):
    a=alpha(S+f'designs/hello_orig/4{n}_black.png');lab,L,W,E,Hh,cap,yW=classify(a)
    forty=L[:5];fx0=min(c['x'] for c in forty);fx1=max(c['x']+c['w'] for c in forty);fy0=min(c['y'] for c in forty)
    fcap=np.median([c['h'] for c in forty])
    sc=fcap/THIRTY_cap;th=cv2.resize(THIRTY,(int(THIRTY.shape[1]*sc),int(THIRTY.shape[0]*sc)),interpolation=cv2.INTER_AREA)
    delta=th.shape[1]-(fx1-fx0)
    H,Wd=a.shape;out=np.zeros((H,Wd+delta+10),np.uint8)
    keep=mask_of(lab,Hh,a.shape);out[:,:Wd]=np.where(keep,a,0)
    rest=[c for c in W if c not in forty]+E
    for c in rest:
        g=a*(lab==c['i']);sl=g[c['y']:c['y']+c['h'],c['x']:c['x']+c['w']]
        X=c['x']+delta;out[c['y']:c['y']+c['h'],X:X+c['w']]=np.maximum(out[c['y']:c['y']+c['h'],X:X+c['w']],sl)
    out[fy0:fy0+th.shape[0],fx0:fx0+th.shape[1]]=np.maximum(out[fy0:fy0+th.shape[0],fx0:fx0+th.shape[1]],th)
    # year: replace third digit (d -> d+1)
    E=sorted(E,key=lambda c:c['x']);yr_old=str(2026-(40+n));yr_new=str(2026-(30+n))
    c3=E[-2];c4=E[-1];X3=c3['x']+delta
    out[c3['y']:c3['y']+c3['h'],X3:X3+c3['w']]=0
    g=DIG[yr_new[2]];g=cv2.resize(g,(int(g.shape[1]*c3['h']/g.shape[0]),c3['h']),interpolation=cv2.INTER_AREA)
    dx=g.shape[1]-c3['w']
    if dx:  # move last digit to keep spacing
        X4=c4['x']+delta;last=out[c4['y']:c4['y']+c4['h'],X4:X4+c4['w']].copy();out[c4['y']:c4['y']+c4['h'],X4:X4+c4['w']]=0
        out[c4['y']:c4['y']+c4['h'],X4+dx:X4+dx+c4['w']]=last
    out[c3['y']:c3['y']+c3['h'],X3:X3+g.shape[1]]=np.maximum(out[c3['y']:c3['y']+c3['h'],X3:X3+g.shape[1]],g)
    assert yr_old[3]==yr_new[3]
    return out
for n in range(1,10):
    o=build(n)
    for ink,v in (('black',0),('white',255)):
        r=np.zeros((*o.shape,4),np.uint8);r[...,:3]=v;r[...,3]=o
        cv2.imwrite(S+f'designs/hello_orig/3{n}_{ink}.png',r)
# 30 = original Thirty file
for ink,src in (('black','Black'),('white','White')):
    d=cv2.imread(f'/home/user/claude/hello_png/Hello Thirty {src} Png.png',cv2.IMREAD_UNCHANGED);cv2.imwrite(S+f'designs/hello_orig/30_{ink}.png',d)
print('ok')
