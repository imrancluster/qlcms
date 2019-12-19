from django.core.exceptions import ObjectDoesNotExist

from events.models import Program
from people.models import Member


def get_quantum_associate_id(branch_id: int):
    """
    Get all QA for branch
    return summation of QA + 1

    :param branch_id:
    :return: int
    """
    total_qa = 1
    try:
        qa = Member.objects.filter(member_type="QA", branch_id=branch_id)
        total_qa = 1 if len(qa) == 0 else len(qa) + 1
    except ObjectDoesNotExist:
        pass

    return total_qa
