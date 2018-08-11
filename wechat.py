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

if not msg_box:
    print('消息列表为空')
else:
    for i in msg_box:
        if i.sender not in mps and i.sender != bot.self:
            print(i+' | '+i.receive_time.strftime("%y-%m-%d,%H:%M"))
msg_box_len = 0
while True:                     #一直刷新，等到有新的消息时才打印
    if len(msg_box) != msg_box_len:
        print(msg_box[-1],msg_box[-1].receive_time.strftime("%y-%m-%d  %H-%M"))
        msg_box_len = len(msg_box)
    else:
        msg_box_len = len(msg_box)

        # for i in msg_box:
        #     if i.sender not in mps and i.sender != bot.self:
        #         print(i,i.receive_time.strftime("%y-%m-%d,%H:%M"))
    time.sleep(3)
## 存在问题：消息密集发送时显示的消息数量和顺序有误 2018.8.12


