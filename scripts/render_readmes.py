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
 'geometry':'Acceleration of autoregressive 3D geometry and layout generation.',
 'search':'Acceleration under a multi-path generation or test-time search budget.',
 'foundations':'Reference generators and supporting methods.',
 'evaluation':'Metrics and resources for evaluating generated images.',
 'surveys':'Related reviews of visual generation and efficient sampling.',
 'adjacent':'Related masked-generation methods outside the AR acceleration core.',
 'excluded':'Historical records retained outside the core collection.',
 'pending':'Published candidates with unresolved mechanism or eligibility checks.',
 'venue_pending':'Publication tracks retained separately from the main collection.',
}
ZH_DESCRIPTIONS={
 'sampling':'并行评估、推测解码与生成调度。',
 'computation':'特征复用和选择性执行，涵盖注意力状态存储。',
 'learning':'高效预测器与视觉表示，涵盖学习得到的采样过程。',
 'video':'自回归视频生成与流式合成加速。',
 'geometry':'自回归三维几何与布局生成加速。',
 'search':'多路径生成或测试时搜索预算下的加速。',
}
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

def paper_entry(p,note_prefix,details=False):
    pdf=pdf_link(p)
    title=f"[**{md_title(p['title'])}**]({pdf or p['paper_url']})"
    links=[f"[Paper]({p['paper_url']})"]
    if pdf:links.append(f'[PDF]({pdf})')
    if p.get('code_url'):links.append(f"[Code]({p['code_url']})")
    if details:
        note_id=re.sub(r'[^a-z0-9 -]','',p['id'].lower()).replace(' ','-')
        links.append(f"[Details]({note_prefix}paper-notes.md#{note_id})")
    lines=[f"- {title} ({p['venue']}, {p['year']}). "+' · '.join(links)]
    if details:
        s=p['screening']
        label='Accelerates'if s['decision']=='core'else'Context'
        lines += [f"  - **{label}:** {s['accelerated_object_or_background_role']}."]
        if s['decision']=='core':lines += [f"  - **Approach:** {s['intervention']}."]
        if s['decision']=='pending':lines += [f"  - **To verify:** {s['remaining_issue']}"]
        if p.get('publication_note'):lines += [f"  - {p['publication_note']}"]
    return lines

def ordered(ps):
    return sorted(ps,key=lambda p:(-p['year'],p['title'].casefold()))

