#coding:utf-8

import os
import sys
import importlib

importlib.reload(sys)
#sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE","myblog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


