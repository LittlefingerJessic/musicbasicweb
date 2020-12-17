import re
import pymysql
from selenium.webdriver.chrome.options import Options
import multiprocessing
from selenium import webdriver
import requests
from pyquery import PyQuery as pq
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='@10081.com', database='song',charset='utf8')
def getindex(url):
    result=requests.get(url).text
    doc=pq(result)
    href=doc('ol li a').items()
    for i in href:
        pattern=re.compile('href="(.*?)"',re.S)
        need=re.findall(pattern,str(i))
        for j in need:
            if 'play' in j:
                yield j
def main():
    url1 = 'http://www.9ku.com/zhuanji/75.htm'
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    browser=webdriver.Chrome('/Users/v/Downloads/chromedriver',chrome_options=chrome_options)
    for xx in getindex(url1):
        url='http://www.9ku.com'+xx
        browser.get(url)
        html=browser.page_source
        #print(html)
        doc=pq(html)
        singer=doc('.playingTit h2 a').text()
        song= doc('.playingTit a h1').text()
        lrc=doc('#lrctext textarea').text()
        mp3=doc('#ku-player audio').attr('src')
        print(mp3,song)
        '''cursor=conn.cursor()
        sql_insert ='insert into app01_music(song,singer,lrc,mp3) values(%s,%s,%s,%s)'
        try:
            cursor.execute(sql_insert,(song,singer,lrc,mp3))
            conn.commit()
            print('1')
        except:
            print('失败')
    conn.close()'''
if __name__=='__main__':
    main()