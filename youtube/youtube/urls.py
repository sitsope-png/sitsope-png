
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
#url(r'^youtube/', include('youtubeapp.urls') )
path('paypal/', include('paypal.standard.ipn.urls')),
    path('', include('youtubeapp.urls')),
    path('compte/', include('compte.urls')),
]
