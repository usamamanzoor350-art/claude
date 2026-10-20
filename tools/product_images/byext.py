from PIL import Image;import numpy as np,cv2,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
out='designs/birthyear/'
for y in range(1961,1987):
    im=np.array(Image.open(f'vall/{y}.png'));rgb=im[...,:3].astype(np.int32);a=im[...,3].copy()
    d=np.sqrt(((rgb-np.array([200,175,125]))**2).sum(-1))
    tan=(d<42)&(a>0)
    tanreg=cv2.dilate(((d<30)&(a>150)).astype(np.uint8),np.ones((9,9),np.uint8))>0
    dig=(d>=42)&(a>150)
    a[tan|(tanreg&~dig)]=0
    keep=cv2.dilate((dig&~tanreg).astype(np.uint8),np.ones((7,7),np.uint8))>0
    a[~keep]=0
    n,lbl,st,_=cv2.connectedComponentsWithStats((a>20).astype(np.uint8))
    small=np.zeros(n,bool);small[1:]=st[1:,4]<400
    a[small[lbl]]=0
    im[...,3]=a
    ys,xs=np.where(a>0);c=im[ys.min():ys.max()+1,xs.min():xs.max()+1]
    age=2026-y
    Image.fromarray(c).save(f'{out}{age}_white.png',compress_level=1);Image.fromarray(c).save(f'{out}{age}_black.png',compress_level=1)
    print(y,flush=True)
print('done')
