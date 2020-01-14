from django.urls import path
from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('weekhot/', views.weekhot, name='weekhot'),
    path('tag/', views.tag, name='tag'),
    path('search/', views.search_results, name='search'),
    path('search_results_bylength/', views.search_results_bylength, name='search_results_bylength'),
    path('search_results/', views.search_results, name='search_results'),
    path('search_results_bycreate_time/', views.search_results_bycreate_time, name='search_results_bycreate_time'),
    path('search_results_byrequests/', views.search_results_byrequests, name='search_results_byrequests'),

    ]