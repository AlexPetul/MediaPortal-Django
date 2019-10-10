from django.contrib import admin
from mediaportal_app.models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name', )}


class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
