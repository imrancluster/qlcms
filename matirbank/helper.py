import datetime
from itertools import chain

from matirbank.models import MatirBank
from people.models import UserProfile


def get_ready_banks(user, last_days=30):

    branch_id = UserProfile.objects.filter(user=user)[0].branch.id
    matirbank_list1 = MatirBank.objects.filter(
        branch=branch_id,
        status="DISTRIBUTED",
        distribution_date__lte=datetime.datetime.today() - datetime.timedelta(days=90))\
        .exclude(member__member_type="QMP")

    matirbank_list2 = MatirBank.objects.filter(
        branch=branch_id,
        status="DISTRIBUTED",
        distribution_date__lte=datetime.datetime.today() - datetime.timedelta(days=last_days),
        member__member_type="QMP")

    result_list = sorted(
        chain(matirbank_list1, matirbank_list2),
        key=lambda instance: instance.distribution_date)

    return result_list
