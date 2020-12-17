import re
import time
import pymysql
from selenium.webdriver.chrome.options import Options
import multiprocessing
from selenium import webdriver
import requests
from pyquery import PyQuery as pq
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='@10081.com', database='song',charset='utf8')
import os
def main(n):
    url= f'http://baidu.9ku.com/song/?key={n}'.format(n)
    #print(url)
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    browser=webdriver.Chrome('/Users/v/Downloads/chromedriver',chrome_options=chrome_options)
    browser.get(url)
    html=browser.page_source
    doc=pq(html)
    songlists=doc('.songList li').items()
    for song in songlists:
        xx=pq(song)
        songname=xx('.songName').text()
        singer=xx('.singerName').text()
        urx=xx('.songName').attr('href')
        print(urx)
        #print(urx)
        browser.get(urx)
        #time.sleep(1)
        #browser.find_element_by_css_selector('.ku-volume .jp-mute').click()
        time.sleep(1)
        browser.find_element_by_css_selector('#songlist > li:nth-child(1) > a.name').click()
        html1 = browser.page_source
        doc1 = pq(html1)
        singer1 = doc1('.playingTit h2 a').text()
        song1 = doc1('.playingTit a h1').text()
        lrc = doc1('#lrctext textarea').text()
        mp3 = doc1('#ku-player audio').attr('src')
        print(song1)
        cursor = conn.cursor()
        sql_insert = 'insert into app01_music(song,singer,lrc,mp3) values(%s,%s,%s,%s)'
        try:
            cursor.execute(sql_insert,(song1,singer1,lrc,mp3))
            conn.commit()
            print('1')
        except:
            print('失败')
    conn.close()
    browser.close()
if __name__=='__main__':
    with open('/Users/v/PycharmProjects/mp3/搜索文件.txt') as f:
        a=f.read()
        b=a.split('\n')
        for c in b:
            if len(c)>1:
                main(c)
    with open('/Users/v/PycharmProjects/mp3/搜索文件.txt','w') as f:
        f.write('')
        f.close()