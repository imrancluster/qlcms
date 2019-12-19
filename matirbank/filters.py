import django_filters
# from django_filters import filterset
from matirbank.models import MatirBank


class MatirBankFilter(django_filters.FilterSet):

    class Meta:
        model = MatirBank
        fields = {
            'bank_code': ['exact'],
            'member': ['exact'],
            'distribution_date': ['exact']
        }