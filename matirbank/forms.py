from string import Template

from django import forms
from django.utils.safestring import mark_safe

from matirbank.models import MatirBank
from people.models import Member, UserProfile
from people.utils import get_quantum_associate_id
from qlcms import settings
from qlcms.fields import MEMBER_TYPE_CHOICES, GENDER_CHOICES, MARITAL_STATUS_CHOICES, BLOOD_GROUP_CHOICES, YEARS, \
    MATIR_BANK_STATUS


class MatirBankForm(forms.ModelForm):
    bank_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    family_code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'input'}))
    distribution_date = forms.DateField(widget=forms.SelectDateWidget())
    collection_date = forms.DateField(widget=forms.SelectDateWidget())

    member = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'input'}))
    amount = forms.CharField(required=False, initial=0, widget=forms.TextInput(attrs={'class': 'input'}))
    status = forms.CharField(widget=forms.Select(choices=MATIR_BANK_STATUS, attrs={'class': 'input'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.formType = kwargs.pop('formType')

        super(MatirBankForm, self).__init__(*args, **kwargs)
        branch_id = UserProfile.objects.filter(user=self.user)[0].branch.id
        self.fields['member'].queryset = Member.objects.filter(branch=branch_id).order_by('-pk')

        if self.formType == 'new':
            del self.fields['collection_date']
        else:
            # self.fields['member'].widget.attrs['class'] = 'nwe class name comma sep'
            self.fields['member'].disabled = True

    class Meta:
        model = MatirBank
        fields = ('bank_code', 'family_code', 'distribution_date',
                  'collection_date', 'member', 'amount', 'status')
        # fields = '__all__'

    def save(self, branch_id=None, user_id = None):
        matirbank = super(MatirBankForm, self).save(commit=False)

        if branch_id:
            matirbank.branch_id = branch_id
        if user_id:
            matirbank.user_id = user_id

        matirbank.save()

        return matirbank