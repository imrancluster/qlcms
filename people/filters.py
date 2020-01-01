import django_filters

from people.models import Member, Contact


class MemberFilter(django_filters.FilterSet):

    class Meta:
        model = Member
        fields = {
            'member_type': ['exact'],
            'name': ['icontains'],
            'registration_no': ['exact'],
            'phone': ['exact']
        }


class ContactFilter(django_filters.FilterSet):

    class Meta:
        model = Contact
        fields = {
            'type': ['exact'],
        }
