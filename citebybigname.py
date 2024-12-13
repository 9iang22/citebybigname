# /usr/bin/python3
import json
import argparse
import requests
import subprocess
import os

def clone_github_repo(repo_url, destination_folder):
    try:
        subprocess.run(["git", "clone", repo_url, destination_folder], check=True)
        print(f"clone into {destination_folder}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"git clone error: {e}")
    except Exception as e:
        print(f"error: {e}")
    return False

def get_citeby_papers(doi):
    url = f"https://api.semanticscholar.org/v1/paper/{doi}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        citeby_papers = data.get('citations', [])
        
        citeby_list = []
        for paper in citeby_papers:
            paper_info = {
                'title': paper.get('title', 'N/A'),
                'authors': [author.get('name', 'N/A') for author in paper.get('authors', [])],
                'year': paper.get('year', 'N/A'),
                'venue': paper.get('venue', 'N/A'),
                'DOI': paper.get('doi', 'N/A')
            }
            citeby_list.append(paper_info)
        
        return citeby_list
    else:
        print(f"Error: {response.status_code}")
        return None

def is_fellow(name):
    n = {'name': name}
    n['fellow'] = []
    n['fellow_info'] = []
    for f in ieee:
        if n['name'] == f['name']:
            n['fellow'].append("IEEE_FELLOW")
            n['fellow_info'].append(f)
    for f in acm:
        if n['name'] == f['name'] :
            n['fellow'].append("ACM_FELLOW")
            n['fellow_info'].append(f)
    for f in aaas:
        if n['name'] == f['name']:
            n['fellow'].append("AAAS_FELLOW")
            n['fellow_info'].append(f)
    for f in aaai:
        if n['name'] == f['name']:
            n['fellow'].append("AAAI_FELLOW")
            n['fellow_info'].append(f)
    return n



parser = argparse.ArgumentParser(description='Find IEEE/ACM fellows in a citation list')
parser.add_argument('-d', '--doi', type=str, help='paper DOI', required=True)
parser.add_argument('-f', "--fellow", type=str, help="fellowship name, default = 'ACM, IEEE, AAAS, AAAI'", nargs='+', default=["ACM", "IEEE", "AAAS", "AAAI"])
parser.add_argument('--json', help='output in jsonl format', action='store_true')
args = parser.parse_args()

# thanks @xiaohk [https://github.com/xiaohk] for the data
db_url = "https://github.com/xiaohk/academic-awards.git"
db_dir = os.path.join(".", "academic-awards")
if not os.path.exists(db_dir):
    ok = clone_github_repo(db_url, db_dir)
    if not ok:
        exit(0)
# load data
ieee = json.load(open(os.path.join(db_dir, "data", "ieee-fellows.json"), encoding='utf-8'))
acm = json.load(open(os.path.join(db_dir, "data", "acm-fellow.json"), encoding='utf-8'))
aaas = json.load(open(os.path.join(db_dir, "data", "aaas-fellows.json"), encoding='utf-8'))
aaai = json.load(open(os.path.join(db_dir, "data", "aaai-fellows.json"), encoding='utf-8'))

print("Search DOI: " + args.doi)

# thanks free but powerful API from Semantic Scholar
cite = get_citeby_papers(args.doi)
if cite:
    for c in cite:
        authors = c['authors']
        for a in authors:
            f = is_fellow(a)
            if f['fellow'] != []:
                if args.json:
                    print(json.dumps({"citeby": c, "bigname":f}, indent=4))
                else:
                    print('---------------------------------')
                    print(f"CiteBy: {c['title']}")
                    print(f"BigName: {a}")
                    print(f"Fellowship: {set(f['fellow'])}")
                    print(f"Fellowship Info: {f['fellow_info']}")