import cv2,numpy as np,sys,json
sys.path.insert(0,'.')
import rmdesign as r1, rmdesign3 as r3
from scipy import ndimage as nd
def residual(o):
    # remaining print: strong local contrast blobs inside central chest box
    H,W=o.shape[:2];L=cv2.cvtColor(o,cv2.COLOR_BGR2LAB)[...,0].astype(np.float32)
    bg=cv2.medianBlur(L.astype(np.uint8),61).astype(np.float32);d=np.abs(L-bg)
    B=np.zeros((H,W),bool);B[int(H*.35):int(H*.72),int(W*.30):int(W*.70)]=True
    g=o.astype(int);skin=((g[...,2]-g[...,0])>30)&((g[...,1]-g[...,0])>5)&(g[...,2]>110)
    m=(d>30)&B&~skin;m=nd.binary_opening(m,iterations=1);return m.mean()*100
a=int(sys.argv[1]);got=json.load(open(f'hv{a}/colors.json'));rep={}
for c,k in got.items():
    x=cv2.imread(f'hv{a}/raw{k}.png');x=cv2.resize(x,(1122,1122),interpolation=cv2.INTER_AREA)
    _,m1=r1.clean(x);_,m3=r3.clean(x)
    cands={'v1':m1,'v3':m3,'u':cv2.bitwise_or(m1,m3)}
    best=None
    for n,M in cands.items():
        area=(M>0).mean()*100
        if area>14: continue
        o=cv2.inpaint(x,M,11,cv2.INPAINT_TELEA);r=residual(o);score=r*10+area*0.15
        if best is None or score<best[0]: best=(score,n,o,area,r)
    if best is None: best=(0,'none',x,0,residual(x))
    rep[c]=(best[1],round(best[3],1),round(best[4],2))
    o=best[2];p=np.zeros((1402,1122,3),np.uint8);p[:]=np.median(o[:10].reshape(-1,3),0);p[140:1262]=o
    cv2.imwrite(f'hv{a}/src_{c}_p.png',p)
print(a,rep)
