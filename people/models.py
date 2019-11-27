from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


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

class Member(models.Model):
    name = models.CharField(max_length=150)
    branch = models.ForeignKey('geography.Branch', on_delete=models.CASCADE)
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPE_CHOICES, blank=True)
    registration_no = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=13, db_index=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    marital_status = models.CharField(max_length=50, blank=True, choices=MARITAL_STATUS_CHOICES)
    occupation = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
    email = models.CharField(max_length=100, blank=True)
    reference_name = models.CharField(max_length=150)
    additional_info = models.TextField(blank=True)
    status = models.BooleanField(default=True)

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey('geography.Branch', on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, db_index=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username