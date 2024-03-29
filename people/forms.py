from string import Template

from django import forms
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe

from people.models import Member, UserProfile, Contact
from people.utils import get_quantum_associate_id
from qlcms.fields import MEMBER_TYPE_CHOICES, GENDER_CHOICES, MARITAL_STATUS_CHOICES, BLOOD_GROUP_CHOICES, YEARS, \
    MEMBER_CONTACT_TYPE_CHOICES


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img src="/media/$link"/>""")
        return mark_safe(html.substitute(link=value))


class MemberForm(forms.ModelForm):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your name'}))
    member_type = forms.CharField(widget=forms.Select(choices=MEMBER_TYPE_CHOICES, attrs={'class': 'input'}))
    registration_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'input'}))
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'input'}))

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'input'}))

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
    # avatar = forms.ImageField(widget=PictureWidget)


    class Meta:
        model = Member
        fields = ('name', 'member_type', 'registration_no', 'gender', 'date_of_birth', 'phone',
                  'address_1', 'address_2', 'marital_status', 'occupation', 'blood_group', 'email',
                  'reference_name', 'additional_info', 'status', 'is_quantier', 'avatar')

    def save(self, branch_id=None, user_id = None):
        member = super(MemberForm, self).save(commit=False)

        # avatar image file
        # image = Image.open(photo.file)
        # cropped_image = image.crop((x, y, w + x, h + y))
        # resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        # resized_image.save(photo.file.path)

        # TODO: avoid following function if this form is a update form
        if branch_id:
            member.branch_id = branch_id
        if user_id:
            member.user_id = user_id

        if member.member_type == "QA" and member.registration_no == "":
            member.registration_no = get_quantum_associate_id(branch_id)
        member.save()

        return member


class ContactForm(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'input'}),
                                    empty_label=_("Select Member"))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super(ContactForm, self).__init__(*args, **kwargs)
        branch_id = UserProfile.objects.filter(user=self.user)[0].branch.id
        self.fields['member'].queryset = Member.objects.filter(branch=branch_id).order_by('-pk')

    class Meta:
        model = Contact
        fields = ('member', 'type', 'feedback')

    def save(self, user_id=None):
        contact = super(ContactForm, self).save(commit=False)

        if user_id:
            contact.user_id = user_id
        contact.save()

        return contact


class SimpleContactForm(forms.ModelForm):
    type = forms.CharField(widget=forms.Select(choices=MEMBER_CONTACT_TYPE_CHOICES, attrs={'class': 'input'}))
    feedback = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input'}))

    class Meta:
        model = Contact
        fields = ('type', 'feedback')
