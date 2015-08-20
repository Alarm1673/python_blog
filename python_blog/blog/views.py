#coding:utf-8
from django.shortcuts import render
from django.conf import settings
import  logging
# Create your views here.

logger = logging.getLogger('blog.views')

#设置全局setting，读取setting文件
def global_setting(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC':settings.SITE_DESC ,
            'WEIBO_SINA':settings.WEIBO_SINA,
            'WEIBO_TENCENT':settings.WEIBO_TENCENT}

def index(request):
    return render(request, 'index.html',locals())