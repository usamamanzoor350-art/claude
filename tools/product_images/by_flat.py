# Birth Year flat lay: same 3-shirt flat lay as Vintage, digits only, centred where the Vintage design sat
import sys,flat
D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/vintage_e_by/'
age,tag=sys.argv[1],sys.argv[2]
_ap=flat.apply
flat.apply=lambda im,m,f,cx,top,w,disp=0.5,opacity=0.97:_ap(im,m,f,cx,top,w,disp=0.1,opacity=0.99)  # thin lines stay crisp
flat.POS=[('black',210,410,'w'),('pink',558,451,'b'),('white',909,410,'b')]
flat.flat(D+f'{age}_black.png',D+f'{age}_white.png',f'final/{tag}_7_flatlay.jpg',178)
