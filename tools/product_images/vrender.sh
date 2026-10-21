#!/bin/bash
# render only (geometry + masks already prepared)
S=/tmp/claude-0/-home-user-claude/c9e590a4-3afc-5ada-9071-97ba7f0cf5fc/scratchpad
d=$1;a=$2;cd $S/$d
python3 make_age.py vintage_e $a vint$a | tr '\n' ' '
python3 flat.py vintage_e $a vint$a 165 >/dev/null
python3 square.py vint$a >/dev/null 2>&1
cd $S && python3 fixpad.py $d $a >/dev/null
echo
