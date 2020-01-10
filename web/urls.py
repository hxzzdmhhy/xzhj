from django.urls import path
from web import views

app_name = 'cms'

urlpatterns = [
    path('', views.index, name='index'),
    ]