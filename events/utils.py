from events.models import Program


def get_presence_members_by_program_id(program_id):
    member_attended = Program.objects.get(id=program_id).members.all().order_by('-pk')

    return member_attended


def get_presence_member_ids_by_program_id(program_id):
    attended = []
    member_attended = Program.objects.get(id=program_id).members.all()
    for member in member_attended:
        attended.append(member.id)

    return member_attended


def get_program_history(program_id):
    member_attended = Program.objects.get(id=program_id).members.all()

    total_promaster = []
    total_promaster_male = []
    total_promaster_female = []
    total_graduate = []
    total_graduate_male = []
    total_graduate_female = []
    total_associate = []
    total_associate_male = []
    total_associate_female = []

    for member in member_attended:

        # Calculate Promaster
        if member.member_type == "QMP":
            total_promaster.append(member)
            if member.member_type == "QMP" and member.gender == "F":
                total_promaster_female.append(member)
            if member.member_type == "QMP" and member.gender == "M":
                total_promaster_male.append(member)

        # Calculate Graduate
        if member.member_type == "QG":
            total_graduate.append(member)
            if member.member_type == "QG" and member.gender == "F":
                total_graduate_female.append(member)
            if member.member_type == "QG" and member.gender == "M":
                total_graduate_male.append(member)

        # Calculate Associate
        if member.member_type == "QA":
            total_associate.append(member)
            if member.member_type == "QA" and member.gender == "F":
                total_associate_female.append(member)
            if member.member_type == "QA" and member.gender == "M":
                total_associate_male.append(member)

    return {
        'total': len(member_attended),
        'total_promaster': len(total_promaster),
        'total_promaster_male': len(total_promaster_male),
        'total_promaster_female': len(total_promaster_female),
        'total_graduate': len(total_graduate),
        'total_graduate_male': len(total_graduate_male),
        'total_graduate_female': len(total_graduate_female),
        'total_associate': len(total_associate),
        'total_associate_male': len(total_associate_male),
        'total_associate_female': len(total_associate_female),
        'total_male': len(total_promaster_male) + len(total_graduate_male) + len(total_associate_male),
        'total_female': len(total_promaster_female) + len(total_graduate_female) + len(total_associate_female),
    }