def build_readmes(d,files,anchor,resources=None):
    resources=resources or {}
    out={};ps=[{**p,'pdf_url':resources.get(p['id'],{}).get('pdf_url',p.get('pdf_url',''))}for p in d['papers']];cats=d['categories']
    counts={k:sum(k in p['categories']for p in ps)for k in cats}
    counts_by_role={k:sum(p['screening']['decision']==k for p in ps)for k in ['core','background','pending']}
    def section_members(cat,h):
        return [p for p in ps if cat in p['categories']and (h=='Papers'or any(x['category']==cat and x['heading']==h for x in p['sections']))]
    def category_page(cat,nested):
        m=cats[cat];rel='../../'if nested else'../';notes='../'if nested else''
        lines=[f"# {m['title']}",'',f'[Home]({rel}README.md) · [All categories]({rel}papers/README.md) · [By year]({rel}papers/by-year.md)','',DESCRIPTIONS[cat],'',f"**{counts[cat]} papers.** Titles link to recorded PDFs or the official paper page.",'']
        hs=m['subsections']or['Papers']
        hs=[h for h in hs if section_members(cat,h)]
        if len(hs)>1:lines += ['## Contents','']+[f'- [{h}](#{anchor(h)})'for h in hs]+['']
        for h in hs:
            lines += [f'## {h}','']
            for p in ordered(section_members(cat,h)):
                lines+=paper_entry(p,notes,details=True)+['']
        return '\n'.join(lines)
    for cat in cats:
        out[f'papers/{files[cat]}/README.md']=category_page(cat,True)
        out[f'papers/{files[cat]}.md']=category_page(cat,False)

    for role,title in [('core','All Core Acceleration Papers'),('background','Background and Related Work'),('pending','Pending Papers')]:
        chosen=[p for p in ps if p['screening']['decision']==role]
        lines=[f'# {title}','','[Home](../../README.md) · [Categories](../README.md) · [Source notes](../paper-notes.md)','',f'**{len(chosen)} papers.**','']
        if role=='pending':lines += ['These entries are separate from the core acceleration list. The outstanding check is stated beside each paper.','']
        tasks=sorted({p['screening']['visual_output']for p in chosen})
        lines += [f'- [{t}](#{anchor(t)})'for t in tasks]+['']
        for task in tasks:
            lines += [f'## {task}','']
            for p in ordered([p for p in chosen if p['screening']['visual_output']==task]):lines += paper_entry(p,'../',True)+['']
        out[f'papers/{role}/README.md']='\n'.join(lines)

    for lang in ['en','zh']:
        zh=lang=='zh'
        # English section headings provide identical stable anchors in both homepages.
        lines=[f'# {SURVEY_TITLE}','','**Survey paper: Coming soon...**','','A curated paper list on accelerating autoregressive image and visual generation.'if not zh else'自回归图像与视觉生成加速论文集。','',
            '[English](README.md) · [中文](README.zh-CN.md) · [Core papers](papers/core/README.md) · [BibTeX](core_references.bib)','',
            f"## Contents",'', '[Overview](#overview) · [Categories](#categories) · [Paper list](#paper-list) · [Background](#background-and-related-work) · [Resources](#resources)','',
            '## Overview','',
            '本仓库按具体加速机制组织论文，涵盖现有生成器的执行优化与高效生成器设计。视频和3D生成单独列出。'if zh else'This collection organizes acceleration methods by the computation they change. It covers execution improvements to existing generators and efficient generator design, with separate video and 3D collections.','',
            f"**{counts_by_role['core']} core papers.** "+('同一论文可以出现在多个相关分类。'if zh else'A paper can appear in more than one category.'),'',
            '## Categories','',
            '| 分类 | 主要内容 | 论文数 |'if zh else'| Category | Focus | Papers |','|---|---|---:|']
        for cat in CORE_CATEGORIES:
            desc=ZH_DESCRIPTIONS[cat]if zh else DESCRIPTIONS[cat]
            lines.append(f"| [{cats[cat]['title']}](papers/{files[cat]}/README.md) | {desc} | {counts[cat]} |")
        lines+=['','### Subcategories','']
        for cat in CORE_CATEGORIES:
            base=f'papers/{files[cat]}/README.md'
            lines += [f"- [{cats[cat]['title']}]({base})"]
            for h in cats[cat]['subsections']:
                if section_members(cat,h):lines += [f'  - [{h}]({base}#{anchor(h)})']
        lines+=['','## Paper List','',
            '点击论文标题可访问已记录的PDF链接。未取得PDF链接的条目跳转官方论文页面。各分类README提供具体干预对象和详细来源。'if zh else'Click a paper title for its recorded PDF link, or its official page when no PDF link is recorded. Category READMEs provide the specific intervention and source details.','']
        for cat in CORE_CATEGORIES:
            lines += [f"### {cats[cat]['title']}",'',f"[{'分类README与子分类'if zh else'Category README and subcategories'}](papers/{files[cat]}/README.md)",'']
            for p in ordered([p for p in ps if cat in p['categories']]):lines+=paper_entry(p,'papers/',details=False)
            lines += ['', '[↑ Top](#contents)','']
        lines += ['## Background and Related Work','',
            f"- [{'全部背景文献'if zh else'All background papers'}](papers/background/README.md) ({counts_by_role['background']}).",
            f"- [{'基础生成模型'if zh else'Foundations'}](papers/{files['foundations']}/README.md).",
            f"- [{'相关综述'if zh else'Related surveys'}](papers/{files['surveys']}/README.md).",
            f"- [{'评价资源'if zh else'Evaluation resources'}](papers/{files['evaluation']}/README.md).",
            f"- [{'相关非AR掩码生成'if zh else'Related non-AR masked generation'}](papers/{files['adjacent']}/README.md).",
            f"- [{'待核实论文'if zh else'Pending papers'}](papers/pending/README.md) ({counts_by_role['pending']}).",'',
            '## Resources','',
            '- [All papers](papers/README.md) · [By year](papers/by-year.md) · [By venue](papers/by-venue.md).',
            f"- [Full catalog](data/papers.csv): {len(ps)} records. [Core BibTeX](core_references.bib) · [Complete BibTeX](references.bib).",
            '- [Paper-level source notes](papers/paper-notes.md) · [Coverage](docs/coverage.md) · [Inclusion criteria](docs/inclusion-criteria.md).',
            '- [Full-directory follow-up](docs/directory-review-20261031.md) · [Per-entry reading status](data/complete_directory_progress_20261031.csv).',
            '- [Contributing](CONTRIBUTING.md) · [Maintenance](docs/maintenance.md) · [Changelog](CHANGELOG.md).','',
            '## Related Awesome Lists','',
            '- [Awesome-VAR](https://github.com/zhanghm1995/Awesome-VAR).',
            '- [Awesome Diffusion Models](https://github.com/diff-usion/Awesome-Diffusion-Models).',
            '- [Awesome Multimodal Large Language Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models).','',
            '[CC BY 4.0](LICENSE.md) for documentation and catalog arrangement. [MIT](LICENSE-CODE) for maintenance scripts. Linked works retain their own licenses.','']
        out['README.zh-CN.md'if zh else'README.md']='\n'.join(lines)
    # Category index resolves directly to category README files.
    lines=['# Paper Collections','','[Home](../README.md) · [Core papers](core/README.md) · [By year](by-year.md) · [By venue](by-venue.md)','',
        f"**{len(ps)} records:** {counts_by_role['core']} core, {counts_by_role['background']} background and {counts_by_role['pending']} pending.",'','## Acceleration Papers','','| Category | Papers |','|---|---:|']
    for cat in CORE_CATEGORIES:lines += [f"| [{cats[cat]['title']}]({files[cat]}/README.md) | {counts[cat]} |"]
    lines+=['','## Supporting Collections','']
    for cat in ['foundations','surveys','evaluation','adjacent']:
        lines += [f"- [{cats[cat]['title']}]({files[cat]}/README.md) ({counts[cat]})."]
    lines+=['','[All background](background/README.md) · [Pending papers](pending/README.md) · [Paper-level source notes](paper-notes.md)','']
    out['papers/README.md']='\n'.join(lines)
    return out
