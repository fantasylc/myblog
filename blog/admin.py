from django.contrib import admin
from blog.models import Article, Category, Comment, Carousel
# Register your models here.
from django.db import models
from django.forms import TextInput,Textarea

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
       models.TextField: {'widget': Textarea(attrs={'rows':25, 'cols':80,'style':"font-size:16px;"})},
}



admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Carousel)
