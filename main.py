import requests
from bs4 import BeautifulSoup

def foo():
    for x in range(100):
        url = 'http://python.jobbole.com/all-posts/page/{}/'.format(str(x))
        wb = requests.get(url)
        if wb.status_code == 200:
            GetUrl(url)
        else:
            break

def GetUrl(url):
    wb = requests.get(url)
    wb.encoding = 'utf8'
    soup = BeautifulSoup(wb.text,'lxml')
    title = soup.select('#archive > div > div.post-meta > p > a.archive-title')
    for i in title:
        print(i.get_text())
        print(i.get('href'))

foo()