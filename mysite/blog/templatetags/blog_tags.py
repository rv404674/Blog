from django import template
from django.db.models import Count

# Each template tag module needs to contain a variable register
# to be a valid tag library

# Use to register your own template library and filter
register = template.Library()

from ..models import Post


# simple_tag, inclusion_tag and assignment_tag see notebook.

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

#create an assignmment tag to display most commented post
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
