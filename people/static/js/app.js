$(function ($) {
    $('#id_member_type').change(function() {
        if ($(this).val() == 'QA') {
            $('#id_registration_no').val('AUTO');
            $('#id_registration_no').prop('disabled', true);
        } else {
            $('#id_registration_no').val('');
            $('#id_registration_no').prop('disabled', false);
        }
    });
});