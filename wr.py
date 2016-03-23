#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup

base_url = 'http://www.wordreference.com'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8"
}

parser = argparse.ArgumentParser()
parser.add_argument('from_to')
parser.add_argument('word')
args = parser.parse_args()

url = base_url + '/' + args.from_to + '/' + args.word

r = requests.get(url, headers=headers)
html = r.text

soup = BeautifulSoup(html, 'lxml')

results = []
result = {}
for tr in soup.select('table.WRD tr'):
    if 'class' not in tr.attrs or set(tr.attrs['class']).isdisjoint(set(['even', 'odd'])): continue
    for td in tr.select('td'):
        if 'class' in td.attrs:
            if td.attrs['class'][0] == 'FrWrd':
                if result:
                    results.append(result)
                    result = {}
                result['word'] = ' '.join(td.strong.stripped_strings)
                result['trans'] = []
            elif td.attrs['class'][0] == 'ToWrd':
                s = list(td.strings)
                result['trans'].append(s[0])
        else:
            if td.string:
                s = str(td.string).strip()
                if s.startswith('('):
                    result['syn'] = s
if result:
    results.append(result)

for result in results:
    header = result['word']
    if 'syn' in result:
        header = header + " " + result['syn']
    print()
    print(header)
    for trans in result['trans']:
        print("    %s" % trans)
