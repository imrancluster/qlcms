from django import forms
from django.utils.translation import gettext as _

from matirbank.models import MatirBank
from people.models import Member, UserProfile
from qlcms.fields import MATIR_BANK_STATUS


class MatirBankForm(forms.ModelForm):
    bank_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    family_code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'input'}))
    distribution_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input'}))
    collection_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input'}))

    member = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'input'}),
                                    empty_label=_("Select Member"))
    amount = forms.CharField(required=False, initial=0, widget=forms.TextInput(attrs={'class': 'input'}))
    status = forms.CharField(widget=forms.Select(choices=MATIR_BANK_STATUS, attrs={'class': 'input'}))
    money_receipt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'style': 'display:none;margin-top:10px;',
               'placeholder': 'Enter money receipt number'}),
        label="", required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.formType = kwargs.pop('formType')

        super(MatirBankForm, self).__init__(*args, **kwargs)

        branch_id = UserProfile.objects.filter(user=self.user)[0].branch.id
        self.fields['member'].queryset = Member.objects.filter(branch=branch_id).order_by('-pk')

        if self.formType == 'new':
            del self.fields['collection_date']
            del self.fields['money_receipt']
        else:
            # self.fields['member'].widget.attrs['class'] = 'nwe class name comma sep'
            self.fields['member'].disabled = True

    class Meta:
        model = MatirBank
        fields = ('bank_code', 'family_code', 'distribution_date',
                  'collection_date', 'member', 'amount', 'status', 'money_receipt')
        # fields = '__all__'

    def save(self, branch_id=None, user_id=None):
        matirbank = super(MatirBankForm, self).save(commit=False)

        if branch_id:
            matirbank.branch_id = branch_id
        if user_id:
            matirbank.user_id = user_id

        matirbank.save()

        return matirbank
