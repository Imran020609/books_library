import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(field_name='published_data', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='published_data', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['author','title', 'min_date', 'max_date']




