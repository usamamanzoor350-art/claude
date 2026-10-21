import cv2,numpy as np
from scipy import ndimage as nd
def clean(a):
    H,W=a.shape[:2]
    lab=cv2.cvtColor(cv2.GaussianBlur(a,(0,0),1.5),cv2.COLOR_BGR2LAB).astype(np.float32)
    # shirt colour = most common colour in lower-chest band (design rarely reaches here)
    band=lab[int(H*.70):int(H*.80),int(W*.35):int(W*.65)].reshape(-1,3)
    q=(band//6).astype(int);k=q[:,0]*10000+q[:,1]*100+q[:,2];v,c=np.unique(k,return_counts=True)
    ref=band[k==v[np.argmax(c)]].mean(0)
    d=np.sqrt((((lab-ref)*[0.35,1.4,1.4])**2).sum(-1))
    shirt=d<18
    shirt=nd.binary_opening(shirt,iterations=2)
    l,n=nd.label(shirt);sz=nd.sum(shirt,l,range(1,n+1));shirt=l==1+np.argmax(sz)
    region=nd.binary_fill_holes(nd.binary_closing(shirt,iterations=12))
    region=cv2.erode(region.astype(np.uint8),np.ones((7,7),np.uint8))>0
    B=np.zeros((H,W),bool);B[int(H*.22):int(H*.85),int(W*.12):int(W*.88)]=True
    g=a.astype(int);skin=((g[...,2]-g[...,0])>30)&((g[...,1]-g[...,0])>5)&(g[...,2]>110)&(d>18)
    skin=nd.binary_opening(skin,iterations=3)
    ink=region&B&~shirt&~skin
    # keep only ink that contrasts in lightness (prints), ignore soft folds
    ink&=np.abs(lab[...,0]-ref[0])>14
    ink=nd.binary_opening(ink,iterations=1)
    M=cv2.dilate(ink.astype(np.uint8)*255,np.ones((9,9),np.uint8))
    out=cv2.inpaint(a,M,11,cv2.INPAINT_TELEA)
    return out,M
