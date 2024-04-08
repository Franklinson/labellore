from django.contrib import admin
from blog.models import Blogs, Category
# Register your models here.

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "categories")
    list_filter = ("categories",)
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categories", )