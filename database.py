

import threading, time
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.utils import timezone


def start_thread():
    while True:
        print("시작")
        save()
        time.sleep(60)

def save():
    print('불러오는중')
    for item in stock_list():
        t = threading.Thread(target=save_thread,args=(item[0],item[1],))
        t.start()
    

def start():
    t = threading.Thread(target=start_thread)
    t.daemon = True 
    t.start()

def save_thread(name,codetemp):
    try:
        urlcode = "https://finance.naver.com/item/main.nhn?code="+codetemp
        html = urlopen(urlcode)
        bsObject = BeautifulSoup(html,"html.parser")
        result1 = bsObject.findAll("p")
        result2 = result1[7].find("span").text
        result3 = ""
        print(name+","+result2)
        for temp in result2:
            if temp>='0' and temp<='9':
                result3 = result3 + temp
        result = int(result3)
    except:
        print('오류발생! #'+name)
    #print(result)
    #views.db_save(code=codetemp,price=result)

def stock_list():
    result = [
        ['삼성전자','005930'],
        ['서울식품','004410'],
        ['기아차','000270'],
        ['대한항공','003490'],
        ['LG유플러스','032640'],
        ['한국전력','015760'],
        ['한화생명','088350'],
        ['휴온스','243070'],
        ['삼성중공업','010140'],
        ['흥국화재','000540'],
        ['LG전자','066570'],
        ['KT','030200'],
        ['두산','000150'],
    ]
    '''
        ['두산중공업','034020'],
        ['한화','000880'],
        ['현대차','005380'],
        ['SK하이닉스','000660'],
        ['녹십자','006280'],
        ['인터파크','035080'],
        ['카카오','035720'],
        ['빅히트','352820'],
        ['현대모비스','012330'],
        ['NAVER','035420'],
        ['신풍제약','019170'],
        ['세운메디칼','100700'],
        ['삼성물산','028260'],
        ['미래에셋대우','006800'],
        ['NH투자증권','005940'],
        ['현대해상','001450'],
        ['KB금융','115560'],
    ]
    '''
    return result