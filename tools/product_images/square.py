import cv2,numpy as np,glob,os,sys
rng=np.random.default_rng(0)
def side(strip,pad,H,flat):
    rows=strip.mean(1);yy=np.arange(H);ok=np.ones(H,bool)
    if flat: ok[270:740]=False
    col=np.stack([np.interp(yy,yy[ok],rows[ok,c]) for c in range(3)],1)
    col=cv2.GaussianBlur(col[:,None,:],(1,61),0)
    return np.repeat(col,pad,1)+rng.normal(0,1.6,(H,pad,3)).astype(np.float32)
tag=sys.argv[1];os.makedirs('sq',exist_ok=True)
for f in sorted(glob.glob(f'final/{tag}_*.jpg')):
    im=cv2.imread(f).astype(np.float32);H,Wd=im.shape[:2];pad=(H-Wd)//2;fl='flatlay' in f
    w=30 if fl else 40
    if not fl:
        c=im[30:30+Wd];cv2.imwrite('sq/'+os.path.basename(f).replace('.jpg','_sq.jpg'),cv2.resize(np.clip(c,0,255).astype(np.uint8),(1600,1600),interpolation=cv2.INTER_LANCZOS4),[cv2.IMWRITE_JPEG_QUALITY,93]);continue
    sq=np.concatenate([side(im[:,:w],pad,H,fl),im,side(im[:,-w:],pad,H,fl)],1)
    if not fl:
        for x0 in (pad,pad+Wd): sq[:,x0-12:x0+12]=cv2.GaussianBlur(sq[:,x0-18:x0+18],(25,1),0)[:,6:-6]
    cv2.imwrite('sq/'+os.path.basename(f).replace('.jpg','_sq.jpg'),cv2.resize(np.clip(sq,0,255).astype(np.uint8),(1600,1600),interpolation=cv2.INTER_LANCZOS4),[cv2.IMWRITE_JPEG_QUALITY,93])
fs=sorted(glob.glob(f'sq/{tag}_*_sq.jpg'));ims=[cv2.resize(cv2.imread(f),(420,420)) for f in fs];ims.append(np.full_like(ims[0],255))
cv2.imwrite(f'prev_{tag}.jpg',np.vstack([np.hstack(ims[:4]),np.hstack(ims[4:])]))
