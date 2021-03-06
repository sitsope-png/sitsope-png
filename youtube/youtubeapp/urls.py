
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('own', views.own, name='own'),

    path('', views.first, name='first'),
    path('home', views.index, name='home'),
    path('download/', views.download, name='download'),
    path('about', views.about, name='about'),
    path('error', views.about, name='error'),
    path('done', views.about, name='done'),

    path('online', views.online, name='online'),
    path('process_subscription/', views.process_subscription, name='process_subscription'),
    path('n',views.subscription, name='name'),
    path('download/<resolution>', views.yt_download_done, name='download_done'),
]