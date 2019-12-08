from django import forms

from people.models import Member
from qlcms.fields import MEMBER_TYPE_CHOICES, GENDER_CHOICES, MARITAL_STATUS_CHOICES, BLOOD_GROUP_CHOICES, YEARS


class MemberForm(forms.ModelForm):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your name'}))
    member_type = forms.CharField(widget=forms.Select(choices=MEMBER_TYPE_CHOICES, attrs={'class': 'input'}))
    registration_no = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'input'}))

    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    phone = forms.CharField(min_length=11, max_length=13,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    address_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    address_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'input'}))
    marital_status = forms.CharField(widget=forms.Select(choices=MARITAL_STATUS_CHOICES, attrs={'class': 'input'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    blood_group = forms.CharField(widget=forms.Select(choices=BLOOD_GROUP_CHOICES, attrs={'class': 'input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    reference_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    additional_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'input'}))




    class Meta:
        model = Member
        fields = ('name', 'member_type', 'registration_no', 'gender', 'date_of_birth', 'phone',
                  'address_1', 'address_2', 'marital_status', 'occupation', 'blood_group', 'email',
                  'reference_name', 'additional_info', 'status')

    def save(self, branch_id=None, user_id = None):
        member = super(MemberForm, self).save(commit=False)
        if branch_id:
            member.branch_id = branch_id
        if user_id:
            member.user_id = user_id
        member.save()

        return member