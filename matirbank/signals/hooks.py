from django.db.models.signals import post_save
from django.dispatch import receiver

from matirbank.models import MatirBank, BankHistory


@receiver(post_save, sender=MatirBank)
def bank_post_save(sender, instance: MatirBank, created, **kwargs):
    # bank = kwargs.get('instance', None)
    # created = kwargs.get('created', False)
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
        last_history = BankHistory.objects.filter(bank=instance.id).last()
        if last_history and last_history.status != instance.status:
            instance.bankhistory_set.create(status=instance.status, bank=instance, user=login_user)
    else:
        instance.bankhistory_set.create(status=instance.status, bank=instance, user=login_user)
