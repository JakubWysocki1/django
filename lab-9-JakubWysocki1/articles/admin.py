from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Article, ArticleAdmin)
