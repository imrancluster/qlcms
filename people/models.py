from django.contrib.auth.models import User
from django.db import models

from qlcms.fields import MEMBER_TYPE_CHOICES, GENDER_CHOICES, MARITAL_STATUS_CHOICES, BLOOD_GROUP_CHOICES, \
    MEMBER_CONTACT_TYPE_CHOICES


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
    is_quantier = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to='images/', blank=True)
    # default = 'pic_folder/None/no-img.jpg'

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

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


class Contact(models.Model):
    member = models.ForeignKey('people.Member', on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=MEMBER_CONTACT_TYPE_CHOICES)
    feedback = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

