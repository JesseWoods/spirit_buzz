from django.conf.urls import url
from spiritbuzz import views

urlpatterns = [
    url(r'^$', views.show_cart, {'template_name': 'cart/cart.html'}, name='show_cart')
]