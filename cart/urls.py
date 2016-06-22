from django.conf.urls import url
from spiritbuzz import views
#app_name = 'polls'
urlpatterns = [
    url(r'^$', views.show_cart, {'template_name': 'cart/cart.html'}, name='show_cart')
]