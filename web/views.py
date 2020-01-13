import time
from django.db import connection
from django.shortcuts import render

# Create your views here.
import MySQLdb
import MySQLdb.cursors
import datetime

sitename="锡纸花甲"







def index(request):


    return render(request, 'index.html')



def weekhot(request):

    return render(request,'weekhot.html')


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

    return render (request,'detail.html' )






def notfound(request):
    return render(request,"404.html")
