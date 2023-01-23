from django.conf import settings
from decimal import Decimal
from django.shortcuts import render , get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
# Create your views here.
@csrf_exempt
def payment_done(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    return render(request, 'payment/done.html',{'order': order})