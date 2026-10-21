import cv2,numpy as np,json,sys
def skin(a): return ((a[...,2]-a[...,0])>30)&((a[...,1]-a[...,0])>5)&(a[...,2]>110)
def measure(f,neck,x0=561):
    a=cv2.imread(f).astype(int);H,W=a.shape[:2];sk=skin(a)
    sk=cv2.morphologyEx(sk.astype(np.uint8),cv2.MORPH_OPEN,np.ones((3,3),np.uint8))>0
    # neck bottom: along center columns, last skin row of the neck/chest skin before shirt
    col=sk[:,x0-4:x0+5].mean(1)>0.5
    ys=np.where(col[250:900])[0]+250
    # find the first long non-skin run after ys start (shirt)
    ny=None
    for y in ys:
        if col[y] and not col[y+1:y+25].any(): ny=y;break
    # torso edges at chest rows
    lab=cv2.cvtColor(cv2.GaussianBlur(cv2.imread(f),(0,0),2),cv2.COLOR_BGR2LAB).astype(float)
    ref=np.median(lab[ny+150:ny+250,x0-30:x0+30].reshape(-1,3),0)
    white=ref[0]>225
    d=np.sqrt((((lab-ref)*np.array([0.35,1.5,1.5]))**2).sum(-1))
    shirt=(~sk) if white else (d<22)
    Ls=[];Rs=[]
    for y in range(ny+230,ny+380,6):
        r=shirt[y];x=x0
        if not r[x]: continue
        l=x
        while l>5 and r[l-1]: l-=1
        rr=x
        while rr<W-6 and r[rr+1]: rr+=1
        if rr-l<700: Ls.append(l);Rs.append(rr)
    L=float(np.median(Ls));R=float(np.median(Rs))
    # neck center refine: skin run at ny-6
    r=sk[ny-6];xs=np.where(r[x0-150:x0+150])[0]+x0-150
    runs=np.split(xs,np.where(np.diff(xs)>1)[0]+1);rr=max(runs,key=len);nc=(rr[0]+rr[-1])/2
    # hem: jeans at center column below ny+250
    hem=H-1
    for y in range(ny+250,H):
        if not shirt[y,int((L+R)/2)-10:int((L+R)/2)+10].mean()>0.5 and not shirt[y+5,int((L+R)/2)]: hem=y;break
    return dict(ny=int(ny),L=L,R=R,cx=(L+R)/2,neck_cx=float(nc),bw=R-L,hem=int(hem),neck=neck)
if __name__=='__main__':
    P=json.loads(sys.argv[1]);G={}
    for f,c,nk in P:
        g=measure(f,nk);g.update(file=f,mask=f'mask_{c}.png')
        m=np.zeros(cv2.imread(f).shape[:2],np.uint8);m[g['ny']-5:g['hem']-8,int(g['L'])+4:int(g['R'])-4]=255;cv2.imwrite(g['mask'],m)
        g['maxbottom']=g['hem']-35
        G[c]=g;print(c,{k:(round(v) if isinstance(v,float) else v) for k,v in g.items() if k not in('file','mask')})
    json.dump(G,open('geo.json','w'))
