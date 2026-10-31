"""Generate the public catalog from data/papers.json. Python standard library only."""
from pathlib import Path
import csv,json,re,collections,argparse
from render_readmes import build_readmes,pdf_link

ROOT=Path(__file__).resolve().parents[1]
FILES={'sampling':'sampling-and-decoding','computation':'conditional-computation','learning':'efficient-generators','foundations':'foundations','evaluation':'evaluation','surveys':'related-surveys','adjacent':'related-masked-generation','search':'related-search-budgets','excluded':'outside-core-scope','pending':'pending-mechanism-check','venue_pending':'other-publication-tracks','video':'video-generation','geometry':'3d-generation'}
def anchor(s):return re.sub(r'[^a-z0-9 -]','',s.lower()).replace(' ','-')
def safe(s):return s.replace('|','&#124;').replace('\n',' ')
def render(check=False):
    d=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))
    resources=json.loads((ROOT/'data/paper_resources.json').read_text(encoding='utf-8'))['papers']
    records=d['papers'];output={}
    def paper_pdf(p):return pdf_link({**p,'pdf_url':resources.get(p['id'],{}).get('pdf_url','')})or p['paper_url']
    decisions={k:[p for p in records if p['screening']['decision']==k] for k in ['core','background','pending']}
    lines=['# Papers by Year','','[Home](../README.md) · [By mechanism](README.md)','','Year follows the retained publication citation. A proceedings imprint can differ from the conference or first-online year. Publication years follow the entries below.','']
    for year in sorted({p['year'] for p in records},reverse=True):
        lines += [f'## {year}','']
        for p in sorted((p for p in records if p['year']==year),key=lambda p:p['title'].lower()):
            lines.append(f"- [{p['title']}]({paper_pdf(p)}). {p['venue']}."+(f" Scope: {p['collection_role']}." if p.get('collection_role') else ''))
        lines+=['']
    output['papers/by-year.md']='\n'.join(lines)
    lines=['# Papers by Publication Venue','','[Home](../README.md) · [By year](by-year.md)','','Venue names identify the publication record. They do not imply a cross-paper performance comparison. Proceedings imprint years can differ from conference and online-publication years.','']
    venues=collections.defaultdict(list)
    for p in records:venues[p['venue']].append(p)
    for v,ps in sorted(venues.items(),key=lambda z:z[0].casefold()):
        lines += [f'## {v}','','| Year | Paper | Scope or publication note |','|---|---|---|']
        for p in sorted(ps,key=lambda z:(-z['year'],z['title'].lower())):
            notes=p['collection_role']
            lines.append(f"| {p['year']} | [{safe(p['title'])}]({paper_pdf(p)}) | {safe(notes)} |")
        lines+=['']
    output['papers/by-venue.md']='\n'.join(lines)
    import io
    buf=io.StringIO(newline='');fields=['id','title','authors','year','venue','publication_status','publication_evidence_url','first_online_date','conference_year','publication_note','paper_url','doi','code_url','code_source_url','categories','collection_role','venue_policy','scope_reading_extent','scope_note','metadata_checked_on','code_checked_on']
    fields+=['decision','visual_output','accelerated_object','intervention','original_source_basis','cost_boundary','reading_extent','source_url','source_locator']
    w=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n');w.writeheader()
    for p in records:
        flat={**p,**p['screening'],'accelerated_object':p['screening']['accelerated_object_or_background_role']}
        w.writerow({k:('; '.join(flat[k]) if isinstance(flat.get(k),list) else flat.get(k,'')) for k in fields})
    output['data/papers.csv']=buf.getvalue()
    for key,ps in decisions.items():
        b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=list(records[0]['screening']),lineterminator='\n');w.writeheader();w.writerows(p['screening']for p in ps)
        output[f'data/{key}_papers.csv']=b.getvalue()
    for filename,ps in [('scope_decisions',records),('full_review_186',[p for p in records if p['screening']['cohort']=='original 186']),('followup_visual_20261031',[p for p in records if p['screening']['cohort']!='original 186'])]:
        b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=list(records[0]['screening']),lineterminator='\n');w.writeheader();w.writerows(p['screening']for p in ps)
        output[f'data/{filename}.csv']=b.getvalue()
    bib=[]
    for p in records:
        original=p['bibtex'];fields={**original['fields'],'url':p['paper_url']}
        bib += [f"@{original['type']}{{{p['id']},"]
        for i,(k,v) in enumerate(fields.items()):bib += ['  '+k+' = {'+v+'}'+(',' if i<len(fields)-1 else '')]
        bib+=['}','']
    output['references.bib']='\n'.join(bib)
    output['core_references.bib']='\n'.join(block for block in output['references.bib'].split('\n\n')if block and re.match(r'@\w+\{([^,]+),',block).group(1)in {p['id']for p in decisions['core']})+'\n'
    output.update(build_readmes(d,FILES,anchor,resources))
    import posixpath
    from urllib.parse import urlsplit
    for role in ['core','background','pending']:
        text=output[f'papers/{role}/README.md']
        def relocate(m):
            url=m.group(2)
            if urlsplit(url).scheme or url.startswith('#'):return m.group(0)
            return '['+m.group(1)+']('+posixpath.relpath(posixpath.normpath(posixpath.join('papers/'+role,url)),'papers')+')'
        output[f'papers/{role}.md']=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',relocate,text)
    drift=[]
    for rel,text in output.items():
        p=ROOT/rel
        if check:
            if not p.exists() or p.read_text(encoding='utf-8')!=text:drift.append(rel)
        else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8',newline='')
    if drift:raise SystemExit('Generated files need rebuilding: '+', '.join(drift))
    print(f'{len(records)} papers; {len(output)} generated files '+('match data.' if check else 'updated.'))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');render(ap.parse_args().check)
