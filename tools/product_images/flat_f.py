import cv2,numpy as np,sys
from place import apply
from PIL import Image,ImageDraw,ImageFont
F='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/fonts/'
POS=None
def flat(dw,db,out,pw=168):
    im=cv2.imread('src_1293.png')
    _pos=[(n,cx,t,dw if i=='w' else db) for n,cx,t,i in POS] if POS else None
    for n,cx,top,ink in (_pos if _pos else [('black',210,391,dw),('pink',558,432,db),('white',909,391,db)] if 'vintage' in dw else [('black',212,372,dw),('pink',558,428,db),('white',925,377,db)]):
        m=cv2.imread(f'fmask_{n}.png',0)//255
        import os as _o
        _p=ink.rsplit('_',1)[0]+f'_{n}.png'
        if 'vintage_e' in ink and _o.path.exists(_p): ink=_p
        cxa=cx
        if 'hello' in ink:
            import sys as _s;_s.path.insert(0,'..');from firstl import hello_info;hf,hc=hello_info(ink);pw=min(112/hf,190);cxa=cx+(0.5-hc)*pw
        im,_=apply(im,m,ink,cxa,top,pw,disp=0.5,opacity=0.97)
    img=Image.fromarray(cv2.cvtColor(im,cv2.COLOR_BGR2RGB));d=ImageDraw.Draw(img);Wc=img.width
    def ctext(y,t,f,fill):
        w=d.textlength(t,font=f);d.text(((Wc-w)/2,y),t,font=f,fill=fill)
    def font(n,s,wt):
        f=ImageFont.truetype(F+n,s);f.set_variation_by_axes([wt]);return f
    ink_c=(43,36,38);soft=(110,98,94);acc=(140,58,74)
    y=830
    ctext(y,"We don't sell a piece of cloth.",font('PlayfairDisplay-Italic%5Bwght%5D.ttf',52,500),soft);y+=84
    ctext(y,"We sell the feeling",font('PlayfairDisplay%5Bwght%5D.ttf',66,700),ink_c);y+=80
    ctext(y,"of being celebrated.",font('PlayfairDisplay%5Bwght%5D.ttf',66,700),acc);y+=118
    d.line([(Wc/2-60,y),(Wc/2+60,y)],fill=(185,170,162),width=2);y+=40
    sizes=['S','M','L','XL','2XL','3XL'];cw=100;gap=16;tw=len(sizes)*cw+(len(sizes)-1)*gap;x=(Wc-tw)/2;fb=font('Montserrat%5Bwght%5D.ttf',25,600)
    for s in sizes:
        d.rounded_rectangle([x,y,x+cw,y+56],radius=28,outline=(150,134,126),width=2)
        t=d.textlength(s,font=fb);d.text((x+(cw-t)/2,y+13),s,font=fb,fill=ink_c);x+=cw+gap
    y+=96
    ctext(y,"100% SOFT COTTON   ·   MADE TO ORDER, JUST FOR YOU",font('Montserrat%5Bwght%5D.ttf',26,500),soft);y+=64
    ctext(y,"BirthdayUniverse.co",font('PlayfairDisplay-Italic%5Bwght%5D.ttf',32,400),(150,134,126))
    img.save(out,quality=94)
if __name__=='__main__':
    D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/'
    DES,AGE,TAG,PW=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])
    flat(D+f'{DES}/{AGE}_'+('black' if DES=='vintage_e' else 'white')+'.png',D+f'{DES}/{AGE}_'+('white' if DES=='vintage_e' else 'black')+'.png',f'final/{TAG}_7_flatlay.jpg',PW)
