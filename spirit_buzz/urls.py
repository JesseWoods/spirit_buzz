from django.conf.urls import include, url
from django.contrib import admin
from spiritbuzz import views

#from cart import urls
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns +=[
    # Examples:
    #url(r'^$', 'spirit_buzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^spiritbuzz/', spiritbuzz.urls),
    url(r'^spiritbuzz/$', views.index, name='spirit_buzz'),
    url(r'^spiritbuzz/category/(?P<category_slug>[-\w\d\_]+)/$', views.category, name='category'),
    url(r'^spiritbuzz/category/(?P<category_slug>[-\w\d\_]+)/product/(?P<product_slug>[-\w\d\_]+)/$', views.product, name ='product'),
    url(r'^spiritbuzz/cart/', include('cart.urls')),
    url(r'^spiritbuzz/checkout/', include('checkout.urls')),
    url(r'^spiritbuzz/accounts/', include('accounts.urls')),
    url(r'^spiritbuzz/accounts/', include('django.contrib.auth.urls')),
    url(r'^spiritbuzz/search/', include('search.urls')),
]