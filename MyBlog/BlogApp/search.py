import django_filters
from .models import BlogPost


class PostSearch(django_filters.FilterSet):
    class Meta:
        model = BlogPost
        fields = ('postHeader', 'postData')
