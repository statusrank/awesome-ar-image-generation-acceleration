"""Build reader-facing Awesome-list homepages and category README files."""
from urllib.parse import urlsplit,urldefrag
import re

SURVEY_TITLE='Accelerating Autoregressive Image Generation: A Survey of Mechanisms, Guarantees, and Computational Trade-offs'
CORE_CATEGORIES=['sampling','computation','learning','video','geometry','search']
DESCRIPTIONS={
 'sampling':'Parallel evaluation, speculative decoding and generation scheduling.',
 'computation':'Feature reuse and selective execution, including attention-state storage.',
 'learning':'Efficient predictors and representations, including learned sampling procedures.',
 'video':'Acceleration of autoregressive video generation and streaming synthesis.',
 'geometry':'Acceleration of autoregressive 3D geometry, layouts and human motion.',
 'search':'Acceleration under a multi-path generation or test-time search budget.',
 'foundations':'Reference generators and supporting methods.',
 'evaluation':'Metrics and resources for evaluating generated images.',
 'surveys':'Related reviews of visual generation and efficient sampling.',
 'adjacent':'Related masked-generation methods outside the AR acceleration core.',
 'excluded':'Related papers outside the acceleration collection.',
 'pending':'Papers awaiting classification, excluded from the acceleration-paper count.',
 'venue_pending':'Publication tracks retained separately from the main collection.',
}
def display_heading(text):
    return text.replace('Other verified parallel sampling','Other parallel sampling')
def pdf_link(p):
    """Use an existing reading-source PDF, without guessing new download URLs."""
    for candidate in [p.get('pdf_url',''),p['screening']['source_url'],p['paper_url']]:
        candidate=urldefrag(candidate)[0]
        path=urlsplit(candidate).path.lower()
        if path.endswith('.pdf')or '/pdf/'in path or path.endswith('/pdf')or '/article/download/'in path:
            return candidate
    return ''

def md_title(s):
    return s.replace('[','\\[').replace(']','\\]').replace('\n',' ')

def public_location(text):
    text=re.sub(r';\s*abstract/selected method and performance passages.*','',text,flags=re.I)
    text=re.sub(r'\.?\s*(?:Table \d+ )?visually checked.*','',text,flags=re.I)
    text=re.sub(r'\s*,?\s*(?:abstract and selected passages|selected primary PDF passages|selected method passages)','',text,flags=re.I)
    return text.replace('Original PDF','PDF').replace('Official ECCV PDF','PDF').replace('Primary PDF','PDF').strip(' .;')

def paper_entry(p,note_prefix,details=False):
    pdf=pdf_link(p)
    title=f"[**{md_title(p['title'])}**]({pdf or p['paper_url']})"
    id=re.sub(r'[^a-z0-9 -]','',p['id'].lower()).replace(' ','-')
    lines=([f'<a id="paper-{id}"></a>','']if details else[])+[f"- {title} ({p['venue']}, {p['year']})."]
    if details:
        s=p['screening']
        lines += [f"  - **Focus:** {s['accelerated_object_or_background_role'].rstrip('.')}."]
        if p['collection_role']=='core':
            mechanism=s['intervention']
            if p['id']=='scalemogen_motion':mechanism='Predicts each skeletal-temporal scale from text and completed coarser token maps'
            lines += [f"  - **Mechanism:** {mechanism.rstrip('.')}."]
            location=public_location(s['source_locator'])
            if location:lines += [f"  - **Source location:** {location}."]
    return lines

def ordered(ps):
    return sorted(ps,key=lambda p:(-p['year'],p['title'].casefold()))

