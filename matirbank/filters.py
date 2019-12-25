import django_filters
from django.utils.translation import gettext as _
from matirbank.models import MatirBank
from people.models import UserProfile, Member


def custom_member_queryset(request):
    if request is None:
        return Member.objects.none()

    branch_id = UserProfile.objects.filter(user=request.user)[0].branch.id
    return Member.objects.filter(branch=branch_id).order_by('-pk')


class MatirBankFilter(django_filters.FilterSet):

    member = django_filters.ModelChoiceFilter(queryset=custom_member_queryset, empty_label=_("Select Member"))

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user')
        self.branch_id = UserProfile.objects.filter(user=self.user)[0].branch.id

        super(MatirBankFilter, self).__init__(*args, **kwargs)





    class Meta:
        model = MatirBank
        fields = {
            'bank_code': ['exact'],
            'member': ['exact'],
            'status': ['exact']
        }
