from django.conf.urls import url
from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   url(r'^$', views.home, name='home_page'),
   url(r'article/(?P<post_id>\d+)/$', views.post_show, name='post_show'),
   url(r'^login/$', auth_views.login, {'template_name':'user/login.html'}, name='login'),
   url(r'^logout/$', auth_views.logout, {}, name='logout')
]