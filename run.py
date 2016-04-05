#coding=utf-8
import itchat

import Lib.netEase as netEase

itchat.auto_login()

@itchat.msg_register('Text')
def music_player(msg):
    if msg['Text'] != u'关闭':
        music_box = netEase.NetEase()
        music_url = music_box.get_music_url(msg['Text'])
        music_box.open_web(music_url)
        return "播放成功"
    else:
        try:
            os.system('killall epiphany-browser')
            return "音乐已关闭"
        except:
            pass

itchat.run()
