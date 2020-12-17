import pymongo
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='@10081.com', database='song',charset='utf8')
cursor = conn.cursor()
client=pymongo.MongoClient('localhost',27017)
db=client['你好']
table=db['mp3']
data=list(table.find())
for i in data:
    singer=i.get('singer')
    song=i.get('song')
    hp=i.get('headphoto')
    mp3 = i.get('mp3')
    r = i.get('rank')
    lrc = i.get('lrc')
    if singer:
        #print(singer,song,hp,mp3,r,lrc)
        sql_insert ='insert into app01_mp3(singer,song,hp,mp3,`rank`,lrc) values(%s,%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql_insert,(singer,song,hp,mp3,r,lrc))
            conn.commit()
            print('保存成功')
        except:
            print('失败')
conn.close()