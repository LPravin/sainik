$("#filter").click(function (){
    const url = 'ajax/filter_esm';
    const name = $('#id_name_contains').val();
    const rt = $('#id_registration_types').val();
    const et = $('#id_esm_type').val();
    const rc = $('#id_rank_categories').val();
    const ro = $('#id_record_offices').val();
    const service = $('#id_services').val();
    const trade = $('#id_trades').val();
    const cq = $('#id_civil_qualifications').val();
    const es = $('#id_employment_status').val();
    const er = $("#id_employment_registration").val();
    const sj = $("#id_security_job").val();
    const ms = $("#id_marital_status").val();
    const ac = $("#id_age_completed").val();
    const dd = $("#id_dob_date").val();
    const ed = $("#id_enrollment_date").val();
    const edc = $("#id_ed_conditions").val();
    const dod = $("#id_date_of_discharge").val();
    const dc = $("#id_dod_conditions").val();
    const city = $("#id_city").val();
    const dis = $("#id_district").val();
    const st = $("#id_state").val();
    $.ajax({
            url: url,
            data: {
                'name': name,
                'rt': rt,
                'rc': rc,
                'ro': ro,
                'service': service,
                'trade': trade,
                'cq': cq,
                'es': es,
                'et': et,
                'er': er,
                'sj': sj,
                'ms': ms,
                'ac': ac,
                'dd': dd,
                'ed': ed,
                'edc': edc,
                'dod': dod,
                'dc': dc,
                'city': city,
                'dis': dis,
                'st':st
            },
            success: function (data) {
                $('#esm_list').html(data);
            }
        });
});
