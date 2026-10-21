import cv2,numpy as np
def first_l(path):
    d=cv2.imread(path,cv2.IMREAD_UNCHANGED);a=d[...,3]>40;ys,xs=np.where(a);a=a[ys.min():ys.max()+1,xs.min():xs.max()+1];H,W=a.shape
    rows=a.any(1)
    # hello band: from top to first blank row after 20% height
    y=int(H*0.15)
    while y<H and rows[y]: y+=1
    if y>H*0.6: y=int(H*0.45)  # hello touches the number: no blank gap
    band=a[:y]
    # ascender zone: top 28% of hello band (h, l, l stems)
    asc=band[:max(3,int(y*0.28))]
    xs=np.where(asc.any(0))[0];runs=np.split(xs,np.where(np.diff(xs)>3)[0]+1)
    runs=[r for r in runs if len(r)>2]
    return W,[((r[0]+r[-1])/2/W) for r in runs]
if __name__=='__main__':
    for age in [50,55,61,70]:
        for ink in ['white']:
            try: print(age,first_l(f'designs/hello/{age}_{ink}.png'))
            except Exception as e: print(age,e)
