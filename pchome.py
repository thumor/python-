# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:18:46 2024

@author: Hank
"""

from bs4 import BeautifulSoup 
import requests
import json
import pandas as pd
import time
keyword = '鞋櫃'
# 要抓取的網址
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q='+keyword+'&page=1&sort=sale/dc'
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
getdata = json.loads(list_req.content)
# 蒐集多頁的資料，打包成csv檔案
alldata = pd.DataFrame() # 準備一個容器
for i in range(1,10):
    # 要抓取的網址
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q='+keyword+'&page='+str(i)+'&sort=sale/dc'
    #請求網站
    list_req = requests.get(url)
    #將整個網站的程式碼爬下來
    getdata = json.loads(list_req.content)
    todataFrame = pd.DataFrame(getdata['prods']) # 轉成Dataframe格式
    alldata = pd.concat([alldata, todataFrame]) # 將結果裝進容器
    ##time.sleep(5) #拖延時間
# 儲存檔案
alldata.to_csv('PChome.csv', # 名稱 
               encoding='utf-8-sig', # 編碼 
               index=False) # 是否保留Index