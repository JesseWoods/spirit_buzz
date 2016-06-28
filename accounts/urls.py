from django.conf.urls import url
from accounts import views
from spirit_buzz import settings
import django.contrib.auth.views as loginviews

urlpatterns = [
    url(r'^$', views.register, {'template_name': 'registration/register.html', 'SSL': settings.ENABLE_SSL}, name='register'),
    url(r'^my-account/$', views.my_account, {'template_name': 'registration/my_account.html'}, name='my_account'),
    url(r'^order-details/(?P<order_id>[-\w]+)/$', views.order_details, {'template_name': 'registration/order_details.html'}, name='order_details'),
    url(r'^order-info/$', views.order_info, {'template_name': 'registration/order_info.html'}, name='order_info'),
]
urlpatterns += [
    url(r'^login/$', loginviews.login, {'template_name': 'registration/login.html', 'SSL': settings.ENABLE_SSL}, name='login'),
    ]