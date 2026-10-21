import cv2,numpy as np,glob,sys
S='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/'
out=sys.argv[1];rows=[]
for p in sys.argv[2:]:
    d,a=p.split(':');fs=sorted(glob.glob(f'{S}{d}/sq/fing{a}_*_sq.jpg'))
    ims=[cv2.resize(cv2.imread(f),(300,300)) for f in fs]
    r=np.hstack(ims);cv2.putText(r,a,(8,40),cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,0,255),3);rows.append(r)
cv2.imwrite(out,np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,85])
