import requests
from bs4 import BeautifulSoup
import re

# G
from conn import startdb

type = 'zs'
first = '艺术学'
second = '艺术'


def getDetail(url):
    # url = 'https://yz.chsi.com.cn/zyk/specialityDetail.do?zymc=%e4%b8%ad%e5%9b%bd%e5%93%b2%e5%ad%a6&zydm=010102&cckey=10&ssdm=&method=distribution#zyk-zyfb'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    li = soup.find_all('li')
    # print(li)
    res = []
    for i in li:
        n = re.findall('<li\stitle="(.*?)">', str(i))
        if(len(n)>0):
            res.append(n[0])
    return '-'.join(res)

def getList():
    data = ''
    with open('t', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            data += line
    soup = BeautifulSoup(data, "lxml")
    aa = soup.findAll('tr')
    for x in aa[1:]:
        xx = x.findAll('td')
        pat_href = "a\shref=\"(.*?)\""
        pat_code = "\d{4}.."
        pat_xk = "[\u4e00-\u9fa5]+"
        xk = re.findall(pat_xk,str(xx))[0]
        href = "https://yz.chsi.com.cn"+str(re.findall(pat_href, str(xx))[0]).replace('amp;', '')
        code = re.findall(pat_code, str(xx))[0]
        school_list = getDetail(href)
        db = startdb()
        cur = db.cursor()
        sql = "insert into majorall values(null,'%s','%s','%s','%s','%s','%s')" % (type, first, second, xk, code, school_list)
        print(sql)
        cur.execute(sql)
        db.commit()
        # print(xk, href, code)
        # print(school_list)
        import time
        time.sleep(2)
    return 0
getList()

def dump():

    getList()
    pass
