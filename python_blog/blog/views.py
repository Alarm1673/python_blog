#coding:utf-8
from django.shortcuts import render
from django.conf import settings
from models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
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
        #分类信息获取(导航数据)
        category_list = Category.objects.all()
        #广告数据 TODO
        ad_list = Ad.objects.all()
        #标签云
        tag_list = Tag.objects.all()
        #最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list,2)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except(EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
        #文章归档
        #获取文章中的 年-月
        print Article.objects.values("date_publish").distinct()
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html',locals())