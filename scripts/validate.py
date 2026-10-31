"""Check catalog structure, local documentation links and generated-file consistency."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,re,collections,csv
from render import render,anchor,FILES
from render_readmes import pdf_link,md_title,SURVEY_TITLE,CORE_CATEGORIES

ROOT=Path(__file__).resolve().parents[1]
def validate():
    d=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'));ps=d['papers'];cats=d['categories']
    assert d['schema_version']==1
    ids=[p['id'] for p in ps];assert len(ids)==len(set(ids)),'Duplicate paper IDs'
    assert len({anchor(x)for x in ids})==len(ids),'Source-note anchor collision'
    titles=[re.sub(r'\W','',p['title']).casefold() for p in ps]
    assert len(titles)==len(set(titles)),'Duplicate normalized paper titles need review'
    dois=[p['doi'].lower().removeprefix('https://doi.org/') for p in ps if p.get('doi')]
    assert len(dois)==len(set(dois)),'Duplicate DOI'
    decisions=collections.Counter()
    for p in ps:
        assert all(p.get(k) for k in ['id','title','authors','year','venue','paper_url','categories','sections','bibtex']),p['id']
        assert isinstance(p['year'],int) and 1900<p['year']<2100,p['id']
        assert 'workshop' not in p['venue'].lower(),p['id']
        assert p.get('publication_status') in ['published','preprint_background'],p['id']
        for u in ['paper_url','code_url','code_source_url','publication_evidence_url']:
            if p[u]:
                s=urlsplit(p[u]);assert s.scheme=='https' and s.netloc and not re.search(r'\s',p[u]),(p['id'],u)
        assert bool(p['code_url'])==bool(p['code_source_url']),p['id']
        assert not p['code_url'] or p['code_checked_on'],p['id']
        for s in p['sections']:
            assert s['category'] in cats,p['id']
            assert not s['heading'] or s['heading'] in cats[s['category']]['subsections'],p['id']
        assert set(p['categories'])=={s['category'] for s in p['sections']},p['id']
        s=p['screening'];decision=s['decision'];decisions[decision]+=1
        assert decision in ['core','background','pending'],p['id']
        assert p['collection_role']==decision,p['id']
        for k in ['visual_output','accelerated_object_or_background_role','intervention','original_source_basis','cost_boundary','reading_extent','source_url','source_locator','publication_evidence_url','venue_eligibility','checked_on','cohort']:
            assert s.get(k),(p['id'],k)
        for k in ['source_url','publication_evidence_url']:
            u=urlsplit(s[k]);assert u.scheme=='https' and u.netloc,(p['id'],k)
        assert s['id']==p['id'] and s['title']==p['title'] and s['year']==p['year'] and s['venue']==p['venue'],p['id']
        if decision=='core':
            assert p['publication_status']=='published',p['id']
            assert set(p['categories'])<= {'sampling','computation','learning','search','video','geometry'},p['id']
        if decision=='pending':assert s['remaining_issue'],p['id']
        if any(c in p['categories'] for c in ['sampling','computation','learning','search','video','geometry']):assert decision=='core',p['id']
        for c in p['categories']:
            if cats[c]['subsections']:
                assert any(x['category']==c and x['heading']in cats[c]['subsections'] for x in p['sections']),(p['id'],'unrendered category assignment')
    originals=[p for p in ps if p['screening']['cohort']=='original 186']
    assert len(originals)==186,'Original cohort coverage changed'
    render(check=True)
    for filename,expected in [('full_review_186',originals),('core_papers',[p for p in ps if p['screening']['decision']=='core']),('scope_decisions',ps)]:
        rows=list(csv.DictReader((ROOT/f'data/{filename}.csv').open(encoding='utf-8-sig')))
        assert {p['id']for p in expected}=={r['id']for r in rows},filename
        assert len(rows)==len(expected),filename
    for fn,expected in [('references.bib',len(ps)),('core_references.bib',decisions['core'])]:
        assert len(re.findall(r'^@\w+\{', (ROOT/fn).read_text(encoding='utf-8'),re.M))==expected,fn
    resources=json.loads((ROOT/'data/paper_resources.json').read_text(encoding='utf-8'))['papers']
    assert set(resources)<=set(ids),'Resource link refers to an unknown paper'
    for id,resource in resources.items():
        u=urlsplit(resource['pdf_url']);assert u.scheme=='https' and u.netloc,id
        assert resource['link_source'],id
    def entry_prefix(p):
        copy={**p,'pdf_url':resources.get(p['id'],{}).get('pdf_url','')}
        return f"- [**{md_title(p['title'])}**]({pdf_link(copy)or p['paper_url']})"
    home_checks={}
    for fn in ['README.md','README.zh-CN.md']:
        text=(ROOT/fn).read_text(encoding='utf-8')
        assert text.startswith('# '+SURVEY_TITLE+'\n\n**Survey paper: Coming soon...**'),fn
        for p in ps:
            assert (entry_prefix(p)in text)==(p['collection_role']=='core'),(fn,p['id'])
        for cat in CORE_CATEGORIES:
            assert f'(papers/{FILES[cat]}/README.md)'in text,(fn,cat)
        home_checks[fn]=decisions['core']
    for cat in cats:
        text=(ROOT/f'papers/{FILES[cat]}/README.md').read_text(encoding='utf-8')
        for p in ps:
            assert (entry_prefix(p)in text)==(cat in p['categories']),(cat,p['id'])
    checked=0
    for p in ROOT.rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        for label,url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',text):
            if urlsplit(url).scheme:continue
            path,_,frag=unquote(url).partition('#');target=(p.parent/path).resolve() if path else p.resolve()
            assert target.is_relative_to(ROOT.resolve()) and target.exists(),(p,url)
            if frag and target.suffix=='.md':
                target_text=target.read_text(encoding='utf-8')
                headings=re.findall(r'^#+\s+(.+)$',target_text,re.M)
                explicit=set(re.findall(r'<a\s+(?:name|id)="([^"]+)"',target_text))
                assert frag in {anchor(h) for h in headings}|explicit,(p,url)
            checked+=1
    for fn in ['README.md','README.zh-CN.md']:
        assert str(len(ps)) in (ROOT/fn).read_text(encoding='utf-8'),fn+' paper count needs update'
    directory_path=ROOT/'data/complete_directory_entries_20261031.csv'
    if directory_path.exists():
        entries=list(csv.DictReader(directory_path.open(encoding='utf-8')))
        directory_ids={x['directory_id']for x in entries}
        assert len(directory_ids)==len(entries),'Duplicate directory-entry identity'
        sources=list(csv.DictReader((ROOT/'data/complete_directory_sources_20261031.csv').open(encoding='utf-8')))
        source_ids={x['source_id']for x in sources}
        assert len(source_ids)==len(sources),'Duplicate directory-source identity'
        assert all(x['source_id']in source_ids for x in entries),'Unresolved directory source'
        for x in entries:
            assert x['title']and x['title_individually_inspected']in['yes','no'],x['directory_id']
            if x['catalog_id']:assert x['catalog_id']in ids,x['directory_id']
        progress=list(csv.DictReader((ROOT/'data/complete_directory_progress_20261031.csv').open(encoding='utf-8')))
        observed=collections.Counter((x['venue'],x['year'])for x in entries)
        reported={(x['venue'],x['year']):int(x['directory_entries'])for x in progress}
        assert observed==reported,'Directory counts disagree with actual entries'
        directory_decisions=list(csv.DictReader((ROOT/'data/directory_candidate_decisions_20261031.csv').open(encoding='utf-8')))
        assert len({x['directory_id']for x in directory_decisions})==len(directory_decisions),'Duplicate source decision'
        assert all(x['directory_id']in directory_ids and x['original_source_basis']and x['source_locator']for x in directory_decisions),'Missing source-specific decision grounds'
        continuation_path=ROOT/'data/continuation_title_screening_20261031.csv'
        if continuation_path.exists():
            continuation=list(csv.DictReader(continuation_path.open(encoding='utf-8')))
            assert len({x['directory_id']for x in continuation})==len(continuation),'Duplicate continuation title'
            by_directory_id={x['directory_id']:x for x in entries}
            assert all(x['directory_id']in by_directory_id and by_directory_id[x['directory_id']]['title_individually_inspected']=='yes'for x in continuation),'Continuation reading missing from directory status'
            queued=list(csv.DictReader((ROOT/'data/continuation_source_queue_20261031.csv').open(encoding='utf-8')))
            decided={x['directory_id']for x in directory_decisions}
            assert all(x['directory_id']in directory_ids and x['directory_id']not in decided and not by_directory_id[x['directory_id']]['catalog_id']for x in queued),'Resolved or catalogued entry remains in new-source queue'
    # Generated-output navigation must cover exactly the admitted core papers.
    task_sets={}
    for task in ['image','video','3d']:
        text=(ROOT/f'papers/by-task/{task}/README.md').read_text(encoding='utf-8')
        selected={p['id']for p in ps if f'paper-notes.md#{anchor(p["id"])})'in text}
        assert selected and all(p['collection_role']=='core'for p in ps if p['id']in selected),task
        for p in ps:
            if p['id']in selected:assert p['screening']['source_locator']in text and p['screening']['source_url']in text,p['id']
        task_sets[task]=selected
    assert set.union(*task_sets.values())=={p['id']for p in ps if p['collection_role']=='core'},'Task navigation misses a core paper'
    assert not(task_sets['3d']&(task_sets['image']|task_sets['video'])),'3D entries mixed with image/video navigation'
    assert not list(ROOT.rglob('*.pdf')),'Unexpected PDF in public catalog'
    print(json.dumps({'papers':len(ps),'decisions':dict(decisions),'original_cohort':len(originals),'confirmed_code_links':sum(bool(p['code_url']) for p in ps),'pdf_resource_links':len(resources),'homepages_core_paper_coverage':home_checks,'category_readmes_checked':len(cats),'local_links_checked':checked,'category_counts_overlap':{k:sum(k in p['categories'] for p in ps) for k in cats},'generated_files_match':True},indent=2))
if __name__=='__main__':validate()
