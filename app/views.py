from django.shortcuts import render
from .models import Voca
from .models import Blog
from django.core.paginator import Paginator

def index(request):
    return render(request,'index.html')

def voca(request):
    vocas=Voca.objects.all()
    paginator=Paginator(vocas,10)
    now_page=request.GET.get('page')
    vocas=paginator.get_page(now_page)

    context={
        "vocas":vocas
    }
    return render(request,'voca.html',context) 

def search(request):
    vocas=Voca.objects.all()
    search_word=request.GET['search']
    if ord('가')<=ord(search_word)<=ord('힣'): #한글이면 뜻으로 검색
        vocas=Voca.objects.filter(mean__icontains=search_word)
    else: #아니면(영어면) 단어로 검색-> 보완해야
        vocas=Voca.objects.filter(word__icontains=search_word)

    # paginator=Paginator(vocas,5)
    # now_page=request.GET.get('page')
    # vocas=paginator.get_page(now_page)

    context={
        "vocas":vocas
    }
    return render(request,'search.html',context)

def voca_elementary(request):
    vocas=Voca.objects.all()
    vocas = Voca.objects.filter(grade='초등')

    paginator=Paginator(vocas,5)
    now_page=request.GET.get('page')
    vocas=paginator.get_page(now_page)   

    context={
        "vocas":vocas
    }
    return render(request,'voca_elementary.html',context)

def voca_high(request):
    vocas=Voca.objects.all()
    vocas = Voca.objects.filter(grade='중고')

    paginator=Paginator(vocas,5)
    now_page=request.GET.get('page')
    vocas=paginator.get_page(now_page)  

    context={
        "vocas":vocas
    }
    return render(request,'voca_high.html',context)

def voca_ma(request):
    vocas=Voca.objects.all()
    vocas = Voca.objects.filter(grade='전문')

    paginator=Paginator(vocas,5)
    now_page=request.GET.get('page')
    vocas=paginator.get_page(now_page)  

    context={
        "vocas":vocas
    }
    return render(request,'voca_ma.html',context)
