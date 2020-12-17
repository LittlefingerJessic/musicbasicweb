import random
from django.shortcuts import render, redirect,HttpResponse
from app01 import models
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='@10081.com', database='song',charset='utf8')
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        nickname=request.POST.get('nickname')
        password=request.POST.get('password')
        if nickname=='Tom' and password=='zhenwoyinyue':
            request.session['nickname']='Tom'
            return redirect('/%sindex'%nickname)
        else:
            msg='请核对你的账号密码再登陆'
            return render(request,'login.html',{'msg':msg})
def index(request):
    v=request.session.get('nickname')
    if v:
        return render(request,'websitindexpage.html')
    else:
        return redirect('/login')
def tom(request,a):
    v = request.session.get('nickname')
    if v:
        return render(request,'Tomindex.html')
def mymusic(request):
    v = request.session.get('nickname')
    if v:
        if request.method=='GET':
            msg=models.Mp3.objects.filter(song='他一定很爱你').first()
            return render(request,'mymusic.html',{'msg':msg})
        else:
            a=request.POST.get('searchyo')
            b=models.Mp3.objects.filter(song=a)
            c = models.Mp3.objects.filter(singer=a)
            if b:
                return render(request,'search.html',{'msg':b})
            if c:
                return render(request, 'search.html', {'msg': c})
            else:
                return render(request, 'search.html')
def sresult(request,ss):
    v = request.session.get('nickname')
    dt=ss.split('by')
    try:
        song=dt[0]
        singer=dt[1]
        if v:
            if request.method == 'GET':
                msg = models.Mp3.objects.filter(song=song, singer=singer).first()
                xp=models.AddList.objects.filter(song=song, singer=singer).first()
                if xp:
                    xxx = '爱你'
                    return render(request, 'mymusic.html', {'msg': msg,'tip':xxx})
                return render(request, 'mymusic.html', {'msg': msg})
            else:
                a = request.POST.get('searchyo')
                xf = request.POST.get('tight')
                xd = request.POST.get('tigh')
                xp = models.AddList.objects.filter(song=xf, singer=xd).first()
                xq=request.POST.get('forward')
                px=request.POST.get('back')
                xxx = '爱你'
                if xq:
                    qpo=models.AddList.objects.all()
                    i=0
                    for popo in qpo:
                        i+=1
                    xop=random.randint(1,i+1)
                    if xop==2:
                        msg = models.AddList.objects.filter(id=3).first()
                        return render(request, 'mymusic.html', {'msg': msg, 'tip': xxx})
                    else:
                        msg=models.AddList.objects.filter(id=xop).first()
                        return render(request, 'mymusic.html', {'msg': msg,'tip':xxx})
                if px:
                    qpo = models.AddList.objects.all()
                    i = 0
                    for popo in qpo:
                        i += 1
                    xop = random.randint(1, i + 1)
                    if xop == 2:
                        msg = models.AddList.objects.filter(id=3).first()
                        return render(request, 'mymusic.html', {'msg': msg, 'tip': xxx})
                    else:
                        msg = models.AddList.objects.filter(id=xop).first()
                        return render(request, 'mymusic.html', {'msg': msg, 'tip': xxx})
                if xp:
                    xxx='爱你'
                    return render(request, 'mymusic.html', {'msg': xp,'tip':xxx})
                if xf:
                    # print(xf,xd)
                    tips = '添加歌曲到歌单成功'
                    msg = models.Mp3.objects.filter(song=xf, singer=xd).first()
                    mi = models.Mp3.objects.filter(song=xf, singer=xd)
                    wuyu='爱你'
                    for dsf in mi:
                        models.AddList.objects.create(song=dsf.song,singer=dsf.singer,lrc=dsf.lrc,hp=dsf.hp,rank=dsf.rank,mp3=dsf.mp3)
                        print('建立数据成功')
                    # print(msg)
                    return render(request, 'mymusic.html', {'msg': msg, 'ms': tips,'tip':wuyu})
                else:
                    print('没有值')
                # print(a)
                b = models.Mp3.objects.filter(song=a)
                c = models.Mp3.objects.filter(singer=a)
                if b:
                    return render(request, 'search.html', {'msg': b})
                if c:
                    return render(request, 'search.html', {'msg': c})
                else:
                    return render(request, 'search.html')
    except:
        print('dds')
