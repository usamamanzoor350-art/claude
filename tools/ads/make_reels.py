# 9:16 Meta Reels ads from product photos: slow zoom slides, hook text in the safe zone, brand end card.
import sys,os,subprocess,numpy as np
from PIL import Image,ImageDraw,ImageFont
SRC,OUT,FONTS=sys.argv[1],sys.argv[2],sys.argv[3]
W,H,FPS=1080,1920,30
def font(sz,wt=800):
    f=ImageFont.truetype(FONTS+'/Montserrat%5Bwght%5D.ttf',sz)
    try: f.set_variation_by_axes([wt])
    except Exception: pass
    return f
SQ=1080;TOP=470  # full square photo in the middle, text on the cream band above it
def cover(path):
    im=Image.open(path).convert('RGB');s=SQ*1.06/min(im.size)
    return im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
def wrap(d,t,f,maxw):
    lines,cur=[],''
    for w in t.split():
        n=(cur+' '+w).strip()
        if d.textlength(n,font=f)<=maxw: cur=n
        else: lines.append(cur);cur=w
    return lines+[cur]
def caption(img,text,y,sz=74,bg=(0,0,0,150),fg='white'):
    if not text: return img
    ov=Image.new('RGBA',img.size,(0,0,0,0));d=ImageDraw.Draw(ov);f=font(sz)
    ls=wrap(d,text,f,W-180);lh=int(sz*1.25);th=lh*len(ls)
    for i,l in enumerate(ls):
        tw=d.textlength(l,font=f);x=(W-tw)/2;yy=y+i*lh
        d.rounded_rectangle([x-28,yy-10,x+tw+28,yy+lh-2],radius=22,fill=bg)
        d.text((x,yy),l,font=f,fill=fg)
    return Image.alpha_composite(img.convert('RGBA'),ov).convert('RGB')
def endcard(title,sub):
    im=Image.new('RGB',(W,H),(248,240,234));d=ImageDraw.Draw(im)
    def c(y,t,f,fill):
        for l in wrap(d,t,f,W-160):
            d.text(((W-d.textlength(l,font=f))/2,y),l,font=f,fill=fill);y+=int(f.size*1.25)
        return y
    y=c(560,title,font(84),(43,36,38));y=c(y+30,sub,font(46,500),(110,98,94))
    d.rounded_rectangle([W/2-300,y+90,W/2+300,y+210],radius=60,fill=(140,58,74))
    f=font(52);t='Shop now';d.text(((W-d.textlength(t,font=f))/2,y+118),t,font=f,fill='white')
    c(y+300,'BirthdayUniverse.co',font(50,600),(140,58,74))
    return im
def render(name,slides,end):
    tmp=f'{OUT}/{name}_frames';os.makedirs(tmp,exist_ok=True);k=0
    for img,text,dur in slides:
        base=cover(f'{SRC}/{img}');n=int(dur*FPS)
        for i in range(n):
            z=1+0.05*i/n;cw,ch=int(base.width/1.06/z),int(base.height/1.06/z)
            x0=(base.width-cw)//2;y0=(base.height-ch)//2
            sq=base.crop((x0,y0,x0+cw,y0+ch)).resize((SQ,SQ),Image.BILINEAR)
            fr=Image.new('RGB',(W,H),(248,240,234));fr.paste(sq,(0,TOP))
            fr=caption(fr,text,TOP-190,sz=66,bg=(140,58,74,255))
            fr=caption(fr,'BirthdayUniverse.co',TOP+SQ+70,sz=48,bg=(0,0,0,0),fg=(140,58,74))
            fr.save(f'{tmp}/{k:05d}.jpg',quality=90);k+=1
    ec=endcard(*end)
    for i in range(int(2.5*FPS)): ec.save(f'{tmp}/{k:05d}.jpg',quality=90);k+=1
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{tmp}/%05d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-movflags','+faststart',f'{OUT}/{name}.mp4'],check=True)
    subprocess.run(['rm','-rf',tmp])
H65=[f'h65_{i}.img' for i in range(1,7)];H60=[f'h60_{i}.img' for i in range(1,7)]
E65=('Hello Sixty-Five','Est. 1961 · 6 colours · S–3XL');E60=('Hello Sixty','Est. 1966 · 6 colours · S–3XL')
ADS={
 'ad1_gift_mom65':[(H65[0],"Mom's turning 65?",2.2),(H65[1],'Skip the candle.',2),(H65[2],'Get her something she’ll actually wear.',2.6),(H65[4],'Made to order, just for her.',2.4),(H65[5],'6 colours. S to 3XL.',2.2)],
 'ad2_self65':[(H65[3],'65 and not hiding it.',2.4),(H65[0],'Est. 1961.',1.8),(H65[2],'Still the main character.',2.4),(H65[1],'Hello, Sixty-Five.',2.2),(H65[5],'Celebrate every year of it.',2.4)],
 'ad3_pick_colour65':[(H65[0],'Which colour is SHE?',1.8)]+[(h,f'{i}. {c}',1.4) for i,(h,c) in enumerate(zip(H65,['Black','Blush Pink','Burgundy','White','Navy','Sage Green']),1)]+[(H65[2],'Comment her number',1.8)],
 'ad4_pov_daughter60':[(H60[0],"POV: you found the perfect gift for mom's 60th",2.8),(H60[2],'Not another candle.',2),(H60[3],'Not another mug.',2),(H60[4],'Something she’ll wear all year.',2.4),(H60[5],'Hello, Sixty.',2)],
 'ad5_sixty_fast':[(H60[1],'60 never looked this good.',2)]+[(h,'',0.9) for h in H60]+[(H60[0],'Hello Sixty. Est. 1966.',2)],
 'ad6_dont_wait':[(H65[1],'Her big birthday is coming up…',2.4),(H65[4],"Don't leave it to the last minute.",2.4),(H60[2],'Hello Sixty · Hello Sixty-Five',2.2),(H60[5],'Every age from 30 to 80.',2.2),(H65[3],'Order hers today.',2)],
}
for n,s in ADS.items():
    render(n,s,E60 if '60' in n and '65' not in n else E65);print(n)
