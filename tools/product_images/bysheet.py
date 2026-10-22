import cv2,numpy as np,os,sys
S='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/'
K=['1_black','2_white','3_pink','4_sage','5_burgundy','6_navy','7_flatlay']
def d(a): return 'h50n' if a==50 else (f'f{a}' if os.path.isdir(S+f'f{a}') else f'h{a}')
a0,a1,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3];rows=[]
for a in range(a0,a1+1):
    ims=[cv2.resize(cv2.imread(S+f'{d(a)}/sq/by{a}_{k}_sq.jpg'),(260,260)) for k in K]
    r=np.hstack(ims);cv2.putText(r,str(a),(8,30),0,1,(0,0,255),2);rows.append(r)
cv2.imwrite(out,np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,85])
