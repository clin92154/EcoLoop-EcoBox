
from orders.models import  OrderItem


def getProduct(id):

    items = OrderItem.objects.filter(order=id)
    print(items)
    pass
    products =[

    ]

    for item in items:
        products.append(
            {
            "type": "box",
            "layout": "horizontal",
            "contents": [{
                    "type": "text",
                    "text": f'{item.product}*{item.quantity}',
                    "size": "xxs",
                    "color": "#555555",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": f"${item.get_cost()}",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }]}
        )


    return products


def bubble(order):
    items = getProduct(order)
    return {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [{
                    "type": "text",
                    "text": "RECEIPT",
                    "weight": "bold",
                    "color": "#1DB446",
                    "size": "sm"
                },
                {
                    "type": "text",
                    "text": f"訂單編號#{order.id}",
                    "weight": "bold",
                    "size": "xxl",
                    "margin": "none",
                    "flex": 10
                },
                {
                    "type": "text",
                    "text": f'收貨地址:{order.address}',
                    "size": "xs",
                    "color": "#aaaaaa",
                    "wrap": True,
                    "flex": 10
                },
                {
                    "type": "text",
                    "text": f'收貨人信箱:{order.email}',
                    "size": "xs",
                    "color": "#aaaaaa",
                    "wrap": True,
                    "flex": 10
                },{
                    "type": "text",
                    "text": f'收貨人:{order.name}',
                    "size": "xs",
                    "color": "#aaaaaa",
                    "wrap": True,
                    "flex": 10
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xxl",
                    "spacing": "sm",
                    "contents": [{
                            "type": "box",
                            "layout": "vertical",
                            "contents": items
                        },
                        {
                            "type": "separator",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [{
                                    "type": "text",
                                    "text": "TOTAL",
                                    "size": "sm",
                                    "color": "#555555"
                                },
                                {
                                    "type": "text",
                                    "text": f"${order.get_total_cost()}",
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "md",
                    "contents": [{
                            "type": "text",
                            "text": "PAYMENT ID",
                            "size": "xs",
                            "color": "#aaaaaa",
                            "flex": 0
                        },
                        {
                            "type": "text",
                            "text": f"#{order.id}",
                            "color": "#aaaaaa",
                            "size": "xs",
                            "align": "end"
                        }
                    ]
                }
            ]
        },

        "styles": {
            "footer": {
                "separator": True
            }
        }
    }