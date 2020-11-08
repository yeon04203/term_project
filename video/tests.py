# video/urls.py
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.video_list, name='list'),
    # 아래 코드 추가하기
    url(r'^new$', views.video_new, name='new'),
]