import cv2,numpy as np,json,sys,os
def neck_center(d,c,g):
    im=cv2.imread(f'{d}/{g["file"]}');m=cv2.imread(f'{d}/{g["mask"]}',0)>0
    ny=g['ny'];cx=int(g['cx']);res=[]
    for dy in ([8,20,35,50] if g['neck']=='v' else [6,14,22]):
        y=ny-dy
        if y<0: continue
        row=m[y];xs=np.where(~row[max(0,cx-250):cx+250])[0]+max(0,cx-250)
        # find gap (non-shirt) run containing or nearest cx bounded by shirt on both sides
        sh=np.where(row)[0]
        L=sh[sh<cx];R=sh[sh>cx]
        if len(L) and len(R):
            # nearest shirt pixels left and right of cx with gap between
            l=L.max();r=R.min()
            if r-l>10: res.append(((l+r)/2,r-l))
    return res
if __name__=="__main__":
 for d in sys.argv[1:]:
     G=json.load(open(f'{d}/geo.json'))
     for c,g in G.items():
         r=neck_center(d,c,g)
         print(d,c,'cx',g['cx'],'neck',[(round(a),w) for a,w in r])
