#!/bin/bash
# usage: fprep.sh age "imgid:color ..."  -> save photos, measure, masks, render finger, sheet
S=/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad;I=/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/images
a=$1;d=$S/f$a;mkdir -p $d;cd $d
for p in $2; do python3 -c "from PIL import Image;im=Image.open('$I/${p%:*}.webp').convert('RGB');print(im.size,end=' ');im.save('src_${p#*:}.png')"; done
python3 ../geo2.py '[["src_black.png","black","round"],["src_white.png","white","v"],["src_pink.png","pink","v"],["src_sage.png","sage","round"],["src_burgundy.png","burgundy","round"],["src_navy.png","navy","v"]]' >/dev/null && cp $S/f56/mkmask.py . && python3 mkmask.py && cd $S && ./fbatch.sh f$a $a && python3 fsheet.py /home/user/claude/previews/finger_$a.jpg f$a:$a
