from django import forms
from events.models import Program, ProgramType
from people.models import UserProfile
from qlcms.fields import PROGRAM_STATUS


class ProgramForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=ProgramType.objects.all())
    title = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input'}))
    place = forms.CharField(min_length=2,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    phone = forms.CharField(required=False, min_length=8,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    mobile = forms.CharField(min_length=11, max_length=13,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    student_donation = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input'}))
    general_donation = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input'}))
    additional_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'input'}))
    status = forms.CharField(widget=forms.Select(choices=PROGRAM_STATUS, attrs={'class': 'input'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        branch_id = UserProfile.objects.filter(user=user)[0].branch.id
        super(ProgramForm, self).__init__(*args, **kwargs)
        if branch_id:
            self.fields['type'].queryset = ProgramType.objects.filter(branch_id=branch_id)

    class Meta:
        model = Program
        fields = ('type', 'title', 'date', 'place', 'phone',
                  'mobile', 'student_donation', 'general_donation',
                  'additional_info', 'status')

    def save(self, branch_id=None, user_id = None):
        program = super(ProgramForm, self).save(commit=False)

        if branch_id:
            program.branch_id = branch_id
        if user_id:
            program.user_id = user_id
        program.save()

        return program

