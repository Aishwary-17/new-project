from django.contrib import admin

# Register your models here.

from .models import Date, Genre, News

admin.site.register(News)
admin.site.register(Date)
admin.site.register(Genre)
