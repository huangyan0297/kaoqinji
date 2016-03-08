#coding=utf-8
import urllib
import os
import webbrowser
import urllib2
import json
import requests
import random

class NetEase():
    def __init__(self):
        self.header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }


    def search_song(self, songs, sid=1, stype=1, offset=0, total='true', limit=60):
        base_url = "http://music.163.com/api/search/get"
        search_data = {'s': songs,
            'id':sid,
            'type':stype,
            'offset':offset,
            'total':total,
            'limit':limit,
            }
        connect = requests.post(base_url, data=search_data, headers=self.header)
        connect.encoding='utf-8'
        result_dict = json.loads(connect.text)

        
        if result_dict['code'] == 200:
            try:
                os.system("killall epiphany-browser")
            except:
                pass
            song_sum = len(result_dict['result']['songs'])                       #歌曲总数
            song_num = random.randint(0, song_sum-1)
            return result_dict['result']['songs'][song_num]['id']
        else:
            pass
        


        song_sum = len(result_dict['result']['songs'])                       #歌曲总数
        song_num = random.randint(0, song_sum)
        return result_dict['result']['songs'][song_num]['id']


    def get_music_url(self, songs):
        song_id = self.search_song(songs)
        music_url = "http://music.163.com/outchain/player?type=2&id=%s&auto=1" %song_id
        return music_url

if __name__ == '__main__':
    test = NetEase()
    music_url = test.get_music_url("南山南")
    webbrowser.get('epiphany').open(music_url, new=0, autoraise=False)

