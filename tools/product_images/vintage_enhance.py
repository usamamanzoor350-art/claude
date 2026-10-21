import cv2,numpy as np,glob,os
S='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/'
# light touch only: white = exact zip colours; pink/sage slightly deeper; dark shirts slightly brighter (soft shine)
SHIFT={'white':(0,1.0),'pink':(-32,1.15),'sage':(-38,1.18),'black':(22,1.08),'navy':(22,1.08),'burgundy':(26,1.08)}
for f in glob.glob(S+'designs/vintage_z/*_black.png'):
    age=os.path.basename(f).split('_')[0];d=cv2.imread(f,cv2.IMREAD_UNCHANGED)
    lab=cv2.cvtColor(d[...,:3],cv2.COLOR_BGR2LAB).astype(np.float32)
    for c,(dl,ch) in SHIFT.items():
        o=lab.copy();o[...,0]=np.clip(lab[...,0]+dl,0,255);o[...,1:]=np.clip(128+(lab[...,1:]-128)*ch,0,255)
        e=d.copy();e[...,:3]=cv2.cvtColor(o.astype(np.uint8),cv2.COLOR_LAB2BGR)
        cv2.imwrite(S+f'designs/vintage_e/{age}_{c}.png',e)
print('ok')
