from django.conf.urls import patterns, url
from spiritbuzz import views
from spirit_buzz import settings

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^category/(?P<category_slug>[-\w]+)/$', views.category, name='category'),
    #url(r'^category/(?P<category_slug>[-\w]+)/product/(?P<product_slug>[-\w]+)/$', views.product, name ='product'),
    url(r'^login/', views.user_login, name = 'login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^aboutus/', views.aboutus, name = 'aboutus'),
    url(r'^results/$', views.results, {'template_name': 'spiritbuzz/results.html'}, name = 'search_results'),
    url(r'^review/product/add/$','add_review'),
    )

