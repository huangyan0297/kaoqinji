#coding=utf-8
import urllib
import os
import webbrowser
import urllib2
import json
import requests

path = os.getcwd()

header1 = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }

raw_url = "http://music.163.com/api/search/get"
data1 = {'s': "南山南",
    'id':'1',
    'type':'1',
    'offset':'0', 
    'total':'true',
    'limit':'60',
    }
connect = requests.post(raw_url, data=data1, headers=header1)
connect.encoding='utf-8'

result_dict = json.loads(connect.text)
print result_dict['result']['songs'][0]['id']