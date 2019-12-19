from string import Template

from django import forms
from django.utils.safestring import mark_safe

from matirbank.models import MatirBank
from people.models import Member
from people.utils import get_quantum_associate_id
from qlcms import settings
from qlcms.fields import MEMBER_TYPE_CHOICES, GENDER_CHOICES, MARITAL_STATUS_CHOICES, BLOOD_GROUP_CHOICES, YEARS


class MatirBankForm(forms.ModelForm):

    distribution_date = forms.DateField(widget=forms.SelectDateWidget())
    collection_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = MatirBank
        fields = ('bank_code', 'family_code', 'distribution_date',
                  'collection_date', 'member', 'amount','status')

    def save(self, branch_id=None, user_id = None):
        matirbank = super(MatirBankForm, self).save(commit=False)

        if branch_id:
            matirbank.branch_id = branch_id
        if user_id:
            matirbank.user_id = user_id

        matirbank.save()

        return matirbank