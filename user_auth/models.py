from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self,memodict: self


class User(AbstractUser):
    intro = models.TextField(blank=True, null=True, verbose_name='简介')








