import json,urllib.request,cv2,numpy as np,os,sys
sys.path.insert(0,'.')
from rmdesign import clean
P={a:imgs for a,t,imgs in json.load(open('coll/list.json'))}
REF={'black':(25,128,128),'white':(235,128,128),'pink':(200,150,128),'sage':(175,120,138),'burgundy':(65,165,140),'navy':(45,133,108)}
def classify(a):
    H,W=a.shape[:2];lab=cv2.cvtColor(cv2.GaussianBlur(a,(0,0),3),cv2.COLOR_BGR2LAB).astype(float)
    # sample a band across the lower chest
    px=lab[int(H*.62):int(H*.70),int(W*.40):int(W*.60)].reshape(-1,3);m=np.median(px,0)
    d={c:np.sqrt(((m-np.array(v))**2*[0.5,1.5,1.5]).sum()) for c,v in REF.items()};return min(d,key=d.get),m
age=int(sys.argv[1]);d=f'hv{age}';os.makedirs(d+'/final',exist_ok=True);os.makedirs(d+'/sq',exist_ok=True)
got={}
STD=['black','white','pink','sage','burgundy','navy']
ORD={65:['black','pink','burgundy','white','navy','sage'],66:['pink','burgundy','sage','navy','white','black']}.get(age,STD)
for k,u in enumerate(P[age][:7]):
    f=f'{d}/raw{k+1}.png'
    if not os.path.exists(f): urllib.request.urlretrieve(u,f)
    a=cv2.imread(f)
    if a is None or 'q8_' in u or 'Size' in u: continue
    if abs(a.shape[0]-a.shape[1])>5: continue
    if k>=6: continue
    c=ORD[k]
    got[c]=k+1
    a=cv2.resize(a,(1122,1122),interpolation=cv2.INTER_AREA);o,_=clean(a)
    p=np.zeros((1402,1122,3),np.uint8);p[:]=np.median(o[:10].reshape(-1,3),0);p[140:1262]=o
    cv2.imwrite(f'{d}/src_{c}_p.png',p)
print(age,got)
json.dump(got,open(f'{d}/colors.json','w'))
