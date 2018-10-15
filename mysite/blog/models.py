from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


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


    object = models.Manager() # The default manager.
    published = PublishedManager()

    # Tag Manager will allow you to add, delete remove, tags from post object
    tags = TaggableManager()

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

    def get_absolute_url(self):
        # This looks through all urls defined in urls.py for the url defined with name='post_detail'
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])


class Comment(models.Model):

    '''
    Many to one relationship - Many comment -> One Post
    related_name attribute allows us to name the attribute that we use for the relation from the related object back to this one
    after defining this one use "Comment.Post" to retrieve post of a comment object
    use "Post.comments.all()" to retrieve all comments of a Post
    '''
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)






