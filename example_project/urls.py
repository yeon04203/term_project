"""example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name='index'),
    path('voca/', app.views.voca, name='voca'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('search/', app.views.search, name='search'),
    path('voca_elementary/', app.views.voca_elementary,
         name='voca_elementary'),
    path('voca_high/', app.views.voca_high, name='voca_high'),
    path('voca_ma/', app.views.voca_ma, name='voca_ma'),
    path('voca_test/', app.views.voca_test, name='voca_test'),
    path('test_result/', app.views.test_result, name='test_result'),
    path('listen/', app.views.listen, name='listen'),
    path('write/', app.views.write, name='write'),
    path('pronounce/', app.views.pronounce, name='pronounce'),
    path('voca_cate/', app.views.voca_cate, name='voca_cate'),
    path('user_profile/', app.views.user_profile, name='user_profile'),
]
