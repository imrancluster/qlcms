from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

BRANCH_TYPE = [
    ('BRANCH', 'Branch'),
    ('CELL', 'Cell'),
    ('PRECELL', 'Pre Cell')
]

COUNTRY_CODE = [
    ('BD', 'BD'),
    ('US', 'US')
]

class Branch(models.Model):
    name = models.CharField(max_length=150)
    branch_code = models.CharField(max_length=50, unique=True)
    branch_type = models.CharField(max_length=50, blank=True, choices=BRANCH_TYPE)
    address = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=True, verbose_name=_('Status'))
    additional_info = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    country_code = models.CharField(max_length=50, blank=True, choices=COUNTRY_CODE)
    area = models.ForeignKey('geography.Area', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


class Division(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50)
    division = models.ForeignKey('geography.Division', on_delete=models.CASCADE)

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey('geography.District', on_delete=models.CASCADE)

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    def __str__(self):
        return self.name