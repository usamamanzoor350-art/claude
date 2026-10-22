# Pull the Queen print off the black-shirt mockups: gold crown/fireworks keep their colour, the white script
# is recoloured to black for light shirts.
import numpy as np,cv2,glob,os,re
from PIL import Image
from scipy import ndimage as nd
O='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/queen_z/'
S=2048/1254
for f in sorted(glob.glob('queen/*')):
    m=re.search(r'(\d\d)\.jpg$',f);age=m.group(1) if m else '40'
    im=np.array(Image.open(f).convert('RGB').resize((2048,2048),Image.LANCZOS)).astype(np.float32)
    x0,x1,y0,y1=[int(v*S) for v in (330,930,235,730)]
    c=im[y0:y1,x0:x1]
    bg=np.median(im[int(800*S):int(850*S),int(600*S):int(650*S)].reshape(-1,3),0)  # plain shirt
    mx=c.max(2);mn=c.min(2);sat=(mx-mn)/np.maximum(mx,1)
    a=np.clip((mx-bg.max()-12)/(235-bg.max()-12),0,1)
    lab,n=nd.label(a>0.25);sz=np.bincount(lab.ravel());keep=sz>25;keep[0]=False
    a=a*nd.binary_dilation(keep[lab],iterations=3)
    rgb=np.clip((c-bg*(1-a[...,None]))/np.maximum(a[...,None],0.02),0,255)
    goldm=(sat>0.15)&(a>0.04)&~((mn>200)&(sat<0.12))
    # crown: biggest gold blob, solid object -> fully opaque incl. its dark shading
    lab,n=nd.label(nd.binary_closing(goldm,iterations=3));sz=np.bincount(lab.ravel());sz[0]=0
    crown=nd.binary_fill_holes(lab==np.argmax(sz));crown=nd.binary_erosion(crown,iterations=1)
    a=np.where(crown,np.maximum(a,cv2.GaussianBlur(crown.astype(np.float32),(0,0),1.0)),a)
    rgb=np.where(crown[...,None],c,rgb)
    gold=cv2.GaussianBlur((goldm|crown).astype(np.float32),(0,0),1.2)
    ys,xs=np.where(a>0.04);sl=(slice(ys.min()-4,ys.max()+5),slice(xs.min()-4,xs.max()+5))
    a,rgb,gold=a[sl],rgb[sl],gold[sl]
    for ink,base in (('white',255.),('black',20.)):
        g=rgb if ink=='white' else rgb*0.82   # slightly deeper gold so it reads on light fabric
        aa=a if ink=='white' else np.where(gold>0.5,np.clip(a,0,1)**0.6,a)
        col=g*gold[...,None]+base*(1-gold[...,None])
        Image.fromarray(np.dstack([col,aa*255]).clip(0,255).astype(np.uint8),'RGBA').save(O+f'{age}_{ink}.png')
    print(age,a.shape,end='  ')
