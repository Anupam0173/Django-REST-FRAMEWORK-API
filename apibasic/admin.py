from django.contrib import admin
from .models import Article

# Register your models her


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'email']


admin.site.register(Article, ArticleAdmin)
