# digits-only Birth Year designs: cut the year out of the approved per-colour Vintage PNGs
import numpy as np,os
from PIL import Image
from scipy import ndimage as nd
D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/'
for f in sorted(os.listdir(D+'vintage_e')):
    im=Image.open(D+'vintage_e/'+f);arr=np.asarray(im).copy();a=arr[...,3]
    rows=np.where((a>10).sum(1)>0)[0];y0,y1=rows[0],rows[-1]
    prof=(a>10).sum(1);lo=y0+int(.3*(y1-y0));hi=y0+int(.6*(y1-y0))
    split=lo+int(np.argmin(prof[lo:hi]))
    lbl,n=nd.label(a>10);keep=np.zeros(n+1,bool)
    for i,s in enumerate(nd.find_objects(lbl),1):
        keep[i]=(s[0].start+s[0].stop)/2>split
    arr[...,3]=np.where(keep[lbl],a,0)
    d=Image.fromarray(arr);d=d.crop(d.getbbox())
    p=20;o=Image.new('RGBA',(d.width+2*p,d.height+2*p));o.paste(d,(p,p));o.save(D+'vintage_e_by/'+f)
print(len(os.listdir(D+'vintage_e_by')))
# light shirts: cap each digit's lightness below the fabric so every digit reads clearly (hue kept)
import cv2
LMAX={'white':66,'pink':56,'sage':50}
for f in sorted(os.listdir(D+'vintage_e_by')):
    c=f[:-4].split('_')[1]
    if c not in LMAX: continue
    im=cv2.imread(D+'vintage_e_by/'+f,cv2.IMREAD_UNCHANGED);lab=cv2.cvtColor(im[...,:3],cv2.COLOR_BGR2LAB).astype(np.float32)
    L=lab[...,0]*100/255;k=np.minimum(1,LMAX[c]/np.maximum(L,1))
    lab[...,0]*=k;lab[...,1:]=128+(lab[...,1:]-128)*np.minimum(1.25,1/np.maximum(k,.6))[...,None]
    im[...,:3]=cv2.cvtColor(np.clip(lab,0,255).astype(np.uint8),cv2.COLOR_LAB2BGR);cv2.imwrite(D+'vintage_e_by/'+f,im)
