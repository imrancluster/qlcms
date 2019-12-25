from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from qlcms.fields import MATIR_BANK_STATUS


class MatirBank(models.Model):
    bank_code = models.CharField(max_length=20, unique=True)
    family_code = models.CharField(max_length=20, null=True, blank=True)
    distribution_date = models.DateField(blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)

    branch = models.ForeignKey('geography.Branch', on_delete=models.CASCADE)
    member = models.ForeignKey('people.Member', on_delete=models.DO_NOTHING)

    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0, blank=True)
    status = models.CharField(max_length=50, blank=True, choices=MATIR_BANK_STATUS)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    money_receipt = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class BankHistory(models.Model):
    status = models.CharField(max_length=20, null=True, blank=True)
    bank = models.ForeignKey('matirbank.MatirBank', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


# creare history using django signals
def create_bank_history(sender, **kwargs):
    bank = kwargs.get('instance', None)
    created = kwargs.get('created', False)
    raw = kwargs.get('raw', False)

    # get request for logged in user
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            login_user = request.user
            break
    else:
        login_user = None

    if created is False:
        last_history = BankHistory.objects.filter(bank=bank.id).last()
        if last_history and last_history.status != bank.status:
            bank.bankhistory_set.create(status=bank.status, bank=bank, user=login_user)
    else:
        bank.bankhistory_set.create(status=bank.status, bank=bank, user=login_user)


post_save.connect(create_bank_history, sender=MatirBank)
