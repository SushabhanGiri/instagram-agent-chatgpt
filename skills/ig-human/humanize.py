#!/usr/bin/env python3
import argparse, json, re, sys, unicodedata
from pathlib import Path
BASE=Path(__file__).resolve().parent
CFG=json.loads((BASE/'slop.json').read_text(encoding='utf-8'))
INVIS={chr(int(x,16)) for x in CFG['invisible_codepoints']}

def clean(s):
    changes=[]
    t=''.join(ch for ch in s if ch not in INVIS)
    if t!=s: changes.append('removed invisible formatting characters')
    repl={'—':', ','–':'-','“':'"','”':'"','‘':"'",'’':"'",'…':'...'}
    for a,b in repl.items():
        if a in t: t=t.replace(a,b); changes.append(f'normalized {a}')
    for p in CFG['phrases']:
        if re.search(re.escape(p),t,re.I): changes.append(f'flagged stock phrase: {p}')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r' *\n *','\n',t)
    return t.strip(),changes

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input',nargs='?',default='-'); ap.add_argument('--report',action='store_true'); a=ap.parse_args()
    raw=sys.stdin.read() if a.input=='-' else open(a.input,encoding='utf-8').read(); out,changes=clean(raw); print(out)
    if a.report:
        print('\n--- REPORT ---',file=sys.stderr)
        for c in changes: print('- '+c,file=sys.stderr)
if __name__=='__main__': main()
