
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('n/process_subscription/own', views.own, name='own'),

    path('', views.first, name='first'),
    path('n/process_subscription/home', views.index, name='home'),
    path('n/process_subscription/download/', views.download, name='download'),
    path('n/process_subscription/about', views.about, name='about'),
    path('n/process_subscription/error', views.about, name='error'),
    path('n/process_subscription/done', views.about, name='done'),

    path('n/process_subscription/online', views.online, name='online'),
    path('process_subscription/', views.process_subscription, name='process_subscription'),
    path('n',views.subscription, name='name'),
    path('n/process_subscription/download/<resolution>', views.yt_download_done, name='download_done'),
]