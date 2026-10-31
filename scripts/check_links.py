"""Optional HTTP reachability check. HTTP status alone does not verify paper identity."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.error import HTTPError
import json,argparse,datetime,collections

ROOT=Path(__file__).resolve().parents[1]
def fetch(url):
    try:
        req=Request(url,headers={'User-Agent':'AwesomeARCatalogLinkCheck/1.0','Range':'bytes=0-2047'})
        with urlopen(req,timeout=12) as response:
            response.read(2048)
            return {'url':url,'status':response.status,'final_url':response.url,'result':'reachable'}
    except HTTPError as e:return {'url':url,'status':e.code,'result':'restricted_or_rate_limited' if e.code in [401,403,429] else 'needs_review'}
    except Exception as e:return {'url':url,'status':None,'result':'retrieval_failed','detail':str(e)}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='link_report.json');args=ap.parse_args()
    ps=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))['papers']
    urls=sorted({p[k] for p in ps for k in ['paper_url','code_url'] if p[k]})
    with ThreadPoolExecutor(max_workers=8) as ex:records=list(ex.map(fetch,urls))
    report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'HTTP reachability only, not publication metadata or claim support. A retrieval failure is not proof of an invalid citation.','counts':dict(collections.Counter(x['result'] for x in records)),'records':records}
    Path(args.output).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report['counts']))
