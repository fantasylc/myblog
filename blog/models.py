from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

STATUS = {
    0: '正常',
    1: '草稿',
    2: '删除',
}

class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name='分类名称')
    parent = models.ForeignKey('self',default=None, blank=True,null=True,verbose_name="上级分类")
    rank = models.IntegerField(default=0, verbose_name="排序")
    status = models.IntegerField(default=0, choices=STATUS.items(),verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '分类'
        ordering = ['rank', '-create_time']
        app_label = string_with_title('blog', '博客管理')

    def __str__(self):
        if self.parent:
            return '%s->%s' %(self.parent, self.name)
        else:
            return self.name


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')
    category = models.ForeignKey(Category, verbose_name="分类")
    title = models.CharField(max_length=100, verbose_name="标题")
    img = models.CharField(max_length=200, default='/static/img/article/default.jpg')
    tags = models.CharField(max_length=200, null=True, verbose_name="标签")
    summary = models.TextField(verbose_name="摘要")
    content = models.TextField(verbose_name="正文")

    view_times = models.IntegerField(verbose_name="浏览次数", default=0)
    zan_times = models.IntegerField(default=0, verbose_name='赞')

    is_top = models.BooleanField(default=False, verbose_name="置顶")
    rank = models.IntegerField(default=0, verbose_name="排序")
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    pub_time = models.DateTimeField(default=False, verbose_name="发布时间")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_tags(self):
        return self.tags.split(',')

    class Meta:
        verbose_name_plural = verbose_name = "文章"
        ordering = ['-create_time']
        app_label = string_with_title('blog', "博客管理")

    def __str__(self):
        return self.title


class Suibi(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')
    title = models.CharField(max_length=80, verbose_name="标题")
    img = models.CharField(max_length=200, default='/static/img/article/default.jpg')
    tags = models.CharField(max_length=30, null=True, verbose_name="标签")
    content = models.TextField(verbose_name="正文")
    summary = models.CharField(max_length=200, verbose_name="摘要")
    view_times = models.IntegerField(verbose_name="浏览次数", default=0)
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name='状态')
    is_top = models.BooleanField(default=False, verbose_name="置顶")
    create_time = models.DateTimeField(auto_now_add=True)
    pub_time = models.DateTimeField(default=False, verbose_name="发布时间")

    def get_tags(self):
        return self.tags.split(',')

    class Meta:
        verbose_name_plural = verbose_name = "随笔"
        ordering = ['-create_time']
        app_label = string_with_title('blog', "博客管理")

    def __str__(self):
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')
    article = models.ForeignKey(Article, verbose_name="文章")
    content = models.TextField(max_length=300, verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name_plural = verbose_name = "评论"
        ordering = ['-create_time']
        app_label = string_with_title('blog', '博客管理')
    
    def __str__(self):
        return self.content[0:20]


class Commentsuibi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')
    article = models.ForeignKey(Suibi, verbose_name="随笔")
    content = models.TextField(max_length=300, verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name_plural = verbose_name = "随笔评论"
        ordering = ['-create_time']
        app_label = string_with_title('blog', '博客管理')

    def __str__(self):
        return self.content[0:20]


class Carousel(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    summary = models.TextField(blank=True, null=True, verbose_name='摘要')
    img = models.CharField(max_length=200, verbose_name='轮拨图', default='/static/img/carousel/python.jpg')
    article = models.ForeignKey(Article, verbose_name='文章')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '轮播'
        ordering = ['-create_time']
        app_label = string_with_title('blog', '博客管理')

    def __str__(self):
        return self.title


class Leavemessage(models.Model):
    message = models.TextField(verbose_name='消息')
    name = models.CharField(max_length=30, verbose_name='姓名')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '留言'
        ordering = ['-create_time']
        app_label = string_with_title('blog', '博客管理')

    def __str__(self):
        return self.message

