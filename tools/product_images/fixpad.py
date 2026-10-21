import cv2,json,sys,glob
d,a=sys.argv[1],sys.argv[2];G=json.load(open(f'{d}/geo.json'))
O=['black','white','pink','sage','burgundy','navy']
for c,g in G.items():
    if g['file'].endswith('_p.png'):
        k=O.index(c)+1;f=f'{d}/final/vint{a}_{k}_{c}.jpg'
        x=cv2.imread(f)[140:1262];x=cv2.resize(x,(1600,1600),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(f'{d}/sq/vint{a}_{k}_{c}_sq.jpg',x,[cv2.IMWRITE_JPEG_QUALITY,92]);print('fixed',c)
