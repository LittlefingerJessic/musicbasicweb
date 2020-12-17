import logging
import time

import pymysql
import requests
from pyquery import PyQuery as pq
from selenium.webdriver.chrome.options import Options
import multiprocessing
from selenium import webdriver
import pymongo
#client=pymongo.MongoClient(host='localhost',port=27017)
#db=client['你好']
#collections=db['mp3']
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='@10081.com', database='song',charset='utf8')
b=0
cursor=conn.cursor()
chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome('/Users/v/Downloads/chromedriver')
def main(n):
    try:
        url='http://www.9ku.com/geshou/%s.htm'%n
        a=requests.get(url).text
        doc=pq(a)
        headpicture=doc('.t-i img').attr('src')
        rank=doc('.singerInfo .rankIcon').text().split('P')[1].split('名')[0]
        paihang=int(rank)
        gequurls=doc('.singerMusic li div a').items()
        i=0
        for xx in gequurls:
            ac='http://www.9ku.com'+xx.attr('href')
            browser.get(ac)
            browser.find_element_by_css_selector('#jp_container_1 > div > div.jp-interface.clearfix > div.playerMain-03 > div.fr > ul > li:nth-child(1) > a').click()
            browser.get(ac)
            browser.find_element_by_css_selector('#songlist > li:nth-child(1) > a.name').click()
            html = browser.page_source
            doc1 = pq(html)
            singer = doc1('.playingTit h2 a').text()
            song = doc1('.playingTit a h1').text()
            lrc = doc1('#lrctext textarea').text()
            mp3 = doc1('#ku-player audio').attr('src')
            data={}
            '''data['song']=song
            data['lrc']=lrc
            data['mp3']=mp3
            data['singer']=singer
            data['headphoto']=headpicture
            data['rank']=paihang'''
            sql_insert = 'insert into app01_mp3(singer,song,hp,mp3,`rank`,lrc) values(%s,%s,%s,%s,%s,%s)'
            try:
                cursor.execute(sql_insert, (singer, song, headpicture, mp3, paihang, lrc))
                conn.commit()
                '''collections.update_one({
            'song': data.get('song')
        }, {
            '$set': data
        }, upsert=True)'''
                i += 1
                logging.info('这是目前排行第%s名的歌手%s第%s首歌曲%s'%(paihang,singer,i,song))
            except:
                browser.get(ac)
                browser.find_element_by_css_selector('#jp_container_1 > div > div.jp-interface.clearfix > div.playerMain-03 > div.fr > ul > li:nth-child(1) > a').click()
                browser.find_element_by_css_selector('#songlist > li:nth-child(1) > a.name').click()
                html = browser.page_source
                # print(html)
                doc1 = pq(html)
                singer = doc1('.playingTit h2 a').text()
                song = doc1('.playingTit a h1').text()
                lrc = doc1('#lrctext textarea').text()
                mp3 = doc1('#ku-player audio').attr('src')
                data = {}
                data['song'] = song
                data['lrc'] = lrc
                data['mp3'] = mp3
                data['singer'] = singer
                data['headphoto'] = headpicture
                sql_insert = 'insert into app01_mp3(singer,song,hp,mp3,`rank`,lrc) values(%s,%s,%s,%s,%s,%s)'
                try:
                    cursor.execute(sql_insert, (singer, song, headpicture, mp3, paihang, lrc))
                    conn.commit()
                    '''collections.update_one({
                        'song': data.get('song')
                    }, {
                        '$set': data
                    }, upsert=True)'''
                    i += 1
                    logging.info('这是%s的第%s首歌曲' % (singer, i))
                except:
                    print('怎么又失败了')
        #browser.close()
    except:
        print('404')
if __name__=='__main__':
    nums=[592]
    '''pool=multiprocessing.Pool(processes=12)
    nums=range(1,73500)  
    pool.map(main,nums)
    pool.close()'''
    #conn.close()
    for n in nums:
        main(n)
    browser.close()