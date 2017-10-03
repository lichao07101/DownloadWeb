import requests
from bs4 import BeautifulSoup

url = 'http://python.jobbole.com/all-posts/page/2/'

wb = requests.get(url)
soup = BeautifulSoup(wb.text,'lxml')

print(soup.title)