from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    categories = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.categories}'
    
    class Meta:
        verbose_name_plural = "Category"
    
    
class Blogs(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    body = RichTextUploadingField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} - {self.categories}'
    
    class Meta:
        verbose_name_plural = "Blogs"