from django.conf.urls import url
from . import views
app_name = 'Blog'
urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^(?P<Post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^addlikes/(?P<Post_id>[0-9]+)/$', views.addlikes, name='addlikes'),
    url(r'^addcomment/(?P<Post_id>[0-9]+)/$', views.addcomment, name='addcomment'),
    url(r'^page/(\d+)/$', views.index, name='index'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^addpost/', views.addpost, name='addpost'),
    url(r'^regulations/', views.regulations, name='regulations'),
    url(r'^history/', views.history, name='history'),
]
