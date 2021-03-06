from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from checkout.forms import CheckoutForm
from checkout.models import Order, OrderItem
from checkout import checkout
from cart import cart
from accounts import profile
# Create your views here.

def show_checkout(request, template_name = 'checkout/checkout.html'):

    if cart.is_empty(request):
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)

    if request.method =='POST':

        postdata = request.POST.copy()
        form = CheckoutForm(request.POST)


        if form.is_valid():

            response = checkout.process(request)
            order_number = response.get('order_number', 0)
            error_message = response.get('message', 0)

            if order_number:
                request.session['order_number'] = order_number
                receipt_url = urlresolvers.reverse('show_receipt')
                return  HttpResponseRedirect(receipt_url)

        else:
            #message = 'there is an error'
            error_message = 'Correct the errors below.'

    elif request.user.is_authenticated():
        user_profile = profile.retrieve(request)
        form = CheckoutForm(instance = user_profile)

    else:
        form = CheckoutForm()

    page_title = 'Checkout'

    return render_to_response(template_name, locals(), context_instance = RequestContext(request))

def receipt(request, template_name = 'checkout/receipt.html'):

    order_number = request.session.get('order_number')

    if order_number:
        order = Order.objects.filter(id = order_number)[0]
        order_items = OrderItem.objects.filter(order = order)
        del request.session['order_number']

    else:
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)

    return render_to_response(template_name, locals(), context_instance = RequestContext(request))

