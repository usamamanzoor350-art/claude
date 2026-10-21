import cv2,numpy as np,sys,os,json
from scipy import ndimage as nd
from place import shirt_mask,apply
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/'
HELLO_W=0.53
FAC={'vintage_z':.63,'vintage_zd':.63,'hello':.76,'queen':.85,'finger':.71,'vintage_u':.82,'birthyear_u':.85}
IM=json.load(open('photos.json'))  # list of [file,color,neck]
ORDER=['black','white','pink','sage','burgundy','navy']
def geo(im,seed):
    lab=cv2.cvtColor(cv2.GaussianBlur(im,(0,0),2),cv2.COLOR_BGR2LAB).astype(np.float32)
    x,y=seed;ref=np.median(lab[y-25:y+25,x-25:x+25].reshape(-1,3),0)
    wt=np.array([0.5,1.5,1.5]) if ref[0]>215 else np.array([0.25,1.5,1.5]);thr=14 if ref[0]>215 else 16
    d=np.sqrt((((lab-ref)*wt)**2).sum(-1));m=(d<thr).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8));lbl,_=nd.label(m);m=(lbl==lbl[y,x]).astype(np.uint8)
    m=nd.binary_fill_holes(cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((21,21),np.uint8))).astype(np.uint8)
    col=np.where(m[:,x-6:x+7].all(1))[0];ny=col[0]
    mids=[];ws=[]
    for r in m[ny+100:ny+260]:
        xs=np.where(r)[0]
        if len(xs):
            runs=np.split(xs,np.where(np.diff(xs)>1)[0]+1);rr=min(runs,key=lambda q:abs((q[0]+q[-1])/2-x));mids.append((rr[0]+rr[-1])/2)
    r=m[ny+230];xs=np.where(r)[0];runs=np.split(xs,np.where(np.diff(xs)>1)[0]+1);rr=min(runs,key=lambda q:abs((q[0]+q[-1])/2-x))
    return m,ny,float(np.median(mids)),rr[-1]-rr[0]
if __name__=='__main__':
    des,age,tag=sys.argv[1],sys.argv[2],sys.argv[3]
    G=json.load(open('geo.json'))
    outs=[]
    for k,c in enumerate(ORDER,1):
        if c not in G: continue
        g=G[c];im=cv2.imread(g['file']);m=cv2.imread(g['mask'],0)//255
        ink='white' if c in('black','burgundy','navy') else 'black'
        s=g['bw']/330;w=FAC[des]*g['bw'];top=g['ny']+(45 if g['neck']=='v' else 72)*s
        if g.get('top'): top=g['top']
        f=f'{D}{des}/{age}_{ink}.png'
        if g.get('maxbottom'):
            a=cv2.imread(f,cv2.IMREAD_UNCHANGED)[...,3];ys,xs=np.where(a>10);ar=(ys.max()-ys.min())/(xs.max()-xs.min())
            w=min(w,(g['maxbottom']-top)/ar)
        cxa=g['cx']
        if des=='hello':
            import sys as _s;_s.path.insert(0,'..');from firstl import first_l
            from firstl import hello_info
            hf,hc=hello_info(f);w=HELLO_W*g['bw']/hf  # zip spec: 'hello' same size on every age, centered on the shirt
            if g.get('maxbottom'): w=min(w,(g['maxbottom']-top)/ar)
            # shrink until no ink is hidden by the mask (arms/skin/shirt edge): heart and year must stay whole
            da=cv2.imread(f,cv2.IMREAD_UNCHANGED)[...,3];ys,xs=np.where(da>10);da=da[ys.min():ys.max()+1,xs.min():xs.max()+1]
            mm=cv2.erode(m,np.ones((9,9),np.uint8))
            while True:
                cxa=g['cx']+(0.5-hc)*w;ww=int(w);hh=int(da.shape[0]*ww/da.shape[1]);x0=int(cxa-ww/2);y0=int(top)
                al=cv2.resize(da,(ww,hh))>15;cov=mm[y0:y0+hh,x0:x0+ww][al].mean()
                if cov>=0.9999 or w<0.45*g['bw']: break
                w*=0.98
            print(c,round(w),round(cov,4))
        if des!='hello':
            # keep the whole design on visible shirt fabric (arms, hands, hair)
            da=cv2.imread(f,cv2.IMREAD_UNCHANGED)[...,3];ys,xs=np.where(da>10);da=da[ys.min():ys.max()+1,xs.min():xs.max()+1]
            mm=cv2.erode(m,np.ones((9,9),np.uint8))
            while True:
                ww=int(w);hh=int(da.shape[0]*ww/da.shape[1]);x0=int(cxa-ww/2);y0=int(top)
                al=cv2.resize(da,(ww,hh))>15;cov=mm[y0:y0+hh,x0:x0+ww][al].mean()
                if cov>=0.9995 or w<0.45*g['bw']: break
                w*=0.98
            print(c,round(w),round(cov,4))
        o,_=apply(im,m,f,cxa,top,w)
        cv2.imwrite(f'final/{tag}_{k}_{c}.jpg',o,[cv2.IMWRITE_JPEG_QUALITY,94])
