from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    # it will list all post without any filtering
    url(r'^$', views.post_list, name='post_list'),

    # it will call post list with tagged slug parameter
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),

    # url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    url(r'^search/$', views.post_search, name='post_search'),
]

# include your url in main url of the project
