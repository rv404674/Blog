from django.contrib import admin
from .models import Post


#list_display - allows us to show customized fields
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')

    #slug field will automatically fill itself with title field
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


# PostAdmin is a custom class that inherits from model admin
# Use to show some specified things
admin.site.register(Post, PostAdmin)

# Register your models here.
