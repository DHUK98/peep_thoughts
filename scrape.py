from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import csv

def scrape_episodes():
    out = [] 

    base_url = 'https://transcripts.fandom.com'
    url = 'https://transcripts.fandom.com/wiki/Peep_Show'
    req = urllib.request.urlopen(url)
    page = req.read().decode('utf-8')
    soup = BeautifulSoup(page,'html.parser')

    trans = soup.find(id='mw-content-text')
    ols = trans.find_all('ol')

    for ol in ols:
        lis = ol.find_all('li')
        for li in lis:
            link = li.find('a')['href'] 
            out.append(base_url+link)         
    
    return out


def scrape_thoughts(url):
    out = []

    req = urllib.request.urlopen(url)
    page = req.read().decode('utf-8')
    soup = BeautifulSoup(page,'html.parser')
    
    trans = soup.find(id='mw-content-text')
    ps = trans.find_all('p')
   
    title = ps[0].find('b').get_text().strip()
    print(title)
    #  print(ps[1:])
    for p in ps[1:]:
        text = p.get_text().split(':')
        if len(text) < 2:
            continue
        character = text[0].strip()
        line = text[1]
        re_search = re.finditer(r'\(.*?\)', line)
        for item in re_search:
            thought = item.group(0).strip('()')
            out.append([title,character,thought])
    return out


with open('thoughts.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    urls = scrape_episodes()
    print("urls loaded")
    print()
    for url in urls:
        print(f"scraping {url}")
        thoughts = scrape_thoughts(url)
        print(f"scraped {len(thoughts)} thoughts")
        print()
        csvwriter.writerows(thoughts)
