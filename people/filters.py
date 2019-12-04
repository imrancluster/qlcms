from django_filters import FilterSet

from people.models import Member


class MemberFilter(FilterSet):

    class Meta:
        model = Member
        fields = ['name', 'registration_no', 'phone',]