#-*-coding:utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.
#定义显示信息
class ArticleAdmin(admin.ModelAdmin):
#fields显示列，exclude除此外的列显示
    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc', 'click_count' )

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'tag', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'article', 'content')


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Links)

