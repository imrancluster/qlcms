from django.db import models
from django.contrib.auth.models import User

from qlcms.fields import PROGRAM_STATUS


class ProgramType(models.Model):
    name = models.CharField(max_length=150)
    branch = models.ForeignKey('geography.Branch', on_delete=models.CASCADE)

    @staticmethod
    def autocomplete_search_fields():
        return 'name',

    def __str__(self):
        return '{} - {}'.format(self.name, self.branch.name)


class Program(models.Model):
    type = models.ForeignKey('ProgramType', on_delete=models.CASCADE)
    branch = models.ForeignKey('geography.Branch', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150)
    mobile = models.CharField(max_length=13, db_index=True)
    student_donation = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    general_donation = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    additional_info = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, choices=PROGRAM_STATUS)

    members = models.ManyToManyField('people.Member', blank=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all_members(cls, pk):
        return cls.objects.get(id=pk).members.all()

    @staticmethod
    def autocomplete_search_fields():
        return 'title',

    def __str__(self):
        return self.title

