#coding:utf-8
from django.shortcuts import render
from django.conf import settings
from models import *
import  logging
# Create your views here.

logger = logging.getLogger('blog.views')

#设置全局setting，读取setting文件
def global_setting(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC':settings.SITE_DESC ,
            'WEIBO_SINA':settings.WEIBO_SINA,
            'WEIBO_TENCENT':settings.WEIBO_TENCENT,
            'PRO_RSS':settings.PRO_RSS,
            'PRO_EMAIL':settings.PRO_EMAIL}

def index(request):
    try:
        category_list = Category.objects.all()
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html',{'category_list':category_list})