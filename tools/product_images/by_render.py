# Birth Year (digits only) on blank model photos. Placement measured on the 1971 reference:
# year width ~2/3 of the shirt body, top ~0.23 body widths below the round neckline, centred on the shirt.
import cv2,numpy as np,sys,os,json
from place import apply
D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/vintage_e_by/'
ORDER=['black','white','pink','sage','burgundy','navy']
WF=float(os.environ.get('BYW',.78));TR=float(os.environ.get('BYT',.25));TV=float(os.environ.get('BYV',.17))
age,tag=sys.argv[1],sys.argv[2]
G=json.load(open('geo.json'))
for k,c in enumerate(ORDER,1):
    if c not in G: continue
    g=G[c];im=cv2.imread(g['file']);m=cv2.imread(g['mask'],0)//255
    f=f'{D}{age}_{c}.png'
    w=WF*g['bw'];top=g['ny']+(TV if g['neck']=='v' else TR)*g['bw']
    da=cv2.imread(f,cv2.IMREAD_UNCHANGED)[...,3];ys,xs=np.where(da>10);da=da[ys.min():ys.max()+1,xs.min():xs.max()+1]
    mm=cv2.erode(m,np.ones((9,9),np.uint8))
    while True:  # keep every digit on visible fabric (arms, hair)
        ww=int(w);hh=int(da.shape[0]*ww/da.shape[1]);x0=int(g['cx']-ww/2);y0=int(top)
        al=cv2.resize(da,(ww,hh))>15;cov=mm[y0:y0+hh,x0:x0+ww][al].mean()
        if cov>=0.9995 or w<0.85*WF*g['bw']: break
        w*=0.98
    print(c,round(w),round(cov,4),end=' ')
    o,_=apply(im,m,f,g['cx'],top,w)
    cv2.imwrite(f'final/{tag}_{k}_{c}.jpg',o,[cv2.IMWRITE_JPEG_QUALITY,94])
print()
