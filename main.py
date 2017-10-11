import requests
from bs4 import BeautifulSoup
import MySQLdb
import time

conn = MySQLdb.Connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'root',
    port = 3306,
    db = 'lichao',
    charset = 'utf8'
)
cur = conn.cursor()
sql = ('INSERT INTO `paper`(`title`,`URL`) VALUE (%s, %s);')

def foo():
    for x in range(100):
        url = 'http://python.jobbole.com/all-posts/page/{}/'.format(str(x))
        wb = requests.get(url)
        time.sleep(1)
        if wb.status_code == 200:
            print(x)
            GetUrl(url)
            conn.commit()
        else:
            cur.close()
            break

def GetUrl(url):
    wb = requests.get(url)
    wb.encoding = 'utf8'
    soup = BeautifulSoup(wb.text,'lxml')
    title = soup.select('#archive > div > div.post-meta > p > a.archive-title')
    for i in title:
        a = i.get_text()
        print(a)
        b = i.get('href')
        print(b)
        cur.execute(sql,(a,b))
        # WriteTxt(i.get_text(),i.get('href'))


# def WriteTxt(path,txt):
#     try:
#     	with open('/home/lichao/xxx/'+path+'.txt','w') as f:
#             f.write(txt)
#     except:
# 	    pass

foo()
