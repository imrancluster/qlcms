from django.core.exceptions import ObjectDoesNotExist

from helpers.models import Identification
from people.models import Member


def get_quantum_associate_id_bk(branch_id: int):
    """
    Get all QA for branch
    return summation of QA + 1

    :param branch_id:
    :return: int
    """
    total_qa = 1
    try:
        # identification = Identification.objects.filter(branch_id=branch_id).firtt()
        qa = Member.objects.filter(member_type="QA", branch_id=branch_id)
        total_qa = 1 if len(qa) == 0 else len(qa) + 1
    except ObjectDoesNotExist:
        pass

    return total_qa


def get_quantum_associate_id(branch_id: int):
    auto_number = ""

    try:
        identification = Identification.objects.filter(branch_id=branch_id).first()
        number = identification.qa + 1
        auto_number = identification.quantum_associate_prefix + str(number)
        identification.qa = number
        identification.save()

    except ObjectDoesNotExist:
        pass

    return auto_number


def get_matir_bank_code(branch_id: int):

    bank_code = ""

    try:
        bank_identification = Identification.objects.filter(branch_id=branch_id).first()
        number = bank_identification.bank_code + 1
        bank_code = bank_identification.bank_code_prefix + str(number)
        bank_identification.bank_code = number
        bank_identification.save()

    except ObjectDoesNotExist:
        pass

    return bank_code
