from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)

    # slug - a short label containing only letter,numbers, underscores.
    # used to build SEO friendly url for our blog posts

    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # we are telling django, that each post is written by user and a user can write several posts
    # many to one relationship
    # User - inbuilt model of django authentication system
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    # auto_now_add - saves date created automatically
    # auto_now - date will be updated automatically
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    class Meta:
        '''
         contains metadata
         will sort order by publish field
         in descending acc by default when we query
         db
        '''
        ordering = ('-publish',)

    def __str__(self):
        '''
        default human readable representation
        of object
        '''
        return self.title




