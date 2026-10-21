# flat lay: shirt body below armpit T=265px, armpits at y~470 (black/white), pink V-neck sits 41px lower
import sys,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import flat
from PIL import Image
D='/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad/designs/finger_z/'
age,tag=sys.argv[1],sys.argv[2]
im=Image.open(D+f'{age}_white.png');T=265;pw=(im.width/3)*T/715;h=pw*im.height/im.width
top=470-0.02*T-h/2;dx=0.035*T
flat.POS=[('black',210+dx,top,'w'),('pink',558+dx,max(top,432),'b'),('white',909+dx,top,'b')]
flat.flat(D+f'{age}_white.png',D+f'{age}_black.png',f'final/{tag}_7_flatlay.jpg',pw)
