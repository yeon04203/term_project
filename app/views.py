from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Voca
from .models import Today
from .models import Profile
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm

try:
    from django.utills import simplejson as json
except ImportError:
    import json


def index(request):
    todays = Today.objects.order_by('?')[0]

    context = {"todays": todays}
    return render(request, 'index.html', context)


def voca(request):
    vocas = Voca.objects.all()
    paginator = Paginator(vocas, 10)
    now_page = request.GET.get('page')
    vocas = paginator.get_page(now_page)

    context = {"vocas": vocas}

    return render(request, 'voca.html', context)


def search(request):
    search_word = request.GET['search']
    # if ord('가') <= ord(search_word) <= ord('힣'):
    vocas = Voca.objects.filter(
        Q(mean__icontains=search_word) | Q(word__icontains=search_word))
    # else:
    #     vocas = Voca.objects.filter(word__icontains=search_word)

    # paginator=Paginator(vocas,5)
    # now_page=request.GET.get('page')
    # vocas=paginator.get_page(now_page)

    context = {"vocas": vocas}
    return render(request, 'search.html', context)


#단어 테스트임
def voca_test(request):
    vocas_test = Voca.objects.order_by('?')[0]
    context = {"vocas_test": vocas_test}

    return render(request, 'voca_test.html', context)


def test_result(request):
    user_test_point = Profile.objects.values('user_test_point')
    test_word = request.GET['test_word']
    test_mean = request.GET['mean']
    flag = "플래그"

    if test_mean == test_word:
        flag = "정답"
        user_test_point += 1
        # Profile.objects.values('user_test_point').update(user_test_point)
        context = {"flag": flag}

        return render(request, 'test_result.html', context)
    else:
        flag = "오답"
        context = {"flag": flag}
        context['mean'] = test_mean
        return render(request, 'test_result.html', context)


#----------------------------------


#단어 카테고리 나누기
def voca_cate(request):

    return render(request, 'voca_cate.html')


def voca_elementary(request):
    vocas = Voca.objects.all()
    vocas = Voca.objects.filter(grade='초등')

    paginator = Paginator(vocas, 5)
    now_page = request.GET.get('page')
    vocas = paginator.get_page(now_page)

    context = {"vocas": vocas}
    return render(request, 'voca_elementary.html', context)


def voca_high(request):
    vocas = Voca.objects.all()
    vocas = Voca.objects.filter(grade='중고')

    paginator = Paginator(vocas, 5)
    now_page = request.GET.get('page')
    vocas = paginator.get_page(now_page)

    context = {"vocas": vocas}
    return render(request, 'voca_high.html', context)


def voca_ma(request):
    vocas = Voca.objects.all()
    vocas = Voca.objects.filter(grade='전문')

    paginator = Paginator(vocas, 5)
    now_page = request.GET.get('page')
    vocas = paginator.get_page(now_page)

    context = {"vocas": vocas}
    return render(request, 'voca_ma.html', context)


#----------------------------------


def listen(request):

    return render(request, 'listen.html')


def write(request):

    return render(request, 'write.html')


def pronounce(request):

    return render(request, 'pronounce.html')


def user_profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request,
                             'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_profile.html', {'form': form})

    return render(request, 'user_profile.html')
