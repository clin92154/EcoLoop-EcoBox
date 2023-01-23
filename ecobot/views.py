from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from .models import *
from orders.models import *
from .getOrders import *

from liffpy import (
    LineFrontendFramework as liff,
    ErrorResponse
)


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
liff_api = liff(settings.LINE_CHANNEL_ACCESS_TOKEN)
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:

            Events = {FollowEvent:'加入好友',
            UnfollowEvent:'取消好友',
            JoinEvent:'進入群組',
            LeaveEvent:'離開群組',
            MemberJoinedEvent:'有人入群',
            MemberLeftEvent:'有人退群',
            PostbackEvent:'PostbackEvent'}
            if isinstance(event, MessageEvent):

                # print(event.message.type)
                
                # text=event.message.text #文字訊息
                uid=event.source.user_id  #ID訊息
                # profile=line_bot_api.get_profile(uid) #ID簡介
                # name=profile.display_name #ID 名稱
                # pic_url=profile.picture_url 

                if event.message.type == 'text' and event.message.text in ["查詢目前訂單"]:
                    message =  getOrder(event.source.user_id)
                elif event.message.type == 'text' and event.message.text in ["歸還"]:
                    message = returnBox(event.source.user_id)
                elif event.message.type == 'text' and "Order" in event.message.text:
                    message = DelOrder(uid,event.message.text)
                elif event.message.type == 'text' and event.message.text in ["建立新訂單"]:
                    message =  getNewOrder(event.source.user_id) 

                                
            else: 
                for event,message in Events.items():
                    if isinstance(events,event):
                        message.append(TextSendMessage(text=message))


            line_bot_api.reply_message(event.reply_token,message)

                        
        return HttpResponse()
    else:
        return HttpResponseBadRequest()





def messageType(event):
    TextType = {
        'text':'文字訊息',
        'image':'圖片訊息',
        'location':'位置訊息',
        'video':'影片訊息',
        'sticker':'貼圖訊息',
        'audio':'聲音訊息',
        'file':'檔案訊息'
    }
    
    message = [TextSendMessage(text=TextType[event.message.type])]
    return message


def DeleteData(event):
    text=event.message.text #文字訊息
    uid=event.source.user_id  #ID訊息
    profile=line_bot_api.get_profile(uid) #ID簡介
    name=profile.display_name #ID 名稱
    pic_url=profile.picture_url #頭像
    message=[] #訊息內容

    #假設已經有使用者的ID時
    if User_Info.objects.filter(uid=uid).exists():
        message.append(TextSendMessage(text='正在進行刪除資料中')) 
        user_info = User_Info.objects.all().delete() #取得該會員資料
        message.append(TextSendMessage(text="已刪除完畢"))
        
    #否則，建立資料
    elif not(User_Info.objects.filter(uid=uid).exists()):
        message.append(TextSendMessage(text='目前尚未註冊資料'))

    return message


def SettingData(event):
    text=event.message.text #文字訊息
    uid=event.source.user_id  #ID訊息
    profile=line_bot_api.get_profile(uid) #ID簡介
    name=profile.display_name #ID 名稱
    pic_url=profile.picture_url #頭像

    message=[] #訊息內容

    #假設已經有使用者的ID時
    if User_Info.objects.filter(uid=uid).exists():
        message.append(TextSendMessage(text='已經有建立會員資料囉')) #訊息欄新增
        user_info = User_Info.objects.filter(uid=uid) #取得該會員資料
        for user in user_info: 
            info = f"""使用者ID:\n{user.uid}
            使用者名稱:\n{user.name}
            頭貼:\n{user.pic_url}
            """

            message.append(TextSendMessage(text=info))
    #否則，建立資料
    elif not(User_Info.objects.filter(uid=uid).exists()):
        User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,text=text)
        message.append(TextSendMessage(text='會員資料新增完畢'))

    return message