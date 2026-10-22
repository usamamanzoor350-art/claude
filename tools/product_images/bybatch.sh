#!/bin/bash
# Birth Year render for one age dir: 6 model shots + flat lay + squares
S=/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad
d=$1;a=$2;cd $S/$d
cp $S/by_render.py $S/by_flat.py .; cp $S/flat_f.py flat.py; cp $S/h38/square.py $S/h38/place.py .
[ -f src_1293.png ] || cp $S/h38/src_1293.png $S/h38/fmask_*.png .
mkdir -p final sq
echo -n "$a: "; BYT=.30 BYV=.20 python3 by_render.py $a by$a
python3 by_flat.py $a by$a >/dev/null && python3 square.py by$a >/dev/null 2>&1
