# digits-only Birth Year designs: cut the year out of the approved per-colour Vintage PNGs
import numpy as np,os
from PIL import Image
from scipy import ndimage as nd
D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/'
# ages where a "Vintage" g/t tail is fused onto the top of the digits; each digit's top is rebuilt from the same
# digit in a clean age of the same colour (all years share one font and artboard)
TAIL=[32,39,65,69]
def digits(age,c):
    im=Image.open(D+f'vintage_e/{age}_{c}.png');arr=np.asarray(im).copy();a=arr[...,3].copy()
    rows=np.where((a>10).sum(1)>0)[0];y0,y1=rows[0],rows[-1]
    prof=(a>10).sum(1);lo=y0+int(.3*(y1-y0));hi=y0+int(.6*(y1-y0))
    split=lo+int(np.argmin(prof[lo:hi]))  # thinnest row between the word and the digits
    lbl,n=nd.label(a>10);objs=nd.find_objects(lbl);keep=np.zeros(n+1,bool)
    for i,s in enumerate(objs,1): keep[i]=(s[0].start+s[0].stop)/2>split
    arr[...,3]=np.where(keep[lbl],a,0)
    xs=np.where((arr[...,3]>10).any(0))[0];xl=xs[0]+.1*(xs[-1]-xs[0])
    dtop=min(s[0].start for s in objs if s[1].stop<=xl and s[0].stop>=y1-15)  # top of the leading "1"
    return arr,dtop,xs[0]
def spans(arr,dtop):  # x-ranges of the 4 digits, from the digit body below the overshoot
    col=(arr[dtop+10:,:,3]>10).any(0);x=np.where(col)[0];g=np.split(x,np.where(np.diff(x)>18)[0]+1)
    return [(q[0],q[-1]) for q in g]
for f in sorted(os.listdir(D+'vintage_e')):
    age,c=int(f.split('_')[0]),f[:-4].split('_')[1]
    arr,dtop,x0=digits(age,c)
    if age in TAIL:
        # tail ink is exactly the word's colour; digits differ by >=30 RGB, so a tight match removes only the tail
        a0=np.asarray(Image.open(D+f'vintage_e/{age}_{c}.png')).astype(float);al=a0[...,3]
        r=np.where((al>10).any(1))[0];top=slice(r[0],r[0]+int(.25*(r[-1]-r[0])))
        wc=np.median(a0[top][...,:3][al[top]>200],0)
        dist=np.sqrt(((arr[...,:3].astype(float)-wc)**2).sum(-1));near=dist<14;keep0=arr[...,3].copy()
        near[dtop+int(.1*(r[-1]-dtop)):]=False
        arr[...,3][near]=0
        # anti-aliased rim of the removed word, and anything above the digits' overshoot line
        import cv2 as _cv
        rim=_cv.dilate(near.astype(np.uint8),np.ones((5,5),np.uint8))>0
        arr[...,3][rim]=0
        back=rim&~near&(dist>28)&(keep0>10);arr[...,3][back]=keep0[back]  # digit pixels inside the rim stay
        arr[:dtop-10,:,3]=0
        # what is left of the tail: tiny specks off the digits
        l2,_=nd.label(arr[...,3]>10)
        for i,s2 in enumerate(nd.find_objects(l2),1):
            if (l2[s2]==i).sum()<60: arr[...,3][s2][l2[s2]==i]=0
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
