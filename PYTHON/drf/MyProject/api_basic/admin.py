from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'email', 'date']


admin.site.register(Article, ArticleAdmin)