import numpy as np,cv2,glob,os
from PIL import Image
from scipy import ndimage as nd
O='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/finger_z/'
SC=3  # upscale for smoother edges
for f in sorted(glob.glob('src/*')):
    age=os.path.basename(f).split('.')[0]
    im=np.array(Image.open(f).convert('RGB').resize((1254,1254),Image.LANCZOS)).astype(np.float32)
    c=im[320:770,420:940]
    c=cv2.resize(c,None,fx=SC,fy=SC,interpolation=cv2.INTER_CUBIC)
    R,G,B=c[...,0],c[...,1],c[...,2]; L=c.mean(2)
    red=(R>110)&(R-G>55)&(R-B>45)
    a=np.clip((L-70)/(215-70),0,1)
    a=np.maximum(a,red.astype(np.float32))
    red_s=cv2.GaussianBlur(red.astype(np.float32),(0,0),1.0)
    # drop specks: keep components with some size
    lab,n=nd.label(a>0.35); sz=np.bincount(lab.ravel()); keep=sz>60*SC; keep[0]=False
    k=nd.binary_dilation(keep[lab],iterations=3*SC)
    a=a*k
    a=cv2.GaussianBlur(a,(0,0),0.6)
    ys,xs=np.where(a>0.04); a=a[ys.min()-6:ys.max()+7,xs.min()-6:xs.max()+7]; rs=red_s[ys.min()-6:ys.max()+7,xs.min()-6:xs.max()+7]
    for ink,base in (('white',(255,255,255)),('black',(18,18,18))):
        rgb=np.zeros(a.shape+(3,),np.float32); rgb[:]=base
        nail=np.array([200,16,30],np.float32)
        rgb=rgb*(1-rs[...,None])+nail*rs[...,None]
        out=np.dstack([rgb,a*255]).clip(0,255).astype(np.uint8)
        Image.fromarray(out,'RGBA').save(O+f'{age}_{ink}.png')
    print(age,a.shape,end=' ')
