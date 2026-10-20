import cv2,numpy as np
from scipy import ndimage as nd
def shirt_mask(im,seed,thr=16):
    lab=cv2.cvtColor(cv2.GaussianBlur(im,(0,0),2),cv2.COLOR_BGR2LAB).astype(np.float32)
    x,y=seed;ref=np.median(lab[y-30:y+30,x-30:x+30].reshape(-1,3),0)
    d=np.sqrt((((lab-ref)*np.array([0.25,1.5,1.5]))**2).sum(-1))
    m=(d<thr).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    lbl,n=nd.label(m);m=(lbl==lbl[y,x]).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((21,21),np.uint8));m=nd.binary_fill_holes(m).astype(np.uint8)
    return m
def geometry(m,cx):
    col=np.where(m[:,cx-3:cx+4].all(1))[0];neck=col[0]
    rows=np.where(m.any(1))[0];top,bot=rows[0],rows[-1]
    yr=int(top+0.32*(bot-top));xs=np.where(m[yr])[0]
    runs=np.split(xs,np.where(np.diff(xs)>1)[0]+1);r=min(runs,key=lambda r:abs((r[0]+r[-1])/2-cx))
    return neck,top,bot,r[0],r[-1]
def apply(im,m,design,cx,top_y,width,disp=1.0,opacity=0.96):
    lab=cv2.cvtColor(im,cv2.COLOR_BGR2LAB).astype(np.float32);L=lab[...,0]
    med=np.median(L[m>0]);lo=cv2.GaussianBlur(L,(0,0),3);hi=L-lo
    d=cv2.imread(design,cv2.IMREAD_UNCHANGED);ys,xs=np.where(d[...,3]>10);d=d[ys.min():ys.max()+1,xs.min():xs.max()+1]
    w=int(width);h=int(d.shape[0]*w/d.shape[1]);d=cv2.resize(d,(w,h),interpolation=cv2.INTER_AREA).astype(np.float32)
    H,Wd=im.shape[:2];can=np.zeros((H,Wd,4),np.float32);x0=int(cx-w/2);y0=int(top_y);can[y0:y0+h,x0:x0+w]=d
    lb=cv2.GaussianBlur(L,(0,0),14);gy,gx=np.gradient(lb);gx=np.clip(gx*0.6*disp,-2.5,2.5);gy=np.clip(gy*0.6*disp,-2.5,2.5)
    X,Y=np.meshgrid(np.arange(Wd),np.arange(H))
    can=cv2.remap(can,(X-gx).astype(np.float32),(Y-gy).astype(np.float32),cv2.INTER_LINEAR)
    mm=cv2.erode(m,np.ones((5,5),np.uint8)).astype(np.float32)
    pa=(can[...,3]/255*opacity*mm)[...,None]
    ref=max(med,40)
    shade=np.clip(1+(lo-med)/ref*(0.9 if med>120 else 0.5),0.6,1.12)[...,None]
    tex=(1+np.clip(hi,-12,12)[...,None]/255*1.5)
    ink=can[...,:3]*shade*tex
    out=im.astype(np.float32)*(1-pa)+ink*pa
    return np.clip(out,0,255).astype(np.uint8),(x0,y0,w,h)
