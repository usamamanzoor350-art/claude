import cv2,numpy as np,sys,os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
def mid(src,TL,comp,Ck):
    im=np.array(Image.open(src).convert('RGBA'));rgb=np.ascontiguousarray(im[...,:3])
    lab=cv2.cvtColor(rgb,cv2.COLOR_RGB2LAB).astype(np.float32)
    lab[...,0]=TL+(lab[...,0]-TL)*comp
    lab[...,1]=128+(lab[...,1]-128)*Ck;lab[...,2]=128+(lab[...,2]-128)*Ck
    im[...,:3]=cv2.cvtColor(np.clip(lab,0,255).astype(np.uint8),cv2.COLOR_LAB2RGB);return im
if __name__=='__main__':
    TL,comp,Ck,tag=float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
    for k,p in {'vintage':f'{D}/vall/1976.png','birthyear':f'{D}/designs/birthyear/50_white.png'}.items():
        Image.fromarray(mid(p,TL,comp,Ck)).save(f'{D}/test_{k}_{tag}.png',compress_level=1)
