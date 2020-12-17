import multiprocessing
import requests
from pyquery import PyQuery as pq
def main(n):
    try:
        url = 'http://www.9ku.com/geshou/%s.htm' % n
        a = requests.get(url).text
        doc = pq(a)
        headpicture = doc('.t-i img').attr('src')
        name=doc('.singerInfo h1').text()
        rank = doc('.singerInfo .rankIcon').text().split('P')[1].split('名')[0]
        paihang = int(rank)
        if paihang>0 and paihang <= 14700:
            aileaile=str(n)
            print(aileaile)
            with open('/Users/v/PycharmProjects/mp3/chooserank.txt','a') as f:
                f.write(aileaile+'\n')
                f.close()
        else:
            pass
    except:
        print('404')
if __name__=='__main__':
    pool=multiprocessing.Pool(processes=12)
    nums=range(1,73500)
    pool.map(main,nums)
    pool.close()
    #conn.close()
    '''for n in range(1,73500):
        main(n)'''
