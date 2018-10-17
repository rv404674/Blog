from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # this field is primary search field
    text = indexes.CharField(document=True, use_template=True)
    # publish field is a datetime field that will also be indexed
    # corresponds to publish field of post model
    publish = indexes.DateTimeField(model_attr='publish')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().published.all()