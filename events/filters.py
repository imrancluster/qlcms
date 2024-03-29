import django_filters
from events.models import Program


class ProgramFilter(django_filters.FilterSet):

    class Meta:
        model = Program
        fields = {
            'title': ['icontains'],
            'status': ['exact'],
            'mobile': ['exact']
        }