def build_readmes(d,files,anchor,resources=None):
    resources=resources or {};out={}
    ps=[{**p,'pdf_url':resources.get(p['id'],{}).get('pdf_url',p.get('pdf_url',''))}for p in d['papers']];cats={k:dict(v)for k,v in d['categories'].items()}
    cats['pending']['title']='Pending Papers'
    counts={k:sum(k in p['categories']for p in ps)for k in cats}
    roles={k:sum(p['collection_role']==k for p in ps)for k in ['core','background','pending']}
    def members(cat,h):return[p for p in ps if cat in p['categories']and(h=='Papers'or any(x['category']==cat and x['heading']==h for x in p['sections']))]
    def category(cat,nested):
        m=cats[cat];root='../../'if nested else'../'
        lines=[f"# {m['title']}",'',f'[Home]({root}README.md) · [Collections]({root}papers/README.md)','',DESCRIPTIONS[cat],'',f'**{counts[cat]} papers.**','']
        hs=[h for h in(m['subsections']or['Papers'])if members(cat,h)]
        if len(hs)>1:lines+=['## Contents','']+[f'- [{display_heading(h)}](#{anchor(display_heading(h))})'for h in hs]+['']
        for h in hs:
            lines +=[f'## {display_heading(h)}','']
            for p in ordered(members(cat,h)):lines+=paper_entry(p,'',True)+['']
        return'\n'.join(lines)
    for cat in cats:
        out[f'papers/{files[cat]}/README.md']=category(cat,True)
        out[f'papers/{files[cat]}.md']=category(cat,False)
    for role,title in [('core','All Acceleration Papers'),('background','Background and Related Work'),('pending','Pending Papers')]:
        chosen=[p for p in ps if p['collection_role']==role]
        lines=[f'# {title}','','[Home](../../README.md) · [Collections](../README.md)','',f'**{len(chosen)} papers.**','']
        if role=='pending':lines+=['Papers awaiting classification; excluded from the acceleration-paper count.','']
        tasks=sorted({p['screening']['visual_output']for p in chosen})
        lines +=[f'- [{t}](#{anchor(t)})'for t in tasks]+['']
        for t in tasks:
            lines +=[f'## {t}','']
            for p in ordered([p for p in chosen if p['screening']['visual_output']==t]):lines+=paper_entry(p,'',True)+['']
        out[f'papers/{role}/README.md']='\n'.join(lines)
    lines=[f'# {SURVEY_TITLE}','','**Survey paper: Coming soon...**','','A curated list of papers on accelerating autoregressive image and visual generation.','',
        '[All papers](papers/core/README.md) · [BibTeX](core_references.bib)','',
        '## Contents','','[Overview](#overview) · [Generated output](#generated-output) · [Categories](#categories) · [Paper list](#paper-list) · [Related work](#related-work) · [Resources](#resources)','',
        '## Overview','','Methods include faster sampling and decoding, reduced prediction cost, and efficient generator design. Image, video and 3D tasks have separate collections.','',f"**{roles['core']} acceleration papers.** Papers may appear in multiple categories.",'',
        '## Generated Output','','[Image generation](papers/by-task/image/README.md) · [Video generation](papers/by-task/video/README.md) · [3D and motion generation](papers/by-task/3d/README.md)','',
        '## Categories','','| Category | Focus | Papers |','|---|---|---:|']
    for c in CORE_CATEGORIES:lines.append(f"| [{cats[c]['title']}](papers/{files[c]}/README.md) | {DESCRIPTIONS[c]} | {counts[c]} |")
    lines+=['','### Subcategories','']
    for c in CORE_CATEGORIES:
        url=f'papers/{files[c]}/README.md';lines +=[f"- [{cats[c]['title']}]({url})"]
        for h in cats[c]['subsections']:
            if members(c,h):lines +=[f'  - [{display_heading(h)}]({url}#{anchor(display_heading(h))})']
    lines+=['','## Paper List','']
    for c in CORE_CATEGORIES:
        lines +=[f"### {cats[c]['title']}",'',f'[Mechanisms and papers](papers/{files[c]}/README.md)','']
        for p in ordered([p for p in ps if c in p['categories']]):lines+=paper_entry(p,'')
        lines +=['','[↑ Top](#contents)','']
    lines+=['## Related Work','',f"- [Background and related papers](papers/background/README.md) ({roles['background']}).",f"- [Related surveys](papers/{files['surveys']}/README.md).",f"- [Evaluation resources](papers/{files['evaluation']}/README.md).",f"- [Pending papers](papers/pending/README.md) ({roles['pending']}).",'',
        '## Resources','','- [All collections](papers/README.md) · [By year](papers/by-year.md) · [By venue](papers/by-venue.md).',f'- [Catalog](data/papers.csv): {len(ps)} records. [Acceleration-paper BibTeX](core_references.bib) · [Complete BibTeX](references.bib).',
        '- [Reading guide](docs/reading-guide.md) · [Scope](docs/inclusion-criteria.md) · [Contributing](CONTRIBUTING.md).','',
        '## Related Awesome Lists','','- [Awesome-VAR](https://github.com/zhanghm1995/Awesome-VAR).','- [Awesome Diffusion Models](https://github.com/diff-usion/Awesome-Diffusion-Models).','- [Awesome Multimodal Large Language Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models).','',
        '[CC BY 4.0](LICENSE.md) for documentation and catalog arrangement. [MIT](LICENSE-CODE) for maintenance scripts. Linked works retain their own licenses.','']
    out['README.md']='\n'.join(lines)
    lines=['# Paper Collections','','[Home](../README.md) · [By output](by-task/README.md) · [By year](by-year.md) · [By venue](by-venue.md)','',f"**{len(ps)} records:** {roles['core']} acceleration papers, {roles['background']} background papers and {roles['pending']} pending papers.",'','## Mechanisms','','| Category | Papers |','|---|---:|']
    for c in CORE_CATEGORIES:lines +=[f"| [{cats[c]['title']}]({files[c]}/README.md) | {counts[c]} |"]
    lines+=['','[Background](background/README.md) · [Pending](pending/README.md)',''];out['papers/README.md']='\n'.join(lines)
    labels={'image':['image','image super-resolution'],'video':['video','video view expansion','video avatar','video / scene forecasts'],'3d':['3D layout','3D point cloud','3D mesh','3D shape','3D geometry','3D scene layout','3D human motion','volumetric medical image synthesis'],'image_video':['image; video']}
    titles={'image':'Image Generation Acceleration','video':'Video Generation Acceleration','3d':'3D and Motion Generation Acceleration'};groups={k:[]for k in titles}
    for p in ps:
        if p['collection_role']!='core':continue
        found=[k for k,v in labels.items()if p['screening']['visual_output']in v]
        if len(found)!=1:raise ValueError('Unknown output label: '+p['id'])
        for t in(['image','video']if found[0]=='image_video'else found):groups[t].append(p)
    idx=['# Papers by Generated Output','','[Home](../../README.md) · [Mechanisms](../README.md)','','| Output | Papers |','|---|---:|']
    for t,title in titles.items():
        idx +=[f'| [{title}]({t}/README.md) | {len(groups[t])} |']
        lines=[f'# {title}','','[Home](../../../README.md) · [By output](../README.md) · [Mechanisms](../../README.md)','',f'**{len(groups[t])} acceleration papers.**','']
        for label in sorted({p['screening']['visual_output']for p in groups[t]}):
            lines +=[f'## {label}','']
            for p in ordered([p for p in groups[t]if p['screening']['visual_output']==label]):lines +=paper_entry(p,'',True)+['']
        out[f'papers/by-task/{t}/README.md']='\n'.join(lines)
    idx+=['','Multi-task papers appear in each applicable collection.',''];out['papers/by-task/README.md']='\n'.join(idx)
    return out
