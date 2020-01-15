import time

import jieba.analyse
from django.db import connection
from django.shortcuts import render, redirect,reverse

# Create your views here.
import MySQLdb
import MySQLdb.cursors
import datetime

from web.models import Search_Hash, Search_Keywords, Search_Statusreport, Search_Tags

sitename="锡纸花甲"







def index(request):
    # name = request.POST.get('info_hash')
    name = request.POST.get('name')
    print(name,'---------------')
    total = Search_Hash.objects.count()
    keywords = Search_Keywords.objects.filter().order_by()
    # today = Search_Statusreport.objects.query(sum('new_hashes')).filter(cast('date', Date) == datetime.date.today()).scalar()
    conn = {
        'total':total,
        'keywords':keywords,
        # 'today':today,
        'sitename': sitename
    }
    return render(request, 'index.html',conn)



def weekhot(request):
    weekhot = Search_Hash.objects.all()[:50]
    text = {
        'weekhot':weekhot,
        'sitename':sitename
    }
    return render(request,'weekhot.html',text)


def new(request):


    return render(request,'new.html')



def tag(request):

    return render(request,'tag.html')



def search_results(request):

    return render(request,'list.html')



def search_results_bylength(request):

    return render(request,'list_bylength.html')



def search_results_bycreate_time(request, page=1):


    return render(request,'list_bycreate_time.html')



# @cache.cached(timeout=60*60,key_prefix=make_cache_key)
def search_results_byrequests(request):



    return render(request,'list_byrequests.html')


def detail(request):

    result = Search_Tags.objects.all(info_hash)
    # if not result:
        # return redirect(reverse('web:index'))
    fenci_list = jieba.analyse.extract_tags(result['name'], 4)
    tags = Search_Tags.objects.order_by('id')[:20]
    text = {
        'tags': tags,
        'sitename': sitename,
        'result': result,
        'fenci_list': fenci_list
    }

    return render(request,'detail.html',text)






def notfound(request):
    return render(request,"404.html")
