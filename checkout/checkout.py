from cart import cart
from checkout.models import Order, OrderItem
from checkout.forms import CheckoutForm
from checkout import authnet
from spirit_buzz import settings
from django.core import urlresolvers
import urllib

def get_checkout_url(request):

    return urlresolvers.reverse('show_checkout')

def process(request):

    APPROVED = '1'
    DECLINED ='2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'
    postdata = request.POST.copy()
    card_num = postdata.get('credit_card_number', '')
    exp_month = postdata.get('credit_card_expire_month', '')
    exp_year = postdata.get('credit_card_expire_year', '')
    exp_date = exp_month + '-' + exp_year
    cvv = postdata.get('credit_card_cvv', '')
    amount = cart.cart_subtotal(request)
    results = {}
    response = authnet.do_auth_capture(amount = amount, card_num = card_num, exp_date = exp_date, card_cvv = cvv)

    if response[0] == APPROVED:
        transaction_id = response[6]
        order = create_order(request, transaction_id)
        results = {'order_number': order.id, 'message': ''}
    if response[0] == DECLINED:
        results = {'order_number':0, 'message': 'There is a problem with your credit card.'}
    if response[0] == ERROR or response[0] == HELD_FOR_REVIEW:
        results = {'order_number': 0 , 'message':'There was an error processing your order'}

    return results

def create_order(request, transaction_id):

    order = Order()
    checkout_form = CheckoutForm(request.POST, instance = order)
    order = checkout_form.save(commit = False)
    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED
    order.save()

    if order.pk:
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.save()
        cart.empty_cart(request)

        if request.user.is_authenticated():
            from accounts import profile
            profile.set(request)

    return order





def process2(request):

    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'
    #postdata = request.POST.copy()
    card_num = request.get('credit_card_number', '')
    exp_month = request.get('credit_card_expire_month', '')
    exp_year = request.get('credit_card_expire_year', '')
    exp_date = exp_month +'-'+ exp_year
    cvv = request.get('credit_card_cvv', '')
    amount = request.get('amount', '')
    results = {}
    response = authnet.do_auth_capture(amount = amount, card_num = card_num, exp_date = exp_date, card_cvv = cvv)

    if response[0] == APPROVED:
        transaction_id = response[6]
        order = create_order(request, transaction_id)
        results = {'order_number': order.id, 'message': ''}
    if response[0] == DECLINED:
        results = {'order_number':0, 'message': 'There is a problem with your credit card.'}
    if response[0] == ERROR or response[0] == HELD_FOR_REVIEW:
        results = {'order_number': 0 , 'message':'There was an error processing your order'}

    return (response, results)