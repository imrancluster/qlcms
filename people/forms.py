from django import forms

from people.models import Member
from qlcms.fields import MEMBER_TYPE_CHOICES


class MemberForm(forms.ModelForm):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your name'}))
    member_type = forms.CharField(widget=forms.Select(choices=MEMBER_TYPE_CHOICES, attrs={'class': 'input'}))

    class Meta:
        model = Member
        fields = ('name', 'member_type', 'registration_no', 'gender', 'date_of_birth', 'phone',
                  'address_1', 'address_2', 'marital_status', 'occupation', 'blood_group', 'email',
                  'reference_name', 'additional_info', 'status')

    def save(self, branch_id=None):
        member = super(MemberForm, self).save(commit=False)
        if branch_id:
            member.branch_id = branch_id
        member.save()

        return member