import datetime
from itertools import chain

from matirbank.models import MatirBank
from people.models import UserProfile


def get_ready_banks(user, last_days=30):

    # @TODO: find ready banks for graduate, associate. Normally 90 days
    # @TODO: find ready banks for pro-master. Normally after 30 days
    # @TODO: make sure the bank status = distributed only

    branch_id = UserProfile.objects.filter(user=user)[0].branch.id
    matirbank_list1 = MatirBank.objects.filter(
        branch=branch_id,
        status="DISTRIBUTED",
        distribution_date__lte=datetime.datetime.today(),
        distribution_date__gt=datetime.datetime.today() - datetime.timedelta(days=last_days))

    matirbank_list2 = MatirBank.objects.filter(
        branch=branch_id,
        status="DISTRIBUTED",
        distribution_date__lte=datetime.datetime.today(),
        distribution_date__gt=datetime.datetime.today() - datetime.timedelta(days=10))

    # result_list = sorted(
    #     chain(page_list, article_list, post_list),
    #     key=lambda instance: instance.date_created)

    return list(chain(matirbank_list1, matirbank_list2))