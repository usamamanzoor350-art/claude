import cv2,numpy as np,sys
sys.path.insert(0,'/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad')
import rmdesign as r1, rmdesign3 as r3
def clean(a):
    _,m1=r1.clean(a);_,m3=r3.clean(a)
    M=cv2.bitwise_or(m1,m3)
    out=cv2.inpaint(a,M,11,cv2.INPAINT_TELEA)
    # second pass on the result catches leftovers
    _,m1b=r1.clean(out);_,m3b=r3.clean(out);M2=cv2.bitwise_or(m1b,m3b)
    M=cv2.bitwise_or(M,M2);out=cv2.inpaint(a,M,11,cv2.INPAINT_TELEA)
    return out,M
