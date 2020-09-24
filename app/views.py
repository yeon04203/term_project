from django.shortcuts import render
from .models import Voca
from .models import Blog
from django.core.paginator import Paginator

def index(request):
    vocas=Voca.objects.order_by('?')[0]

    context={
        "vocas":vocas
    }
    return render(request,'index.html',context)

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

def voca_test(request):
    vocas=Voca.objects.order_by('?')[0]
    context={
        "vocas":vocas
    }

    return render(request,'voca_test.html',context)

def test_result(request):
    voca_test()
    test_word=request.GET['test_word']
    flag="정답"
    flag2="오답"
    if vocas.mean==test_word:
        context={
            "flag":flag
                }
        return render(request,'test_result.html',context)
    else:
        context={
            "flag":flag2
            }
        return render(request,'test_result.html',context)

    return render(request,'test_result.html')

def listen(request):

    return render(request,'listen.html')

def write(request):

    return render(request,'write.html')

def pronounce(request):

    return render(request,'pronounce.html')