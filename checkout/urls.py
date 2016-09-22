from django.conf.urls import url
from checkout import views
from spirit_buzz import settings

urlpatterns = [
    url(r'^$', views.show_checkout, {'template_name': 'checkout/checkout.html', 'SSL' : settings.ENABLE_SSL}, name = 'show_checkout'),
    url(r'^receipt/$', views.receipt, {'template_name': 'checkout/receipt.html', 'SSL': settings.ENABLE_SSL}, name = 'show_receipt'),
]


