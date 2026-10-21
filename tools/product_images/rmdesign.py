import cv2,numpy as np,sys
from scipy import ndimage as nd
def clean(a,box=(.34,.74,.22,.78)):
    H,W=a.shape[:2];B=np.zeros((H,W),bool);B[int(H*box[0]):int(H*box[1]),int(W*box[2]):int(W*box[3])]=True
    L=cv2.cvtColor(a,cv2.COLOR_BGR2LAB)[...,0].astype(np.float32)
    lab=cv2.cvtColor(cv2.GaussianBlur(a,(0,0),2),cv2.COLOR_BGR2LAB).astype(np.float32)
    ref=np.median(lab[int(H*.55):int(H*.62),int(W*.42):int(W*.58)].reshape(-1,3),0)
    sh=(np.sqrt((((lab-ref)*[0.3,1.5,1.5])**2).sum(-1))<20);lb,n=nd.label(sh);sz=nd.sum(sh,lb,range(1,n+1))
    sh=nd.binary_fill_holes(lb==1+np.argmax(sz));sh=cv2.erode(sh.astype(np.uint8),np.ones((9,9),np.uint8))>0;B&=sh
    dark=ref[0]<110
    out=a.copy();M=np.zeros((H,W),np.uint8)
    for it,(k,thr) in enumerate([(61,35),(101,22),(151,16)]):
        Lc=cv2.cvtColor(out,cv2.COLOR_BGR2LAB)[...,0]
        bg=cv2.medianBlur(Lc,k).astype(np.float32);d=L-bg
        ink=((d>thr) if dark else (d<-thr))&B
        ink=nd.binary_opening(ink,iterations=1)
        M|=cv2.dilate(ink.astype(np.uint8)*255,np.ones((7,7),np.uint8))
        out=cv2.inpaint(a,M,9,cv2.INPAINT_TELEA)
    return out,M
if __name__=='__main__':
    a=cv2.imread(sys.argv[1]);o,m=clean(a);cv2.imwrite(sys.argv[2],o)
