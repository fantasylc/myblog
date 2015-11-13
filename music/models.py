from django.db import models

# Create your models here

SEX = {
    0: '男',
    1: '女',
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


class Singer(models.Model):
    name = models.CharField(max_length=30,  verbose_name='歌手名字')
    sex = models.IntegerField(default=None, null=True, blank=True, choices=SEX.items(), verbose_name="性别")
    summary = models.TextField(max_length=300, null=True, blank=True,verbose_name="简介")
    touxiang = models.CharField(max_length=100, default='/static/img/article/default.jpg', verbose_name="头像")
    create_time = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default=100, verbose_name="排序")

    class Meta:
        verbose_name_plural = verbose_name = '歌手'
        ordering = ['rank', '-create_time']
        app_label = string_with_title('music', '音乐管理')

    def __str__(self):
        return self.name


class Zhuanji(models.Model):
    author = models.ForeignKey(Singer, verbose_name="歌手")
    name = models.CharField(max_length=30, verbose_name='专辑名')
    img = models.CharField(max_length=100, null=True, blank=True)
    public_time = models.DateField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default=1000, verbose_name="排序")

    class Meta:
        verbose_name = verbose_name_plural = '专辑'
        ordering = ['rank', '-create_time']
        app_label = string_with_title('music', '音乐管理')

    def __str__(self):
        return self.name


class Song(models.Model):
    zhuanji = models.ForeignKey(Zhuanji, verbose_name='专辑')
    author = models.ForeignKey(Singer, verbose_name='歌手')
    name = models.CharField(max_length=30, verbose_name='歌名')
    img = models.CharField(max_length=100, null=True, blank=True)
    url = models.TextField(verbose_name='链接')
    is_top = models.BooleanField(default=False, verbose_name="置顶")
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '歌曲'
        ordering = ['-create_time']
        app_label = string_with_title('music', '音乐管理')

    def __str__(self):
        return self.name
