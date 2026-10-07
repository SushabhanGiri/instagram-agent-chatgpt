#!/usr/bin/env python3
import argparse,csv,json,statistics,sys

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('--out'); a=ap.parse_args()
    with open(a.input,encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    out=[]
    for r in rows:
        try: mult=float(r['views'])/float(r['median']) if float(r['median']) else 0
        except: mult=0
        x=dict(r); x['outlier_multiple']=round(mult,2); out.append(x)
    out.sort(key=lambda r:r['outlier_multiple'],reverse=True)
    lines=['# Swipe file','']
    for r in out:
        lines.append(f"- **{r['outlier_multiple']}x** {r.get('account','')} — {r.get('hook','')} ({r.get('views','')} views; baseline {r.get('median','')})")
    text='\n'.join(lines)+'\n'
    if a.out: open(a.out,'w',encoding='utf-8').write(text)
    else: print(text)
if __name__=='__main__': main()
