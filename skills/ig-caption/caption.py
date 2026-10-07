#!/usr/bin/env python3
import argparse, json, re, sys

def lint(text, keywords=None):
    text=text.strip(); first=text.splitlines()[0] if text else ''
    visible=text[:125]
    hashtags=re.findall(r'(?<!\w)#\w+', text)
    ctas=re.findall(r'\b(comment|save|share|send|follow|dm|click|tap|visit|reply)\b', text, re.I)
    concrete=len(re.findall(r'\$?\b\d[\d,.]*%?\b|(?<!^)(?<!\n)\b[A-Z][a-z]{2,}\b', visible))
    kws=[k.strip() for k in (keywords or []) if k.strip()]
    missing=[k for k in kws if k.lower() not in text.lower()]
    return {
      'length':len(text),'visible_preview':visible,'first_line_chars':len(first),
      'first_line_cut_risk':len(first)>125,'hashtags':hashtags,'hashtag_count':len(hashtags),
      'cta_terms':ctas,'cta_term_count':len(ctas),'concrete_markers_visible':concrete,
      'missing_keywords':missing
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input', nargs='?', default='-'); ap.add_argument('--keywords', default=''); ap.add_argument('--json', action='store_true'); a=ap.parse_args()
    text=sys.stdin.read() if a.input=='-' else open(a.input,encoding='utf-8').read()
    r=lint(text,a.keywords.split(',') if a.keywords else [])
    if a.json: print(json.dumps(r,indent=2,ensure_ascii=False)); return
    print('WHAT THE FEED SHOWS\n'+r['visible_preview']+(' ... more' if len(text)>125 else ''))
    print(f"\nlength: {r['length']} chars\nfirst line: {r['first_line_chars']} chars\nhashtags: {r['hashtag_count']}\nCTA terms: {r['cta_term_count']}\nconcrete markers in preview: {r['concrete_markers_visible']}")
    if r['missing_keywords']: print('missing keywords: '+', '.join(r['missing_keywords']))
if __name__=='__main__': main()
