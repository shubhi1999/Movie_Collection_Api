from django_filters import rest_framework as filters
from .models import Collection

class CollectionFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    movies = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Collection
        fields = ['title', 'description', 'movies']