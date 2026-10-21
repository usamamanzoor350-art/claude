import cv2,numpy as np,glob,os
S='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/'
# target ink lightness (OpenCV LAB, 0-255) per shirt colour: same hues, only lightness/chroma pushed away from the shirt
TARGET={'black':200,'navy':200,'burgundy':205,'white':125,'pink':112,'sage':98}
CHROMA={'black':1.25,'navy':1.25,'burgundy':1.15,'white':1.3,'pink':1.3,'sage':1.35}
for f in glob.glob(S+'designs/vintage_z/*_black.png'):
    age=os.path.basename(f).split('_')[0];d=cv2.imread(f,cv2.IMREAD_UNCHANGED)
    lab=cv2.cvtColor(d[...,:3],cv2.COLOR_BGR2LAB).astype(np.float32);m=d[...,3]>200;mL=lab[...,0][m].mean()
    for c,t in TARGET.items():
        o=lab.copy();o[...,0]=np.clip(t+(lab[...,0]-mL)*0.4,0,255)
        o[...,1:]=np.clip(128+(lab[...,1:]-128)*CHROMA[c],0,255)
        e=d.copy();e[...,:3]=cv2.cvtColor(o.astype(np.uint8),cv2.COLOR_LAB2BGR)
        cv2.imwrite(S+f'designs/vintage_e/{age}_{c}.png',e)
    # flat lay files: _white = for black flat shirt, _black = for pink/white flat shirts
    cv2.imwrite(S+f'designs/vintage_e/{age}_white.png',cv2.imread(S+f'designs/vintage_e/{age}_black.png',cv2.IMREAD_UNCHANGED)) if False else None
print('ok')
