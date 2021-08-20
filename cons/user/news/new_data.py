import requests
import re
from bs4 import BeautifulSoup
from conn import startdb


def getNew():
    url = 'https://yz.chsi.com.cn/kyzx/zcdh/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup)
    lis = soup.findAll('li')[:-6]
    # print(lis)
    # init
    db = startdb()
    tsql = 'truncate table news'
    cur = db.cursor()
    cur.execute(tsql)
    db.commit()
    db.close()

    for i in lis:
        time = i.find('span', class_='span-time').string
        title = i.find('a').string
        href = "https://yz.chsi.com.cn" + i.find('a').attrs['href']
        # print(time)
        # print(title)
        # print(href)
        db = startdb()
        c = db.cursor()
        sql = "insert into news values(null, '%s','%s','%s')"%(title, href, time)
        c.execute(sql)
        db.commit()
        db.close()

    print('最新政策新闻爬取成功')
    return True