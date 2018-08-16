'''
项目：命令行微信聊天室
流程：获取非公众号的所有消息-->选择名字进入对应的单独的"聊天室"-->实时获取双方聊天内容并在屏幕上显示


'''
import wxpy
import time
bot = wxpy.Bot()
mps = bot.mps()
friends_list = bot.friends()
msg_box = bot.messages

class Wechat():
    def __int__(self):
        pass

    def msgBox(self):
        if not msg_box:
            print('消息列表为空')
        else:
            for i in msg_box:
                if i.sender not in mps and i.sender != bot.self:
                    print(i+' | '+i.receive_time.strftime("%y-%m-%d,%H:%M"))
        msg_box_len = 0
        while True:                     #一直刷新，等到有新的消息时才打印
            if len(msg_box) != msg_box_len:
                msg = msg_box[msg_box_len:len(msg_box)]
                for i in msg:
                    print(i.sender.name+" : "+i.text+" | "+i.receive_time.strftime("%y-%m-%d %H:%M"))
                msg_box_len = len(msg_box)
            else:
                msg_box_len = len(msg_box)
            time.sleep(3)

if __name__ == "__main__":
    wechat = Wechat()
    wechat.msgBox()


