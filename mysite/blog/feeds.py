from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    # these methods recieve each objects returned by items()
    # and return title and description for them.

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)



