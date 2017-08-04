import lxml
import requests
from bs4 import BeautifulSoup
def nyt():
    nysc = requests.get('https://www.nytimes.com/pages/opinion/index.html')
    nysp = BeautifulSoup(nysc.content, 'lxml')
    lk = nysp.select('#spanABCRegion > div.spanAB.wrap.module > div.cColumn > div > div >  h3 > a')
    lk2 = lk[0]['href']
    editHead = lk[0].text
    nysc1 = requests.get(lk2)
    nysp1 = BeautifulSoup(nysc1.content, 'lxml')
    editCnt = nysp1.find_all('p', class_="story-body-text story-content")
    ecBin = []
    for ec in editCnt:
        ecBin.append(ec.text)
    return([editHead,ecBin])

def thehindu():
    sc = requests.get('http://www.thehindu.com/opinion/')
    sp = BeautifulSoup(sc.text, 'lxml') 
    h1 = list(sp.find_all('h1'))

    editHead1 = h1[0].find('a').text
    ed1 = h1[0].find('a', href=True)['href']

    sc1 = requests.get(ed1) 
    sp1 = BeautifulSoup(sc1.text, 'lxml')
    ecBin1 = []
    for tx in sp1.find_all('p')[0:2]:
        ecBin1.append(tx.text)

    editHead2 = h1[1].find('a').text
    ed2 = h1[1].find('a', href=True)['href']

    sc2 = requests.get(ed2) 
    sp2 = BeautifulSoup(sc2.text, 'lxml')
    ecBin2 = []
    for tx in sp2.find_all('p')[0:2]:
        ecBin2.append(tx.text)
    return([editHead1,ecBin1, editHead2, ecBin2])

