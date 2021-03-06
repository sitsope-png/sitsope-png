from django.contrib import admin

# Register your models here.
from youtubeapp.models import Entry, Language

admin.site.register(Entry)
admin.site.register(Language)