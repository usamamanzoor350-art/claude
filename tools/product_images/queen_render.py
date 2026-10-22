# Queen design placed exactly like the zip mockup (same method as the Finger design), measured there against the shirt:
#   T = shirt body width just below the armpits (mockup: 715px)
#   design width = 450/715 T, its centre sits at armpit height, and its box centre is 0.035 T right of the shirt centre.
# On a model only the part between the arms is visible (bw), so T = 1.25 bw.
import cv2,numpy as np,sys,os,json
from place import apply
os.chdir(os.path.dirname(os.path.abspath(__file__)))
D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/queen_z/'
ORDER=['black','white','pink','sage','burgundy','navy']
REF_W=1335/3  # mockup design width at 715 torso, in mockup px (extract upscaled x3)
age,tag=sys.argv[1],sys.argv[2]
G=json.load(open('geo.json'))
MED=float(np.median([v['bw'] for v in G.values()]))  # same model and framing in all 6 photos: keep the design size consistent
for k,c in enumerate(ORDER,1):
    if c not in G: continue
    g=G[c];im=cv2.imread(g['file']);m=cv2.imread(g['mask'],0)//255
    ink='white' if c in('black','burgundy','navy') else 'black'
    f=f'{D}{age}_{ink}.png'
    bw=max(g['bw'],0.95*MED);T=1.25*bw
    da=cv2.imread(f,cv2.IMREAD_UNCHANGED)[...,3];ys,xs=np.where(da>10);da=da[ys.min():ys.max()+1,xs.min():xs.max()+1]
    w=0.733*T;w0=w  # queen mockup: print 568px wide on a 775px shirt body
    round_ny=g['ny'] if g['neck']=='round' else g['ny']-0.2*bw
    ya=round_ny+0.42*T
    cx=g['cx']+0.005*T
    mm=cv2.erode(m,np.ones((9,9),np.uint8))
    def cover(w,dy):
        ww=int(w);hh=int(da.shape[0]*ww/da.shape[1])
        top=max(ya-0.055*T-hh/2, g['ny']+0.06*T)+dy
        x0=int(cx-ww/2);y0=int(top)
        al=cv2.resize(da,(ww,hh))>15;return mm[y0:y0+hh,x0:x0+ww][al].mean(),top
    # if hair/arm covers part of the design: first move it down a little, only then shrink
    best=None
    while True:
        for dy in np.arange(0,0.08*T,4):
            cov,top=cover(w,dy)
            if cov>=0.9995: break
        if cov>=0.9995 or w<0.9*w0: break
        w*=0.98
    print(c,round(w),round(cov,4),end='  ')
    o,_=apply(im,m,f,cx,top,w)
    cv2.imwrite(f'final/{tag}_{k}_{c}.jpg',o,[cv2.IMWRITE_JPEG_QUALITY,94])
