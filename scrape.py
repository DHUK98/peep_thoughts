from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import csv


def scrape_thoughts(url):
    req = urllib.request.urlopen(url)
    page = req.read().decode('utf-8')
    soup = BeautifulSoup(page,'html.parser')
    
    trans = soup.find(id='mw-content-text')
    ps = trans.find_all('p')
   
    title = ps[0].find('b').get_text()
    print(title)
    #  for p in ps:
        #  print (p)
url = "https://transcripts.fandom.com/wiki/University_Challenge"
scrape_thoughts(url)
