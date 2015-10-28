from django.contrib import admin
from blog.models import Article, Category, Comment, Carousel
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Carousel)