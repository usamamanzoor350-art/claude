import cv2,numpy as np
from scipy import ndimage as nd
def shirt_ref(a):
    H,W=a.shape[:2];lab=cv2.cvtColor(cv2.GaussianBlur(a,(0,0),1.5),cv2.COLOR_BGR2LAB).astype(np.float32)
    band=lab[int(H*.70):int(H*.80),int(W*.35):int(W*.65)].reshape(-1,3)
    q=(band//6).astype(int);k=q[:,0]*10000+q[:,1]*100+q[:,2];v,c=np.unique(k,return_counts=True)
    return lab,band[k==v[np.argmax(c)]].mean(0)
def clean(a):
    H,W=a.shape[:2];lab,ref=shirt_ref(a);dark=ref[0]<120
    d=np.sqrt((((lab-ref)*[0.35,1.4,1.4])**2).sum(-1));shirt=nd.binary_opening(d<20,iterations=2)
    l,n=nd.label(shirt);sz=nd.sum(shirt,l,range(1,n+1));shirt=l==1+np.argmax(sz)
    # region = shirt hull rows (span between shirt pixels on each row)
    R=np.zeros((H,W),bool)
    for y in range(H):
        xs=np.where(shirt[y])[0]
        if len(xs)>40: R[y,xs[0]+6:xs[-1]-6]=True
    B=np.zeros((H,W),bool);B[int(H*.20):int(H*.86),int(W*.10):int(W*.90)]=True;R&=B
    g=a.astype(int);skin=((g[...,2]-g[...,0])>30)&((g[...,1]-g[...,0])>5)&(g[...,2]>110)&(d>20)
    skin=cv2.dilate(nd.binary_opening(skin,iterations=2).astype(np.uint8),np.ones((5,5),np.uint8))>0
    out=a.copy();M=np.zeros((H,W),np.uint8)
    for it,(k,thr) in enumerate([(61,30),(101,20),(151,14),(201,12)]):
        L=cv2.cvtColor(out,cv2.COLOR_BGR2LAB)[...,0]
        bg=cv2.medianBlur(L,k).astype(np.float32);dd=L.astype(np.float32)-bg
        ink=((dd>thr) if dark else (dd<-thr))&R&~skin
        # also colour-difference ink (e.g. dark print on mid shirts)
        labo=cv2.cvtColor(out,cv2.COLOR_BGR2LAB).astype(np.float32)
        cd=np.sqrt((((labo-ref)*[0.5,1.2,1.2])**2).sum(-1));ink|=(cd>45)&R&~skin
        ink=nd.binary_opening(ink,iterations=1)
        M|=cv2.dilate(ink.astype(np.uint8)*255,np.ones((9,9),np.uint8))
        out=cv2.inpaint(a,M,11,cv2.INPAINT_TELEA)
    return out,M
