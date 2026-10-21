import cv2,numpy as np,glob,os,collections
S='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/'
SC=0.32
PAL=np.array([[128,178,198],[72,96,168],[120,192,240],[168,192,144],[72,192,192]],np.float32)  # BGR: tan Vintage, rose, peach, sage, olive
orig={}
for f in glob.glob(S+'png_vint/*/*.png'):
    y=int(os.path.basename(f)[:4]);a=cv2.imread(f,cv2.IMREAD_UNCHANGED);orig[y]=cv2.resize(a,None,fx=SC,fy=SC,interpolation=cv2.INTER_AREA)
H,W=next(iter(orig.values())).shape[:2]
def classify(a):
    al=a[...,3];d=((a[...,:3].astype(np.float32)[...,None,:]-PAL)**2).sum(-1);cl=d.argmin(-1)
    cl[al==0]=-1
    # spread labels of solid pixels to soft edge pixels
    solid=al>150;lab=np.where(solid,cl,-1)
    for k in range(5):
        m=(lab==k).astype(np.uint8);dm=cv2.dilate(m,np.ones((5,5),np.uint8))>0;fill=(lab==-1)&(al>0)&dm;lab[fill]=k
    return lab
info={};cents=[]
for y,a in orig.items():
    lab=classify(a);info[y]=lab
    cents.append([np.median(np.where(lab==k)[1]) for k in range(1,5)])
cent=np.median(cents,0);print('slot centers',cent)
glyph=collections.defaultdict(list)
for y,a in orig.items():
    lab=info[y]
    for k,d in enumerate(str(y)):
        m=lab==k+1;al=np.where(m,a[...,3],0);ys,xs=np.where(al>0)
        g=al[ys.min():ys.max()+1,xs.min():xs.max()+1]
        glyph[d].append((k,g,ys.min()))
T=1986;lt=info[T];a_t=orig[T]
tb=[]
for k in range(4):
    ys,xs=np.where(lt==k+1);tb.append((xs.min(),xs.max(),ys.min(),ys.max()))
Ht=int(np.median([b[3]-b[2] for b in tb]));Bt=int(np.median([b[3] for b in tb]))
G=np.mean([tb[k+1][0]-tb[k][1] for k in range(3)])
vys,vxs=np.where(lt==0);Vc=(vxs.min()+vxs.max())/2
vint=a_t.copy();vint[lt!=0]=0
def pick(d,k):
    v=glyph[d];hm=np.median([g.shape[0] for _,g,_ in v]);ar=np.median([g.shape[1]/g.shape[0] for _,g,_ in v])
    ok=[(kk,g) for kk,g,_ in v if abs(g.shape[0]-hm)<0.06*hm and abs(g.shape[1]/g.shape[0]-ar)<0.08*ar]
    ok.sort(key=lambda t:(t[0]!=k,abs(t[1].shape[0]-hm)))
    g=ok[0][1];s_=Ht/g.shape[0];return cv2.resize(g,(max(1,int(g.shape[1]*s_)),Ht),interpolation=cv2.INTER_AREA)
def build(year):
    if year in orig: return orig[year]
    gs=[pick(d,k) for k,d in enumerate(str(year))]
    tot=sum(g.shape[1] for g in gs)+3*G;x=Vc-tot/2
    P=300;out=np.zeros((H,W+2*P,4),np.uint8);out[:,P:P+W]=vint;x+=P
    for k,g in enumerate(gs):
        h,w=g.shape;xi=int(round(x));yt=Bt-h;reg=out[yt:yt+h,xi:xi+w];m=g>reg[...,3]
        reg[...,:3][m]=PAL[k+1].astype(np.uint8);reg[...,3][m]=g[m];x+=w+G
    xs=np.where(out[...,3].max(0)>0)[0];return out[:,xs[0]:xs[-1]+1]
os.makedirs(S+'designs/vintage_z',exist_ok=True)
for age in range(30,81):
    d=build(2026-age)
    for ink in ('black','white'): cv2.imwrite(S+f'designs/vintage_z/{age}_{ink}.png',d)
print('done')
