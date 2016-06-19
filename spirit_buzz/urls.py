from django.conf.urls import url
from django.contrib import admin
from spiritbuzz import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns +=[
    # Examples:
    #url(r'^$', 'spirit_buzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^spiritbuzz/', spiritbuzz.urls),
    url(r'^spiritbuzz/$', views.index, name='index'),
    url(r'^spiritbuzz/category/(?P<category_slug>[-\w\d\_]+)/$', views.category, name='category'),
    url(r'^spiritbuzz/category/(?P<category_slug>[-\w\d\_]+)/product/(?P<product_slug>[-\w\d\_]+)/$', views.product, name ='product'),
    url(r'^login/', views.user_login, name = 'login'),
]