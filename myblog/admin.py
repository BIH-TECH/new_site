from django.contrib import admin
from .models import  Tag, Category, Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author","created_time", "category" ]
    list_filter = ['author']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)