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
from abc import ABC, abstractmethod
from .bubble import *
import json

def SetOrder(order):
    return json.dumps(bubble(order))
    

def QueryOrder(uid):
    try:
        orders = [order for order in Order.objects.filter(uid=uid,returnable=True).order_by('-created')]
    except:
        orders=[]
    return orders

def DelOrder(uid,num):
    try:
        for order in QueryOrder(uid):
            print(order.id)
            print(int(num[-2:]))
            if order.id == int(num[-2:]):
                order.returnable = False
                order.save()
            # item.returnable=False
                return TextSendMessage(text=f"訂單編號:{order.id}\n歸還成功")
    except: 
        return TextSendMessage(text="歸還失敗")

def getNewOrder(uid):
    orders = QueryOrder(uid) #取得uid

    bubbles = []

    bubbles.append(json.loads(SetOrder(orders[0])))

    Carousel_template = FlexSendMessage(
                    alt_text = 'Order',
                    contents = {
                        "type": "carousel",
                        "contents": bubbles
                        }
                )
    return Carousel_template



def getOrder(uid):
    orders = QueryOrder(uid) #取得uid
    if len(orders)<1:
        return TextSendMessage(text="目前查無訂單!")


    bubbles = []

    for order in orders:
        bubbles.append(json.loads(SetOrder(order)))

    Carousel_template = FlexSendMessage(
                    alt_text = 'Order',
                    contents = {
                        "type": "carousel",
                        "contents": bubbles
                        }
                )
    return Carousel_template

    
    

def returnBox(uid):
    orders = QueryOrder(uid) #取得uid
    if len(orders)<1:
        return TextSendMessage(text="目前沒有訂單或是全數歸還!")

    actions = [MessageTemplateAction(
                                            label=f"#order:{order}",
                                            text=str(order)
                                        )
                for order in orders
    ]
    return TemplateSendMessage(
                                alt_text='Buttons template',
                                template=ButtonsTemplate(
                                    title='EcoBox歸還',
                                    text='請選擇歸還訂單箱子',
                                    actions=actions
                                )
                            )



    #判斷如果是未歸還箱子的，顯示要歸還的訂單編號
    #將訂單編號的returnable關掉後，回傳編號、訂單內容、箱子已歸還