from django.contrib import admin
from .models import Letter, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class LetterAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]



# Register your models here.
admin.site.register(Letter, LetterAdmin )
admin.site.register(Comment)
