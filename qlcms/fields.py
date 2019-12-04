from django.utils.translation import ugettext_lazy as _

BOOLEAN_SELECT_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),
)

GENDER_CHOICES = [
    ('F', 'Female'),
    ('M', 'Male'),
    ('OTR', 'Others'),
]

MARITAL_STATUS_CHOICES = [
    ('UNMARRIED', _('Single / Never Married')),
    ('MARRIED', _('Married')),
    ('DIVORCED', _('Divorced')),
    ('SEPARATED', _('Separated')),
    ('WIDOWED', _('Widowed')),
]

BLOOD_GROUP_CHOICES = [
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

MEMBER_TYPE_CHOICES = [
    ('QMP', 'QMP'),
    ('QG', 'QG'),
    ('QA', 'QA'),
]

YEARS= [x for x in range(1940, 2021)]