import django_filters
# from django_filters import filterset

from people.models import Member


class MemberFilter(django_filters.FilterSet):

    class Meta:
        model = Member
        fields = {
            'member_type': ['exact'],
            'name': ['icontains'],
            'registration_no': ['exact'],
            'phone': ['exact']
        }