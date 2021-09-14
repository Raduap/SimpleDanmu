import bilibili_api
import asyncio

from bilibili_api.live import LiveDanmaku
room = LiveDanmaku(room_display_id=4799254)
"""
DANMU_MSG: 用户发送弹幕
SEND_GIFT: 礼物
COMBO_SEND：礼物连击
GUARD_BUY：续费大航海
SUPER_CHAT_MESSAGE：醒目留言（SC）
SUPER_CHAT_MESSAGE_JPN：醒目留言（带日语翻译？）
WELCOME: 老爷进入房间
WELCOME_GUARD: 房管进入房间
PREPARING: 直播准备中
LIVE: 直播开始
INTERACT_WORD: 用户进入直播间
本模块自定义事件：
VIEW: 直播间人气更新
ALL: 所有事件
DISCONNECT: 断开连接（传入连接状态码参数）
TIMEOUT: 心跳响应超时
"""
@room.on("DANMU_MSG")  # 指定事件名
async def on_dan_mu(msg_json):
    # com = ''.join(msg_json) + ' '  # 内容
    u_name = msg_json['data']['info'][2][1]
    com = msg_json['data']['info'][1]
    print("收到弹幕:" + com)
    
    """if com[:2] == '*-':
        color = 'rgb(125, 0, 0)'
        msg = [color, f'{u_name}: {com}']
        dan_mu_msg.append(msg)"""

print("start connect")
asyncio.set_event_loop(asyncio.new_event_loop())
bilibili_api.sync(room.connect())

