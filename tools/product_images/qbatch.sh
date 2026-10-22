#!/bin/bash
# usage: fbatch.sh dir age  -> finger render (6 models + flat lay + squares)
S=/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad
d=$1;a=$2;cd $S/$d
cp $S/queen_render.py $S/queen_flat.py .; cp $S/flat_f.py flat.py; cp $S/h38/square.py $S/h38/place.py . 2>/dev/null
[ -f src_1293.png ] || cp $S/h38/src_1293.png $S/h38/fmask_*.png .
mkdir -p final sq
python3 queen_render.py $a queen$a
python3 queen_flat.py $a queen$a
python3 square.py queen$a >/dev/null 2>&1
cd $S && python3 fixpad_q.py $d $a
echo
