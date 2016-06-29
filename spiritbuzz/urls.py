from django.conf.urls import patterns, url
from spiritbuzz import views
from spirit_buzz import settings

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^category/(?P<category_slug>[-\w]+)/$', views.category, name='category'),
    #url(r'^category/(?P<category_slug>[-\w]+)/product/(?P<product_slug>[-\w]+)/$', views.product, name ='product'),
    url(r'^review/product/add/$','add_review'),
    )

