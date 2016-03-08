#coding=utf-8
import hashlib
import web
import time
import os
import urllib2,json
import lxml
from lxml import etree
import json
import urllib
import netEase

urls = ('/', "hello",
        "/weixin", "Weixin")
app = web.application(urls, globals())


class hello:
    def GET(self):
        return "hello"
    
class Weixin:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="youdao" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr     
  
        
    def POST(self):
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        msgType=xml.find("MsgType").text
        
        msgTypeDict = {'event': self.eventAction, 'text': self.textAction} #消息类型字典
        resContent = msgTypeDict[msgType](xml)
        return self.render.reply_text(fromUser,toUser,int(time.time()),resContent)
    
    def eventAction(self, xml): #事件消息处理
        if(xml.find("Event").text == 'subscribe'): #用户首次关注
            text = "你好，欢迎关注yaphone音乐播放器"
        return text    
    
    def textAction(self, xml): #文本信息处理
        content=xml.find("Content").text#获得用户所输入的内容
        music_box = netEase.NetEase()
        music_url = music_box.get_music_url(content)
        music_box.open_web(music_url)
        
        return "播放成功"
 
    
if __name__ == "__main__":
    app.run()