from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.video_list, name='listen'),
    url(r'^new$', views.video_new, name='new'),
    # 이 코드를 추가해 주세요
    url(r'^(?P<video_id>\d+)/$', views.video_detail, name='detail'),
]