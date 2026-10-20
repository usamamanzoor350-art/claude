import cv2,numpy as np,json,sys
def skin_center(d,g):
    im=cv2.imread(f'{d}/{g["file"]}').astype(int);ny=g['ny'];cx=int(g['cx']);out=[]
    for dy in ([10,25,40] if g['neck']=='v' else [8,16,24]):
        y=ny-dy;r=im[y]
        sk=(r[:,2]-r[:,0]>28)&(r[:,2]>110)
        sk=cv2.morphologyEx(sk.astype(np.uint8)[None],cv2.MORPH_CLOSE,np.ones((1,7),np.uint8))[0]>0
        xs=np.where(sk)[0];xs=xs[(xs>cx-160)&(xs<cx+160)]
        if not len(xs): continue
        runs=np.split(xs,np.where(np.diff(xs)>1)[0]+1);rr=max(runs,key=len)
        out.append(((rr[0]+rr[-1])/2,rr[-1]-rr[0]))
    return out
if __name__=="__main__":
 for d in sys.argv[1:]:
     G=json.load(open(f'{d}/geo.json'))
     for c,g in G.items():
         r=skin_center(d,g);med=np.median([a for a,w in r]) if r else None
         print(d,c,g['neck'],'cx',g['cx'],'skin',[(round(a),w) for a,w in r],'-> d',None if med is None else round(med-g['cx']))
