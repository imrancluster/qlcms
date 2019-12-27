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

    $('#id_status').change(function() {
        if ($(this).val() == 'MONEY_RECEIPT') {
            $('#id_money_receipt').show('slow');
        } else {
            $('#id_money_receipt').hide('slow');
        }
    });

    $("#id_date_of_birth, #id_distribution_date, #id_collection_date, #id_date")
        .datepicker({
        format:'yyyy-mm-dd',
    });
});