from django.db import models


class Identification(models.Model):
    branch = models.ForeignKey('geography.Branch', on_delete=models.CASCADE)

    quantum_associate_prefix = models.CharField(max_length=20, unique=True, null=True)
    qa = models.IntegerField(default=0)

    bank_code_prefix = models.CharField(max_length=20, unique=True, null=True)
    bank_code = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.branch.name)
