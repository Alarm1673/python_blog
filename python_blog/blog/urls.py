
from django.conf.urls import url
from blog.views import *
from blog.upload import upload_image

urlpatterns = [
    url(r"^uploads/(?P<path>.*)$", \
                "django.views.static.serve", \
                {"document_root": settings.MEDIA_ROOT,}),
    url(r'^about/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^$', index,  name='index'),
    #url(r'^$', index1,  name='index1'),
    url(r'^archive/$', archive,  name='archive'),
    url(r'^article/$', article, name='article'),
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^login', do_login, name='login'),
    url(r'^category/$', category, name='category'),
    url(r'^about', about, name='about'),
    url(r'^direct', direct, name='direct'),
    url(r'^tag', tag, name='tag'),

]
