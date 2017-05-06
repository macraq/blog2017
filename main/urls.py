from django.conf.urls import url
from main import views

urlpatterns = [
   url(r'^$', views.home, name='home_page'),
   url(r'article/(?P<post_id>\d+)/$', views.post_show, name='post_show')
]