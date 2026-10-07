#!/usr/bin/env python3
import argparse, json, re, statistics, sys
from pathlib import Path
CFG=json.loads((Path(__file__).resolve().parent/'slop.json').read_text(encoding='utf-8'))
def score(t):
    sentences=[x.strip() for x in re.split(r'[.!?]+',t) if x.strip()]
    lens=[len(re.findall(r"[\w'$%’-]+",x)) for x in sentences] or [0]
    burst=min(100, 40+statistics.pstdev(lens)*8)
    concrete=min(100, len(re.findall(r'\$?\b\d[\d,.]*%?\b|(?<!^)(?<!\n)\b[A-Z][a-z]{2,}\b',t))*10)
    slop=sum(len(re.findall(re.escape(p),t,re.I)) for p in CFG['phrases'])
    slop_score=max(0,100-slop*18)
    fingerprint=100 if not re.search(r'[\u200b\u200c\u200d\u2060\ufeff\u00ad]',t) else 20
    overall=round((burst+concrete+slop_score+fingerprint)/4,1)
    return {'burstiness':round(burst,1),'specificity':round(concrete,1),'slop_cleanliness':slop_score,'fingerprint':fingerprint,'human_style_score':overall,'note':'heuristic style score, not an AI detector'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input',nargs='?',default='-'); a=ap.parse_args(); t=sys.stdin.read() if a.input=='-' else open(a.input,encoding='utf-8').read(); print(json.dumps(score(t),indent=2))
if __name__=='__main__': main()
